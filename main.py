from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # 加载
api_key = os.getenv("DEEPSEEK_API_KEY")  # 导入apikey
base_url = "https://api.deepseek.com"
client = OpenAI(api_key=api_key, base_url=base_url)  # 创建client
model = "deepseek-chat"  # 使用官方支持的模型名字
response = client.chat.completions.create(
    model=model,
    messages=[{"role": "user", "content": "我喜欢你"}]
    # n=2 可以添加n等于2来获取多个结果
    )
print(response.choices[0].message.content) # 输出结果  里面的0是获取第一个结果
