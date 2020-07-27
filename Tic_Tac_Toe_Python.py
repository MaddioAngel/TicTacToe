import pygame
pygame.init()
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Set the width and height of the screen [width, height]
width = 700
height = 500
gap = 50

size = (width, height)

first_line_up_w = int(width*(1/3))
first_line_up_h = gap

second_line_up_w = int(width*(2/3))
second_line_up_h = gap

first_line_side_w = gap
first_line_side_h = int(height*(1/3))

second_line_side_w = gap
second_line_side_h = int(height*(2/3))

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

guess = [
            ["","",""],
            ["","",""],
            ["","",""]
]

font = pygame.font.SysFont("comicsansms", 50)
X_WINS = 0
O_WINS = 0

def game():
    # Loop until the user clicks the close button.
    print(X_WINS)
    done = False
    turn = 0
    while not done:
        board()
        game = True
        while(game):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()     
                    if (turn == 0):
                        if (check_board(x,y, turn)):
                            draw_circle(x,y)
                            turn = 1    
                        else:
                            print("Can't play there")
                            print(guess)
                    else:
                        if(check_board(x,y, turn)):
                            draw_cross(x,y)
                            turn = 0
                        else:
                            print("Can't play there")
                            print(guess)
                    if(check_win(guess)):
                        clear_game()
                                           
    # Close the window and quit.
    pygame.quit()

def board():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [first_line_up_w, first_line_up_h], [first_line_up_w, height - first_line_up_h], 5)
    pygame.draw.line(screen, BLACK, [second_line_up_w, second_line_up_h], [second_line_up_w, height - second_line_up_h], 5)

    pygame.draw.line(screen, BLACK, [first_line_side_w, first_line_side_h], [width - first_line_side_w, first_line_side_h], 5)
    pygame.draw.line(screen, BLACK, [second_line_side_w, second_line_side_h], [width - second_line_side_w, second_line_side_h], 5)

    x_wins = font.render("X: "+ str(X_WINS), 1, (0,0,0))
    o_wins = font.render("O: "+ str(O_WINS), 1, (0,0,0))
    screen.blit(x_wins, (0, 0))
    screen.blit(o_wins, (100, 0))
    
    pygame.display.flip()

def check_board(x,y, turn):
    i = 0
    j = 0

    if (x < first_line_up_w):
        i = 0

    elif (x < second_line_up_w):
        i = 1
    else:
        i = 2

    if (y < first_line_side_h):
        j = 0
    elif (y < second_line_side_h):
        j = 1
    else:
        j = 2

    if ((guess[j][i] == "X") or (guess[j][i] == "O") ):
        return False
    else: 
        if (turn == 0):
            guess[j][i] = "O"
            return True
        elif (turn == 1):
            guess[j][i] = "X"
            return True
    
def draw_circle(x,y):
    if (x < first_line_up_w):
        i = 0
    elif (x < second_line_up_w):
        i = 1
    else:
        i = 2
    if (y < first_line_side_h):
        j = 0
    elif (y < second_line_side_h):
        j = 1
    else:
        j = 2

    center_x = int(first_line_up_w * (i + 0.5))
    center_y = int(first_line_side_h * (j + 0.5))
    pygame.draw.circle(screen, RED, (center_x, center_y), 50, 7)
    pygame.display.flip()

def draw_cross(x,y):
    length_of_cross = 75

    if (x < first_line_up_w):
        i = 0
    elif (x < second_line_up_w):
        i = 1
    else:
        i = 2

    if (y < first_line_side_h):
        j = 0
    elif (y < second_line_side_h):
        j = 1
    else:
        j = 2

    x = int((first_line_up_w * (i + 0.5)) - (length_of_cross/2))
    y = int(first_line_side_h * (j + 0.5) - (length_of_cross/2))
    start = [x,y]
    stop = [x + length_of_cross, y + length_of_cross]
    start2 = [x + length_of_cross, y]
    stop2 = [x, y + length_of_cross]
    pygame.draw.line(screen, BLUE, start, stop, 10)
    pygame.draw.line(screen, BLUE, start2, stop2, 10)    
    pygame.display.flip()

def cat_scam():
    empty = 0
    for i in range(3):
        for j in range(3):
            if (guess[i][j] == ""):
                empty = empty + 1
    if (empty == 0):
        return True

def check_win(guess):
    global O_WINS
    global X_WINS
    if(check_O()):
        print("Win for O")
        print(check_O())
        O_WINS = O_WINS + 1
        return True
    if(check_X()):
        print("Win for X")
        X_WINS = X_WINS + 1
        return True
    if(cat_scam()):
        print("Game Over")
        print("No one wins")
        clear_game()
    else:
        return False

def check_X():
    #Across
    if((guess[0][0] == "X") and (guess[0][1] == "X") and (guess[0][2] == "X")): return True
    if((guess[1][0] == "X") and (guess[1][1] == "X") and (guess[1][2] == "X")): return True
    if((guess[2][0]  == "X") and (guess[2][1] == "X")  and (guess[2][2] == "X")): return True
    
    #Diagonal
    if(guess[0][0] == "X" and guess[1][1] == "X" and guess[2][2] == "X"): 
        return True
    if(guess[0][2] == "X" and guess[1][1] == "X" and guess[2][0] == "X"): 
        return True
    
    #Vertical
    if((guess[0][0] == "X") and (guess[1][0] == "X") and (guess[2][0] == "X")): return True
    if((guess[0][1] == "X") and (guess[1][1] == "X") and (guess[2][1] == "X")): return True
    if((guess[0][2] == "X") and (guess[1][2] == "X") and (guess[2][2] == "X")): return True
    else:
        return False

def check_O():
    #Across
    if(guess[0][0] == "O" and guess[0][1] == "O" and guess[0][2] == "O"): 
        print("#Across")
        return True
    if(guess[1][0] == "O" and guess[1][1] == "O" and guess[1][2] == "O"): 
        print("#Across")
        return True
    if(guess[2][0] == "O" and guess[2][1] == "O"and guess[2][2] == "O"): 
        print("#Across")
        return True
    
    #Diagonal
    if(guess[0][0] == "O" and guess[1][1] == "O" and guess[2][2] == "O"): 
        print("#Diagonal")
        return True
    if(guess[0][2] == "O" and guess[1][1] == "O" and guess[2][0] == "O"): 
        print("#Diagonal")
        return True

    #Vertical
    if(guess[0][0] == "O" and guess[1][0] == "O" and guess[2][0] == "O"): 
        print("#Vertical")
        return True
    if(guess[0][1]  == "O" and guess[1][1]  == "O" and guess[2][1] == "O"): 
        print("#Vertical")
        return True
    if(guess[0][2] == "O" and guess[1][2] == "O" and guess[2][2] == "O"): 
        print("#Vertical")
        return True
    else:
        return False


def clear_game():
    print(guess[0])
    print(guess[1])
    print(guess[2])

    print(" ")
    board()
    turn = 0
    for i in range(3):
        for j in range(3):
            guess[j][i] = ""


game()