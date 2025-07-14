# #ask:Roll a die?(y/n)

# #if user enters y
#     generate two random no.
# if user enters n
#     print(thank you for playing)
#     terminate game
# if user enters anything else
#     print invalid

import random
#user entered the game
print("Welcome to the game")

while True:
#asking user he has to play?
    choice=input("enter to play (y/n): ").lower()
#user said yes
    if choice=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"{die1},{die2}")

#user denied to play
    elif choice=='n':
        print("Thank you for playing!")
        break

#user mistakingly typed anything else
    else:
        print("oopss,Invalid!")






