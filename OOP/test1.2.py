class NguoiDung:
    def __init__(self, name, age):
       self.name = name
       self.age = age
    
    def show_info(self):
        print(f"My name is", self.name,",I'm", self.age ,"year old")
        

user = NguoiDung("Thanh", 22)
user.show_info()

   


   