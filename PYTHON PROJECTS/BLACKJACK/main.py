import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

user_cards = []
computer_cards = []

def get_cards():
  card1 = int(deal_card())
  card2 = int(deal_card())
  card3 = int(deal_card())
  card4 = int(deal_card())

  user_cards.append(card1)
  computer_cards.append(card2)
  user_cards.append(card3)

  print(user_cards)
  print(computer_cards)
  
  computer_cards.append(card4)

def calculate_score():
  player_turn = True
  while player_turn:
    user_total = sum(user_cards)
    pc_total = sum(computer_cards)

    if user_total == 21:
      user_total = 0
    if pc_total == 21:
      pc_total == 0
    
    if user_total > 21 and 11 in user_cards:
      return int(user_total - 10)
    if pc_total > 21 and 11 in computer_cards:
      return int(pc_total - 10)
    
    if user_total == 0 and pc_total == 0:
      print(f"Player has {user_cards} and computer has {computer_cards}")
      print("The game has ended as a DRAW!")
      player_turn = False
      game_on = False
    elif user_total == 0:
      print(f"Player has {user_cards} and computer has {computer_cards}")
      print("The game has ended, player has WON!")
      player_turn = False
      game_on = False
    elif pc_total == 0:
      print(f"Player has {user_cards} and computer has {computer_cards}")
      print("The game has ended, computer has WON!")
      player_turn = False
      game_on = False
    elif user_total > 21:
      print(f"Player has {user_cards} and computer has {computer_cards}")
      print("Player BUST! Computer WINS!")
      player_turn = False
      game_on = False
    elif user_total < 21:
      deal_again = input("Do you want another card? Yes or no").lower()
      if deal_again == "yes":
        user_cards.append(deal_card())
        print(user_cards)
      else:
        player_turn = False

def pc_play():
  pc_draw = True 
  while pc_draw:
    if sum(computer_cards) < 17:
      computer_cards.append(deal_card())
    elif sum(computer_cards) > 17:
      pc_draw = False 

def compare():

  pc_final = sum(computer_cards)
  if pc_final > 21 and 11 in computer_cards:
    pc_final = (sum(computer_cards) - 10)
  if pc_final == 21:
    pc_final = 0

  user_final = sum(user_cards)
  if user_final > 21 and 11 in user_cards:
    user_final = (sum(user_cards) - 10)
  if user_final == 21:
    user_final = 0

  if user_final == 0 and pc_final == 0:
      print(f"Player has {user_cards} and computer has {computer_cards}")
      print("The game has ended as a DRAW!")
  elif pc_final > 21:
    print(f"Player has {user_cards} and computer has {computer_cards}")
    print("The game has ended and PLAYER has WON!")
  elif user_final > pc_final:
    print(f"Player has {user_cards} and computer has {computer_cards}")
    print("The game has ended and PLAYER has WON!")
  elif user_final < pc_final:
    print(f"Player has {user_cards} and computer has {computer_cards}")
    print("The game has ended and COMPUTER has WON!")


print("Welcome to Blackjack!")
start = input("Are you ready to play? Yes or no?").lower()

if start == "yes":
  game_on = True
else:
  game_on = False
  print("Next time perhaps...")
while game_on:
  get_cards()

  calculate_score()
  pc_play()
  compare()

  another_round = input("Do you want to play again? Yes or no").lower()
  if another_round == "yes":
    game_on = True
    user_cards.clear()
    computer_cards.clear()
  else:
    game_on = False
    print("Thanks for playing!")
  


    

  
 


  