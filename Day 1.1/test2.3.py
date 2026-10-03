def so_hoan_hao(n):
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong = tong + i
    if tong == n:
        return True
    else:
        return False
print(so_hoan_hao(25))
print(so_hoan_hao(15))