import json

def load_memory():
    try:
        with open("data.json", "r") as f:
            memory = json.load(f)
            return memory
    except FileNotFoundError:
        memory_moi = {"name": "Thanh", "goal": "learning", "skills": []}
        return memory_moi

ket_qua = load_memory()   # <- GỌI hàm, và LẤY kết quả nó return về
print(ket_qua)             # <- IN kết quả đó ra màn hình để xem thử