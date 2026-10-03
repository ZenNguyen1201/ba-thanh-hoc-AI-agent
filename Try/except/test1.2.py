

while True:
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        ket_qua = a / b
        print(ket_qua)
        break
    except ValueError:
        print("Please try again!")
    except ZeroDivisionError:
        print("Cannot divide to 0")