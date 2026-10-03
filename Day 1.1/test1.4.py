a = 17
b = 5

result = {
    "a + b": a + b,
    "a - b": a - b,
    "a * b": a * b,
    "a / b": a / b,
    "a // b": a // b,
    "a % b": a % b,

}
for op, value in result.items():
    print(f"{op} = {value}")