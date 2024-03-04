import random  # Importing the random module to generate random numbers


def roll_dice():
    """Rolls a six-sided dice and returns the result."""
    return random.randint(1, 6)  # Returns a random integer between 1 and 6


def pig_game():
    """Simulates a game of Pig."""
    player1_score = 0  # Initializing player 1's score to 0
    player2_score = 0  # Initializing player 2's score to 0
    current_player = 1  # Initializing current player to Player 1

    print("Welcome to Pig Game!")  # Displaying welcome message

    while True:  # Starting the game loop
        print(f"\nPlayer {current_player}'s turn:")  # Displaying whose turn it is
        roll = roll_dice()  # Rolling the dice
        print(f"You rolled: {roll}")  # Displaying the result of the dice roll

        if roll == 1:  # If the roll is 1
            print("You rolled a 1. Turn ends, no points earned.")  # Informing the player about rolling a 1
            # Switching to the other player
            if current_player == 1:
                current_player = 2
            else:
                current_player = 1
        else:  # If the roll is not 1
            if current_player == 1:  # If it's player 1's turn
                player1_score += roll  # Adding the roll to player 1's score
            else:  # If it's player 2's turn
                player2_score += roll  # Adding the roll to player 2's score

            print(f"Current score for Player 1: {player1_score}")  # Displaying Player 1's current score
            print(f"Current score for Player 2: {player2_score}")  # Displaying Player 2's current score

            choice = input("Do you want to roll again? (y/n): ").lower()  # Asking the player if they want to roll again
            if choice != 'y':  # If the player chooses not to roll again
                # Switching to the other player
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1

        if player1_score >= 100:  # If Player 1's score is equal to or greater than 100
            print("Player 1 wins!")  # Displaying a message indicating Player 1 wins
            break  # Ending the game loop
        elif player2_score >= 100:  # If Player 2's score is equal to or greater than 100
            print("Player 2 wins!")  # Displaying a message indicating Player 2 wins
            break  # Ending the game loop


pig_game()  # Starting the Pig game
