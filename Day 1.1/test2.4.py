def dem_ky_tu(chuoi, ky_tu):
    dem  = 0
    for char in chuoi:
        if char == ky_tu:
            dem = dem + 1
    return dem
print(dem_ky_tu("watermelon", "e"))