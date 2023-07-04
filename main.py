import random


print("-----------WELCOME TO RPS------------")
name = input("Enter your name:")
print("Hi", name)
user_score = 0
comp_score = 0
tie = 0
print("""
---RULES OF THE GAME---
 1.Rock vs Scissor--->Rock
 2.Scissor vs Paper--->Scissor
 3.Paper vs Rock--->Paper""")
print()
while True:
    print("""Choices are:
    1.Rock
    2.Paper
    3.Scissor""")

    choice = int(input("Enter your choice between 1-3: "))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid input:"))
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissor"
    print("the user choice is:", user_choice)
    print("---Now it's Computer turn---")
    computer = random.randint(1, 3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"
    print("the computer's choice:", comp_choice)

    if (user_choice == "Rock" and comp_choice == "Paper") or (user_choice == "Paper" and comp_choice == "Rock"):
        print("Paper Wins!!!")
        result = "Paper"

    elif (user_choice == "Rock" and comp_choice == "Scissor") or (user_choice == "Scissor" and comp_choice == "Rock"):
        print("Rock Wins!!!")
        result = "Rock"
    elif (user_choice == comp_choice):
        print("it's a tie")
    else:
        print("Scissor Wins!!!")
        result = "Scissor"

    if result == "tie":
        tie += 1
    elif result == "user_choice":
        user_score += 1
    else:
        comp_score += 1
    print("Scores are:")
    print(name, "'s score is:", user_score)
    print("computer's score is:", comp_score)
    print("ties are:", tie)

    repeat = input("Do you want to play again?")
    if repeat == "No" or repeat == "No":
       break
print("Game Over!!")
print("Thanks for playing.")