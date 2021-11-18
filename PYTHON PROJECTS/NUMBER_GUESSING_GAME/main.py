import random
numbers = range(1,101)
from art import logo

turns = 0

def guess_number():
  global turns
  user_guess = True
  while user_guess:
    guess = int(input("Make a guess: "))
    if guess == answer:
      print(f"You got it! The answer was {answer}")
      user_guess = False
    elif guess > answer:
      print("Too high")
      print("Guess again")
      turns -= 1
      print(f"You have {turns} attempts remaining to guess the number")
    elif guess < answer:
      print("Too low")
      print("Guess again")
      turns -= 1
      print(f"You have {turns} attempts remaining to guess the number")
    
    if turns == 0:
      print("You have run out of guess. Y O U   L O S E !")
      print(f"The answer was {answer}")
      user_guess = False
      


game_on = True
while game_on:
  print(logo)
  answer = random.choice(numbers)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 and 100")

  difficulty = input("Choose a difficulty: easy or hard\n").lower()
  if difficulty == "easy":
    turns = 10
  elif difficulty == "hard":
    turns = 5
  
  guess_number()

  repeat = input("Do you want to play again? Yes or no?\n").lower()
  if repeat == "yes":
    print("Let's go again!")
  elif repeat == "no":
    print("Thanks for playing!")
    game_on = False


