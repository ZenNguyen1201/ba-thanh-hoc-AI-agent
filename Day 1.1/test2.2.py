def so_nguyen_to(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(so_nguyen_to(10))
print(so_nguyen_to(11))
print(so_nguyen_to(12))