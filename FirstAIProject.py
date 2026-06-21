from openai import OpenAI

client = OpenAI(
    api_key="前往Deeseek获得key",
    base_url="https://api.deepseek.com"
)

history = []

def chat_with_ai(user_message):
    """向 DeepSeek 提问，返回 AI 的回复"""
    history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages = history,
)
    history.append({"role":"assistant", "content":response.choices[0].message.content})
    return response.choices[0].message.content


# --- 调用函数 ---
while True:
    user_input = input("我：")
    if user_input == "exit":
        break
    reply = chat_with_ai(user_input)
    print("AI 回复：", reply)
