import random
from game_data import data
from art import logo
from art import vs

def choose_winner():
    global account1
    winner = ''
    streak = 0
    game_on = True
    while game_on:
        account2 = random.choice(data)

        if account1['follower_count'] > account2['follower_count']:
            winner = 'A'.lower()
        else:
            winner = 'B'.lower()

        print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}")

        print(vs)

        print(f"Against B: {account2['name']}, a {account2['description']}, from {account2['country']}")

        answer = input("Who has more followers? 'A' or 'B'?").lower()

        if answer == 'a' and winner == 'a':
            streak += 1
            print(f"You're right! Current score: {streak}")
        elif answer == 'b' and winner == 'b':
            streak +=1
            print(f"You're right! Current score: {streak}")
            account1 = account2
        else:
            print(f"Sorry, that's wrong. Final score: {streak}")
            game_on = False

print(logo)

account1 = random.choice(data)

choose_winner()



