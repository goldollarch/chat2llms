import os, sys
import requests
import json
from typing import List, Dict

sys.path.append(os.path.join(os.path.dirname(__file__),'..') )

from src.chat2llms.model_response import OpenAIResponse, GeminiResponse
from src.chat2llms.base_client import BaseClient, load_config, logger

#######################################
class GeminiChatClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-pro-exp:generateContent"
        self.history: List[Dict] = []  # 存储完整对话历史
        self.max_history = 20  # 最大保留历史轮次 

    def _build_payload(self, prompt: str) -> Dict:
        """构造包含聊天历史的请求体"""
        parts = [{"text": prompt}]
        
        # 添加历史上下文（排除系统指令）
        context = [
            {"role": entry["role"], "parts": [{"text": entry["content"]}]}
            for entry in self.history[-self.max_history:] 
            if entry["type"] == "chat"
        ]
        
        return {
            "contents": context + [{"role": "user", "parts": parts}],
            "generationConfig": {
                "temperature": 0.9,
                "maxOutputTokens": 2048
            }
        }

    def _parse_response(self, response: Dict) -> str:
        """解析API响应并提取文本内容"""
        try:
            return response["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError) as e:
            raise ValueError(f"无效的API响应结构: {str(e)}")

    def get_responses(self, prompt: str) -> str:
        """执行带历史管理的对话"""
        try:
            # 构造请求头
            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": self.api_key
            }

            # 添加当前对话到历史
            self.history.append({
                "type": "chat",
                "role": "user",
                "content": prompt
            })

            # 发送API请求
            response = requests.post(
                self.api_url,
                headers=headers,
                json=self._build_payload(prompt)
            )
            response.raise_for_status()

            # 解析响应
            ai_response = self._parse_response(response.json())

            # 记录AI响应历史
            self.history.append({
                "type": "chat",
                "role": "model",
                "content": ai_response
            })

            return ai_response

        except requests.exceptions.RequestException as e:
            # 网络错误处理
            self.history.append({
                "type": "system",
                "content": f"网络错误: {str(e)}"
            })
            return f"API请求失败: {str(e)}"
        
        except json.JSONDecodeError:
            # JSON解析错误
            return "响应解析失败"

    def clear_history(self):
        """清空对话历史"""
        self.history = []

# 使用示例
if __name__ == "__main__":

    # client = GeminiChatClient()
    # while True:
    #     try:
    #         user_input = input("You: ")
    #         if user_input.lower() == 'exit':
    #             break
                
    #         response = client.get_responses(user_input)
    #         print(f"Gemini: {response}")            
    #     except KeyboardInterrupt:
    #         print("\n对话已终止")
    #         break

    try:
        config = load_config()
        print("可用的聊天模型：", list(config.keys()))
        
        provider = input("请选择聊天模型: ").strip().lower()
        
        client = BaseClient(provider, config)           
        if provider == "gemini":
            Res_model = GeminiResponse(client)
        else:
            Res_model = OpenAIResponse(client)
        
        print("\n输入 'exit' 结束对话")
        print("输入 'clear' 清除历史记录\n")        
        
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    break
                if user_input.lower() == 'clear':
                    history = []
                    print("\n历史记录已清除\n")
                    continue
                
                response, history = Res_model.get_response_history(user_input)
                print(f"\nAI: {response}\n")
                print(f"\nAI: {history}\n")
                
            except KeyboardInterrupt:
                print("\n对话已终止")
                break
            except RuntimeError as e:
                print(f"\n错误: {str(e)}")
                logger.error(f"请求处理失败: {str(e)}")
            except Exception as e:
                print("\n发生未知错误")
                logger.exception(f"未处理的异常: {str(e)}")
                
    except Exception as e:
        logger.exception("程序初始化失败")
        print("程序启动失败，请检查配置文件和日志")
