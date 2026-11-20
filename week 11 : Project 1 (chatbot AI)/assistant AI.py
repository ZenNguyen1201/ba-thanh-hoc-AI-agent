import os 
import time
import anthropic
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-5-5"
PRICE_IN = 2.00
PRICE_OUT = 10.00
total_cost = 0.00
MAX_COST = 0.20
SYSTEM_PROMPT = (
    "Ban la tro ly thien van cho sinh vien nganh ky thuat vu tru. "
    "Tra loi de hieu, ngan gon, khong dai qua 3 den 4 cau, co so lieu cu the khi phu hop. "
    "Neu khong chac chan hoac so lieu co the da cu, hay noi ro."
    "Chi tra loi cau hoi ve ky thuat vu tru, thien van va vat ly. "
    "Neu cau hoi nam ngoai pham vi nay, tu choi lich su trong 1-2 cau."
    "Duoc phep tra loi ve AI, lap trinh va toan hoc khi chung ap dung vao vu tru hoac thien van. "
    "Rieng khi nguoi xin code, duoc phep dai hon nhung chi dua code can thiet va giai thich ngan."
)


def get_text(msg) -> str:
    """Join all text block and skip thinking text block."""
    return "".join(block.text for block in msg.content if block.type == "text")



def calc_cost(usage) -> float:
    """Calculate the price of input and output when call."""
    cost_in = usage.input_tokens / 1_000_000 * PRICE_IN
    cost_out = usage.output_tokens / 1_000_000 * PRICE_OUT
    return cost_in + cost_out


def log_usage(msg):
    global total_cost
    cost = calc_cost(msg.usage)
    total_cost = total_cost + cost  #sai va da sua lai
    print(f"[usage] input={msg.usage.input_tokens} output={msg.usage.output_tokens} total=${total_cost:.6f}")


def stream_chat(history: list) -> str:
    start = time.perf_counter()
    ttft = None
    with client.messages.stream(
        model=MODEL,
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=history,
    ) as stream:
        for piece in stream.text_stream:
            if ttft is None:
                ttft = time.perf_counter() - start
            print(piece,end="",flush=True)
        final=stream.get_final_message()
    total = time.perf_counter() - start
    print()
    log_usage(final)
    print(f"[time] TTFT={ttft:.2f}s total={total:.2f}s")
    return get_text(final)


if __name__ == "__main__":
    history = []
    try:
        while True:
            user_input = input("\nBan: ").strip()

            if user_input.lower() in ("exit", "stop"):
                print(f"\nFinal price: ${total_cost:.6f}")
                break
            if user_input == "cost":
                print(f"Final cost now: ${total_cost:.6f}")
                continue
            if user_input == "reset":
                history.clear()
                print("The history is clear.")
                continue
            if user_input == "/paste":
                print("Paste the content. Go /end on single line to send.")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "/end":
                        break
                    lines.append(line)
                user_input = "\n".join(lines)
            if user_input == "":
                continue
                       
            
            if total_cost >= MAX_COST:
                print(f"The limit of price ${MAX_COST:.2f}. Dung Chatbot.")
                break

            history.append({"role": "user", "content": user_input})
            print("Claude: ", end="")
            reply = stream_chat(history)
            history.append({"role": "assistant", "content": reply})
    except Exception as e:
        print("Loi: ", type(e).__name__)
        print(e)

