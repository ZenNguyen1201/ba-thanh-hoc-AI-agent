def dao_nguoc(chuoi):
    ket_qua = ""
    for c in chuoi:
        ket_qua = c + ket_qua
    return ket_qua

print(dao_nguoc("thanh"))