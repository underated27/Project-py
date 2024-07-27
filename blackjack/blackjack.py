import random
from art import logo
print(logo)
def deal_card():
    
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    randomcard=random.choice(cards)
    return randomcard
    
def calculate_score(cards):
    
    if sum(cards)== 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
    return sum(cards) 

def compare(user_score, computer_score):
    
    if computer_score == user_score:
        return "Draw"
    elif computer_score==0:
        return "You lose,opponent has black jack"
    elif user_score==0:
        return "You win"
    elif user_score>21:
        return "You went over,You lose"
    elif computer_score>21:
        return "Opponent went over ,You win"
    elif user_score>computer_score:
        return "You win"
    else:
        return "You lose"

user_cards=[]
computer_cards=[]
    
gameover=False

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
while not gameover:

    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"The user cards are: {user_cards} and score is {user_score}")
    print(f"The computer first card is {computer_cards[0]} ")
    if user_score==0 or computer_score== 0 or user_score>21:
        gameover=True
        
    else:
        anothercard=input("Do you want to get another card press 'y' for yes and 'n' for no\n")
        if anothercard=="y":
            user_cards.append(deal_card())
        else:
            gameover=True
       
#for computer to play on its own 
while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)

print (f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score,computer_score))