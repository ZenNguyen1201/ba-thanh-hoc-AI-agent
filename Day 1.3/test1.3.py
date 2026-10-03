f = open("test.txt", "a")
f.write("\nTrong tuong lai rat muon tro thanh AI agent\nDang trau doi kien thuc va luon co gang")
f.close()

f = open("test.txt", "r")
print(f.read())
f.close()