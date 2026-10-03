import json

du_lieu = {"ten": "Thanh", "tuoi": 22}

chuoi_json = json.dumps(du_lieu)
print(chuoi_json)

print(type(chuoi_json))