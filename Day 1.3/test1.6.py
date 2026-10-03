import json

du_lieu = {"ten": "Thanh", "tuoi": 22}

with open("data.json", "w") as f:
    json.dump(du_lieu, f)
with open("data.json", "r") as f:
    ket_qua = json.load(f)
    print(ket_qua)
    print(type(ket_qua))