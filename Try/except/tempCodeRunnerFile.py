try:
    # Đoạn code có nguy cơ gây ra lỗi
    print("--- BẮT ĐẦU ---")
    s1 = input("Nhập số bị chia: ")
    s2 = input("Nhập số chia: ")
    
    # Có thể gây ra ValueError nếu người dùng nhập chữ cái
    num1 = int(s1)
    num2 = int(s2)
    
    # Có thể gây ra ZeroDivisionError (nếu num2 = 0)
    ket_qua = num1 / num2

except ValueError:
    # Xử lý khi gặp lỗi kiểu dữ liệu (nhập chữ thay vì số)
    print("-> LỖI: Bạn phải nhập vào số nguyên, không được nhập chữ!")

except Exception as e:
    # Xử lý các lỗi khác (ví dụ: lỗi chia cho 0)
    print(f"-> LỖI KHÁC: Đã xảy ra lỗi hệ thống: {e}")

else:
    # Chạy phần này NẾU KHÔNG CÓ LỖI nào xảy ra trong try
    print(f"-> THÀNH CÔNG! Kết quả phép chia là: {ket_qua}")

finally:
    # Luôn luôn chạy ở cuối cùng, dù có lỗi hay không có lỗi
    print("--- KẾT THÚC (Khối finally luôn chạy để dọn dẹp) ---\n")