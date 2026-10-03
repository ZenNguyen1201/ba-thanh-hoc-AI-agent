point = {"Toan": 8, "Van": 7,"Anh": 9,"Ly": 6}
tong = 0
for value in point.values():
    tong = tong + value
average = tong / len(point.values())
print(average)