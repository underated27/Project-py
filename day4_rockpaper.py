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
import random
game=[rock, paper, scissors]
user_choice= int(input("What do you choose, Type 0 for rock ,1 for paper,2 for scissors\n"))
if user_choice >= 3 or user_choice <0 :
    print("invalid input,computer wins")
else :
    print(game[user_choice])

    computer_choice=random.randint(0,2)
    print("computer choice:")
    print(game[computer_choice])


    if user_choice ==0 and computer_choice==2:
        print("you win!") 
    elif user_choice == 0 and computer_choice ==1:
        print("You lose")
    elif user_choice == 1 and computer_choice == 0:
        print("You win")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose") 
    elif user_choice == 2 and computer_choice== 1:
        print("You win") 
    elif user_choice == computer_choice:
        print("Draw")         