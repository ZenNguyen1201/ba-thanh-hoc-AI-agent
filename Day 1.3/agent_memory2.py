import json
from os import name

def load_memory():
    with open("data.json", "r") as f:
        memory = json.load(f)
        return memory

def save_memory(memory):
    with open("data.json", "w") as f:
        json.dump(memory, f)


memory = load_memory()

while True:
    print("\n1. Add skill")
    print("2. Change goal")
    print("3. Show your name")
    print("4. Show memory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_skill = input("Enter your new skill: ")
        memory["skills"].append(new_skill)

    if choice == "2":
        change_goal = input("Enter your change goal: ")
        memory["goal"] = change_goal

    if choice == "3":
        anwser = input("Wanna show your name? (yes/no): ")
        if anwser == "yes":
            print(memory["name"])

        else:
            print("OKK")
    
    if choice == "4":
        print(memory)

    if choice == "5":
        print("Good Bye!!")
    
save_memory(memory)