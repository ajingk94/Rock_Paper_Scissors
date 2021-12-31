import os
import sys
import random
import time

#Assign ASCII arts to the variables - Rock, Paper & Scissors

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps = [rock, paper, scissors]

while True:
    os.system('cls')
    user_choice = int(input("\nWelcome to Ajin's Rock-Paper-Scissors\n\n\
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice > 2 or user_choice < 0:
        print("You chose an invalid number, you lose!!")
        break
    
    print("\nYou chose")
    print(rps[user_choice])

    computer_choice = random.randint(0,2)
    print("\nComputer chose")
    print(rps[computer_choice])

    #Result Matrix
    row1 = ["Draw", "Computer Wins!!", "You Win!!"]

    #Define a function to rotate the row1 elements to get row2 and row3
    def rotate(l,n):
        return(l[-n:] + l[:-n])

    row2 = rotate(row1,1)
    row3 = rotate(row1,2)

    result_matrix = [row1, row2, row3]
    # print(f"{row1}\n{row2}\n{row3}")
    print(f"\n{result_matrix[user_choice][computer_choice]}\n\n")

    replay = input("Do you want to play again??Reply Yes or No\n").lower()
    if replay == "yes" or replay == "y":
        print("Great!!")
        time.sleep(3)    
    else:
        print("OK! Goodbye!!")
        sys.exit()
