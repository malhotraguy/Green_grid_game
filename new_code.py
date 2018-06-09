import time
import pygame


# Code for Prime No.#
def is_prime(x):
    x = abs(int(x))
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for n in range(3, int(x ** 0.5) + 2, 2):
            if x % n == 0:
                return False
        return True

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE_widhth = 255
WINDOW_SIZE_height=255
screen = pygame.display.set_mode([WINDOW_SIZE_widhth,WINDOW_SIZE_height])

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 5

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WINDOW_SIZE_widhth / 2), (WINDOW_SIZE_height / 2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    my_game_loop()


def crash():
    message_display('You Lost')

def my_game_loop():
    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.
    grid = []
    for row in range(10):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(10):
            grid[row].append(0)  # Append a cell




    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    # -------- Main Program Loop -----------

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                print(row, column)
                # Set that location to one
                if is_prime(row):
                    print("Row is prime")
                    if is_prime(column):
                        grid[row][column] = 2
                        print("Row & column is prime")

                        done = True

                    else:
                        grid[row][column] = 1

                else:
                    grid[row][column] = 1
                print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(10):
            for column in range(10):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                elif grid[row][column] == 2:
                    color = RED
                    pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
                    crash()
                    #pygame.display.update()

                pygame.draw.rect(screen,
                                     color,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
my_game_loop()
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
