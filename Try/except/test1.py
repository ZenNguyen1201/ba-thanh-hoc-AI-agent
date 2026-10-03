try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    ket_qua = a / b
    print(ket_qua)


except ZeroDivisionError:
    print("Khong the chia het cho 0")
