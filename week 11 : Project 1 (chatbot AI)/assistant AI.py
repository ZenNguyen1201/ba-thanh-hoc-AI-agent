import os
import anthropic
import time
from dotenv import load_dotenv , find_dotenv

load_dotenv(find_dotenv())
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-5-5"
PRICE_IN = 2.00
PRICE_OUT = 10.00
total_cost = 0.00
SYSTEM_PROMPT = (
    "Ban la tro ly thien van cho sinh vien nganh ky thuat vu tru. "
    "Tra loi de hieu, ngan gon, co so lieu cu the khi phu hop. "
    "Neu khong chac chan hoac so lieu co the da cu, hay noi ro."
)


def get_text(msg) -> str:
    """Join all text block and skip thinking blocks."""
    return "".join(block.text for block in msg.content if block.type == "text")


def calc_cost(usage) -> float:
    """Calculate the price of input and output when call. """
    cost_in = usage.input_tokens / 1_000_000 * PRICE_IN
    cost_out = usage.output_tokens / 1_000_000 * PRICE_OUT
    return cost_in + cost_out



def log_usage(msg):
    global total_cost
    cost = calc_cost(msg.usage)
    total = calc_cost + cost
    print(f"[usage] input={msg.usage.input_tokens} output={msg.usage.output_tokens} total=${total:.6f}")



def stream_chat(history: list) -> str:
    start = time.perf_counter()
    ttft = None
    with client.messages.stream(
        model=MODEL,
        max_tokens=2000,
        messages=history,
    ) as stream:
        for piece in stream.text_stream:
            if ttft is None:
                ttft = time.perf_counter() - start
            print(piece, end="", flush=True)
        final = stream.get_final_message()
    total = time.perf_counter() - start


    print()
    log_usage(final)
    print(f"[time] TTFT={ttft:.2f}s total={total:.2f}s")
    return get_text(final)
    

if __name__ == "__main__":
    history = []

    try:
        while True:
            user_input = input("Ban: ").strip()

            if user_input.lower() == "exit":
                print(f"Final price: ${total_cost:.6f}")
                break
            if user_input == "cost":
                print(f"Final cost now: ${total_cost:.6f}")
                continue
            if user_input == "reset":
                history.clear()
                print(f"Deleted history.")
                continue
            if user_input == "":
                continue

            history.append({"role": "user", "content": user_input})
            print("Claude: ", end="")
            reply = stream_chat(history)
            history.append({"role": "assistant" , "content": reply})

    except Exception as e:
        print("Loi:", type(e).__name__)
        print(e)





        