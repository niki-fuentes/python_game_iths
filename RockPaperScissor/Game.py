import random

# KEEPING SCORE
ComputerScore=0 
UserScore=0
NumberOfRounds = 1
DrawCount = 0

# GAMEPLAY
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # ROUND COUNTER: 
    options = ["rock", "paper", "scissors"]
    print("LET PLAY ROCK, PAPER, SCISSORS!")
    print(f"Round No: {NumberOfRounds}") 
    NumberOfRounds += 1
    user_option = input("\nPick your weapon!\nType in one of the following options -> rock, paper or scissors : ")
    # INPUT HANDLING ERROR
    while user_option not in options:
        user_option = input('\n You typed something wrong!\n Try again : ')

    computer_option = random.choice(options)
    print(f"\nYou chose {user_option}, computer chose {computer_option}.\n")

    if user_option == computer_option:
        print(f"Both players selected {user_option}. It's a draw!")
        # print("------ SCORE ------")
        # print(f"Human: {UserScore} | Computer: {ComputerScore}")
        DrawCount += 1
    elif user_option == "rock":
        if computer_option == "scissors":
            UserScore += 1
            print("Rock smashes scissors! You win!")
     
        else:
            ComputerScore += 1
            print("Paper covers rock! You lose.")

    elif user_option == "paper":
        if computer_option == "rock":
            UserScore += 1
            print("Paper covers rock! You win!")

        else:
            ComputerScore += 1
            print("Scissors cuts paper! You lose.")
   
    elif user_option== "scissors":
        if computer_option == "paper":
            UserScore += 1
            print("Scissors cuts paper! You win!")

        else:
            ComputerScore += 1
            print("Rock smashes scissors! You lose.")
    # SCORES
    print("------ SCORE ------")
    print(f"Human: {UserScore} | Computer: {ComputerScore}")
    # DRAW COUNTER       
    print(f"Draws: {DrawCount}")
    
#CONTINUE OR EXIT GAME
    play_again = input("\nPlay again? (y/n): ")
    
    if play_again != "y":
        print("Goodbye!")
        break