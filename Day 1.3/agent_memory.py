import json
memory = {
    "name": "Thanh",
    "age": 22,
    "goal": "learning AI agent",
    "skills": [
        "Python",
        "AI agent",
        "Machine learning"
    ]
}
with open("data.json", "w") as f:
    json.dump(memory, f)

with open("data.json", "r") as f:
    ket_qua = json.load(f)


print(ket_qua["skills"])
print(type(ket_qua))