# snake water gun game

''' 1 for snake -1 for water 0 for gun '''


import random


computer_choice = random.choice([1, -1, 0])
user_choice = int(input("Enter your choice: "))

print("Computer choice: ",computer_choice)
print("User choice: ",user_choice)

if computer_choice == user_choice:
    print("It's a tie!")

elif computer_choice == 1 and user_choice == -1:
    print("You lose!")
elif computer_choice == -1 and user_choice == 1:
    print("You win!")
elif computer_choice == 0 and user_choice == 1:
    print("You lose!")
elif computer_choice == 1 and user_choice == 0:
    print("You win!")
elif computer_choice == -1 and user_choice == 0:
    print("You lose!")
