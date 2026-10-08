import os
import anthropic
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")
print("Có key:", bool(key), "| Độ dài:", len(key) if key else 0)
print("Bắt đầu bằng sk-ant:", key.startswith("sk-ant") if key else False)

client = anthropic.Anthropic(api_key=key)
try:
    msg = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=50,
        messages=[{"role": "user", "content": "Xin chào"}],
    )
    print("THÀNH CÔNG:", msg.content[0].text)
except Exception as e:
    print("LỖI:", type(e).__name__)
    print(e)