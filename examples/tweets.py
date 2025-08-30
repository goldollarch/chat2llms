import os
import csv
from datetime import datetime

import tweepy

# 从环境变量获取凭证（推荐安全做法）
CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Retrieve up to 100 Posts and 500 write per month

def get_twitter_client():
    """创建认证的 Twitter 客户端"""
    return tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        wait_on_rate_limit=True
    )

def search_tweets(query, max_results=100):
    """执行推文搜索"""
    client = get_twitter_client()
    
    try:
        response = client.search_recent_tweets(
            query=f"{query} -is:retweet has:links",  # 排除转推且包含链接
            tweet_fields=["author_id", "created_at", "public_metrics", "lang"],
            user_fields=["name", "username", "verified"],
            expansions="author_id",
            max_results=max_results
        )
        
        return response
    
    except tweepy.TweepyException as e:
        print(f"API Error: {e}")
        return None

def save_to_csv(tweets_data, filename):
    """将数据保存到 CSV 文件"""
    if not tweets_data:
        return

    # 创建安全文件名
    safe_filename = "".join([c if c.isalnum() else "_" for c in filename])[:50]
    csv_filename = f"{safe_filename}_{datetime.now().strftime('%Y%m%d')}.csv"

    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'tweet_id', 'created_at', 'text', 'language',
            'author_id', 'author_name', 'author_handle', 'verified',
            'likes', 'retweets', 'replies', 'quotes'
        ]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for tweet in tweets_data:
            writer.writerow({
                'tweet_id': tweet['id'],
                'created_at': tweet['created_at'].strftime('%Y-%m-%d %H:%M:%S UTC'),
                'text': tweet['text'].replace('\n', ' '),  # 去除换行符
                'language': tweet['lang'],
                'author_id': tweet['author_id'],
                'author_name': tweet['author_name'],
                'author_handle': tweet['author_handle'],
                'verified': tweet['verified'],
                'likes': tweet['likes'],
                'retweets': tweet['retweets'],
                'replies': tweet['replies'],
                'quotes': tweet['quotes']
            })
    
    print(f"数据已保存到 {csv_filename} (共 {len(tweets_data)} 条推文)")

def process_tweets(response):
    """处理 API 返回数据"""
    if not response or not response.data:
        return []
    
    # 构建用户信息映射表
    user_map = {user.id: user for user in response.includes['users']}
    
    processed = []
    for tweet in response.data:
        user = user_map[tweet.author_id]
        processed.append({
            'id': tweet.id,
            'created_at': tweet.created_at,
            'text': tweet.text,
            'lang': tweet.lang,
            'author_id': tweet.author_id,
            'author_name': user.name,
            'author_handle': user.username,
            'verified': user.verified,
            'likes': tweet.public_metrics['like_count'],
            'retweets': tweet.public_metrics['retweet_count'],
            'replies': tweet.public_metrics['reply_count'],
            'quotes': tweet.public_metrics['quote_count']
        })
    
    return processed

if __name__ == "__main__":
    # 配置参数
    search_topic = "Picking Quarrels and Provoking Trouble"    # 寻衅滋事
    result_count = 50           # Picking Quarrels and Provoking Trouble
    
    # 执行搜索
    response = search_tweets(search_topic, max_results=result_count)
    
    if response:
        # 处理数据
        tweets_data = process_tweets(response)
        
        # 保存结果
        if tweets_data:
            save_to_csv(tweets_data, search_topic.lower().replace(" ", "_"))
        else:
            print("未找到相关推文")
    else:
        print("搜索失败，请检查API凭证和网络连接")

