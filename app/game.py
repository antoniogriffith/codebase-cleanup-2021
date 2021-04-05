
from random import choice

#
# USER SELECTION
#

valid_options = ["rock", "paper", "scissors"]

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_options:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(valid_options)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock" 
    if (c == "rock"):
        print("It's a tie!")
    if (c == "paper"):
        print("The computer wins")
        break
    if (c == "scissors"):
        print("The user wins")

if u == "paper"
    if (c == "rock"):
        print("The computer wins")
    if (c == "paper"):
        print("It's a tie!")
    if (c == "scissors"):
        print("The user wins")

if u == "scissors"
    if (c == "rock"):
        print("The computer wins")
    if (c == "paper":
        print("The user wins")
    if (c == "scissors"):
        print("It's a tie!")
