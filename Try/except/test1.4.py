





while True:
    try:
        print("---TESLA ENGINEERING---")
        question = input("Are you apply AI agent? (yes/no): ")
        if question == "yes":
            correct_answer = int(input("Can you calculate area of parameter with lenght is 50 and wide is 20: "))
            if correct_answer == 1000:
                print("That's correct, Congratulation!!")
                break
            else:
                print("You Wrong, See you again")
                
        

            
            
    except ValueError:
        print("Please you have to fill the number")

    finally:
        print("---TESLA THANK YOU---")      
