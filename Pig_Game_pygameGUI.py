import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pig Game")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Load dice images
dice_images = [pygame.image.load(f'dice{i}.png') for i in range(1, 7)]

# Scale dice images to a fixed size of 50x50 pixels
dice_images = [pygame.transform.scale(dice, (100, 100)) for dice in dice_images]

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Function to display text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Function to draw the board
def draw_board(player1_score, player2_score, current_player, rolled_number):
    screen.fill(WHITE)

    # Draw player scores
    draw_text(f"Player 1 Score: {player1_score}", font, BLACK, screen, 300, 200)
    draw_text(f"Player 2 Score: {player2_score}", font, BLACK, screen, 600, 200)

    # Draw current player
    draw_text(f"Player {current_player}'s Turn", font, BLUE, screen, WIDTH//2, HEIGHT-200)

    # Draw dice frame
    dice_frame_rect = pygame.Rect(WIDTH//2 - 50, HEIGHT//2 - 25, 100, 100)
    pygame.draw.rect(screen, BLACK, dice_frame_rect, 2)  # Draw a black rectangle as the frame

    # Draw dice based on rolled number
    dice_index = rolled_number - 1  # Adjust for zero-based indexing
    screen.blit(dice_images[dice_index], dice_frame_rect.topleft)

    pygame.display.flip()

# Function to display winner
def draw_winner(winner):
    draw_text(f"{winner} Wins!", font, RED, screen, WIDTH//2, HEIGHT//2)
    pygame.display.flip()
    pygame.time.delay(2000)


# Main game loop
def pig_game():
    player1_score = 0
    player2_score = 0
    current_player = 1
    roll = 0  # Initialize roll variable

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                roll = roll_dice()
                if roll == 1:
                    if current_player == 1:
                        current_player = 2
                    else:
                        current_player = 1
                else:
                    if current_player == 1:
                        player1_score += roll
                    else:
                        player2_score += roll

        draw_board(player1_score, player2_score, current_player, roll)

        if player1_score >= 50:
            draw_winner("Player 1")
            running = False
        elif player2_score >= 50:
            draw_winner("Player 2")
            running = False


# Start the game
pig_game()
