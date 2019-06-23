import random as ran

running = True
def random():
    number = ran.randrange(1,6)
    return number

while running:
    user_input = input("Would you like to roll again? yes or no? ")
    try:
        if user_input.lower() == "yes":
            print(random())
        elif user_input.lower() == "no":
            running = False
        else:
            print("You have to enter yes or no! Please try again!")
    except:
        print("You have to enter yes or no! Please try again!")