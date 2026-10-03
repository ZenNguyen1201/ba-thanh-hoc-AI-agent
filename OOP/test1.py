class NguoiDung:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def show_info(self):
        print("Name:", self.name)
        print("Socre:", self.score)
    
student1 = NguoiDung("Thanh", 10)
student1.show_info()