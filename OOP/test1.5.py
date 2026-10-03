
class Agent:
    def __init__(self, name) :
        self.name = name
        self.skill = []


    def add_skill(self, skill):
        self.skill.append(skill)

    def show_info(self):
        print("Name:", self.name)
        print("Skills:", self.skill)



#object 1
user1 = Agent("Thanh")
user1.add_skill("Python")
user1.add_skill("Programing")

user2 = Agent("The anh")
user2.add_skill("Java")
user2.add_skill("Programing")

user1.show_info()
user2.show_info()
        