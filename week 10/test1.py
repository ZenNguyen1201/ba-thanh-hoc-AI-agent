import os
import time
import anthropic
from dotenv import load_dotenv , find_dotenv


load_dotenv(find_dotenv())
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
MODEL = "claude-sonnet-5-5"
PRICE_IN = 2.00
PRICE_OUT = 10.00
total_cost = 0.00

def get_text(msg)-> str:
    """Join all text blocks and skip thinking blocks"""
    return "".join(block.text for block in msg.content if block.type == "text")

def calc_cost(usage) -> float:
    """Tinh chi phi (USD) moi lan goi in va out"""
    cost_in = usage.input_tokens / 1_000_0000 * PRICE_IN
    cost_out = usage.output_tokens / 1_000_000 * PRICE_OUT
    return cost_in + cost_out


def log_usage(msg):
    global total_cost
    cost = calc_cost(msg.usage)
    total_cost = total_cost + cost
    print(f"[usage] input={msg.usage.input_tokens} ouput={msg.usage.output_tokens} cost={cost: .6f}")


#GOI THUONG BANG CACH NHAN 1 LUOT TU CREATE
def basic_call(prompt: str) -> str:
    start = time.perf_counter() 
    #time.perf_counter() dai dien cho token cuoi de tru
    msg = client.messages.create(
        model=MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )


    total = time.perf_counter() - start
    #het bao lau tu luc gui toi luc nhan

    text = get_text(msg)
    print(text)
    log_usage(msg)
    # voi create thi chu dau tien va chu cuoi cung den cung luc
    #vi vay TTFT bang tong thoi gian

    print(f"[time] total={total:.2f}s")
    return text

#NHAN TUNG MANH NGAY KHI CO HIEN LEN TUNG CHU

def stream_call(prompt: str) -> str:
    start = time.perf_counter() # bam dong ho thoi diem hien tai vao start
    ttft = None #chua nhan nen ttft dang khong co gia tri
    
    with client.messages.stream(
        model=MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        for piece in stream.text_stream:
            if ttft is None:
                ttft = time.perf_counter() - start
                #thoi gian gui request den luc nhan manh dau tien

    #start ──────────────────────────────────────→ mảnh đầu tiên tới
  #│  gửi request  │  Claude đọc câu hỏi  │  Claude viết token đầu  │  gửi mảnh về máy bạn  │
  #└─── mạng ──────┴──── máy chủ xử lý ───┴─────────────────────────┴──────── mạng ────────┘
                                   # = TTFT


        print(piece, end="",flush=True)
        #end="" noi cac manh lai voi nhau thanh 1 cau
        #flash=True bat python in ra ngay lap tuc


        final = stream.get_final_messages()
        #stream xong lay lai tin nhan day du giong create
    
    total = time.perf_counter() - start
    #tong thoi gian ma claude dua ra cau tra loi ke tu khi gui request

    print()
    log_usage(final)
    print(f"f[time] TTFT={ttft:.2f}s total={total:.2f}s")
    return get_text(final)


if __name__ == "__main__":
    prompt = "Giai thich con meo cua schrödinger."

    try:
        print("--- Basic Call ---")
        basic_call(prompt)

        print("\n--- Stream Call ---")
        stream_call(prompt)

        print(f"\nTong chi phi phien nay: ${total_cost:.6f}")
    except Exception as e:
        print("Loi:", type(e).__name__)
        print(e)





