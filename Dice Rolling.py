import random

again = "y"

while again == "y":
    number = random.randrange(1, 7)
    print(number)

    again = input("Would you like to roll again ? (y, n): ")
    
    if again == "n":
        print("Thanks for using our service!")