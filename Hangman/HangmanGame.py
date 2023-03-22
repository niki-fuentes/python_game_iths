#EXTRAUPPGIFT FÖR MIG SJÄLV. MIN INLÄMNING TILL LABB 1 ÄR "ROCK, PAPER, SCISSORS" !!
#EXTRAUPPGIFT FÖR MIG SJÄLV. MIN INLÄMNING TILL LABB 1 ÄR "ROCK, PAPER, SCISSORS" !!
#EXTRAUPPGIFT FÖR MIG SJÄLV. MIN INLÄMNING TILL LABB 1 ÄR "ROCK, PAPER, SCISSORS" !!


import random


options = [ "zephyr", "blizzard"]
SecretWord = random.choice(options)
blanks = ["_"] * len(SecretWord)

# Chances = len(SecretWord)
print("~Guess the word~")
print(f"{blanks}")
player_guess = input("\n Choose a letter, but choose wisley :")


while True:
    while player_guess not in SecretWord:
        player_guess = input("Wrong! Guess again: ")
    if player_guess in SecretWord:
        print("correct!")
        for i, player_guess in enumerate(SecretWord):
             if player_guess != "_" and player_guess == player_guess:
    # Set the underscore at that position to the correct letter
                SecretWord[i] = input
                player_guess = input("\n Keep guessing :")
                

#EXTRAUPPGIFT FÖR MIG SJÄLV. MIN INLÄMNING TILL LABB 1 ÄR "ROCK, PAPER, SCISSORS" !!
#EXTRAUPPGIFT FÖR MIG SJÄLV. MIN INLÄMNING TILL LABB 1 ÄR "ROCK, PAPER, SCISSORS" !!
#EXTRAUPPGIFT FÖR MIG SJÄLV. MIN INLÄMNING TILL LABB 1 ÄR "ROCK, PAPER, SCISSORS" !!
