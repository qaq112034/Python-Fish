import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(encoding='utf-8-sig')

client = OpenAI(
    api_key = os.getenv("DEEPSEEK_API_KEY"),
    base_url = "https://api.deepseek.com"
)

def chat_with_ai(user_message):
    response = client.chat.completions.create(
        model = "deepseek-chat",
        messages = [{"role" : "user", "content" : user_message}]
    )
    return response.choices[0].message.content

while True :
    user_input = input("请输入你的问题:")
    if user_input == "exit":
        break
    reply = chat_with_ai(user_input)
    print("AI回复:",reply)

