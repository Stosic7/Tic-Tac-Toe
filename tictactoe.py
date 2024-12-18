import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions and constants
width = 600
height = 600
line_width = 15
board_rows = 3
board_cols = 3
circle_radius = 60
circle_width = 15
cross_width = 25
space = 55

# Colors
background_color = (28, 170, 156)
line_color = (23, 145, 135)
circle_color = (239, 231, 200)
cross_color = (66, 66, 66)
text_color = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Board representation (3x3 grid)
board = [[0] * board_cols for _ in range(board_rows)]

# Function to draw the grid
def draw_grid():
    for i in range(1, board_cols):
        pygame.draw.line(screen, line_color, (200 * i, 0), (200 * i, height), line_width)
    for i in range(1, board_rows):
        pygame.draw.line(screen, line_color, (0, 200 * i), (width, 200 * i), line_width)

# Function to draw X and O
def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 1:  # Draw circle (O)
                pygame.draw.circle(screen, circle_color, (int(col * 200 + 100), int(row * 200 + 100)), circle_radius, circle_width)
            elif board[row][col] == 2:  # Draw cross (X)
                pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + space),
                                 (col * 200 + 200 - space, row * 200 + 200 - space), cross_width)
                pygame.draw.line(screen, cross_color, (col * 200 + space, row * 200 + 200 - space),
                                 (col * 200 + 200 - space, row * 200 + space), cross_width)

# Function to mark a square
def mark_square(row, col, player):
    board[row][col] = player

# Function to check if a square is available
def available_square(row, col):
    return board[row][col] == 0

# Function to check if the board is full
def is_board_full():
    for row in board:
        for cell in row:
            if cell == 0:
                return False
    return True

# Function to check for a winner
def check_winner(player):
    # Check rows
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    # Check columns
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to display end screen
def display_end_screen(message):
    screen.fill(background_color)  # Clear the screen
    font = pygame.font.SysFont("comicsansms", 50)
    text = font.render(message, True, text_color)
    screen.blit(text, (width // 6, height // 3))
    small_font = pygame.font.SysFont("comicsansms", 30)
    retry_text = small_font.render("Press R to Restart or Q to Quit", True, text_color)
    screen.blit(retry_text, (width // 6, height // 2))
    pygame.display.update()

# Function to restart the game
def restart_game():
    global board
    board = [[0] * board_cols for _ in range(board_rows)]
    main()

# Main game function
def main():
    screen.fill(background_color)
    draw_grid()

    player = 2  # Player 2 starts (X)
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]  # X-coordinate of the click
                    mouseY = event.pos[1]  # Y-coordinate of the click

                    clicked_row = mouseY // 200
                    clicked_col = mouseX // 200

                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        if check_winner(player):  # Check if the current player wins
                            draw_figures()
                            pygame.display.update()
                            pygame.time.delay(500)  # Slight delay before clearing the grid
                            display_end_screen(f"Player {player} wins!")
                            game_over = True
                        elif is_board_full():  # Check if it's a draw
                            draw_figures()
                            pygame.display.update()
                            pygame.time.delay(500)  # Slight delay before clearing the grid
                            display_end_screen("It's a Draw!")
                            game_over = True
                        player = 3 - player  # Switch player (1 -> 2, 2 -> 1)

            if game_over:  # Handle restart or quit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Restart the game
                        restart_game()
                    if event.key == pygame.K_q:  # Quit the game
                        pygame.quit()
                        sys.exit()

        if not game_over:
            draw_figures()
        pygame.display.update()

main()
