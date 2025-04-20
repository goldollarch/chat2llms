import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../src') )

from chat2llms.analyzer import AnswerComparator
from chat2llms.model_response import OpenAIResponse, GeminiResponse
from chat2llms.base_client import BaseClient
from chat2llms.output_files import WriteMarkDown

if __name__ == "__main__":

    # 初始化客户端
    gemini = BaseClient("gemini")
    deepseek = BaseClient("deepseek")

    # 获取响应
    gemini_response = GeminiResponse(gemini)
    deepseek_response = OpenAIResponse(deepseek)

    comparator = AnswerComparator([gemini_response, deepseek_response])

    question = "量子计算对传统密码学的主要影响是什么？"
    responses = comparator.get_answers(question)

    analysis = comparator.analyze_answers(responses)
    report = comparator.generate_report(analysis, question)
    print(report)

    # # 保存报告
    # with open("analysis_report.md", "w") as f:
    #     f.write(report)
