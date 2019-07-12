# Imports
import pygame
import time

# Init
pygame.init()
pygame.font.init()

# Fenster erstellen
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")

# Font festlegen
font = pygame.font.SysFont("Comic Sans MS", 20)

# Highscore laden
filer = open("Snake/HighScore.txt", "r")
highscore = float(filer.readline())
filer.close()

# Player Stats
x = 250
y = 250
size_x = 10
size_y = 10
vel = 10
vel_x = vel
vel_y = 0
facing = "right"
snake_x = [x]
snake_y = [y]

# More Variables
clock = pygame.time.Clock()
score = 20

# Game Loop
run = True
while run:

    # Every Tick
    clock.tick(30)
    score += 0.1

    # Key Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_UP] and facing != "down":
        facing = "up"
        vel_x = 0
        vel_y = -vel

    if key[pygame.K_DOWN] and facing != "up":
        facing = "down"
        vel_x = 0
        vel_y = vel

    if key[pygame.K_RIGHT] and facing != "left":
        facing = "right"
        vel_x = vel
        vel_y = 0

    if key[pygame.K_LEFT] and facing != "right":
        facing = "left"
        vel_x = -vel
        vel_y = 0

    if x > 490 or x < 0 or y > 490 or y < 0:
        run = False

    # Slow Key
    if key[pygame.K_SPACE]:
        time.sleep(0.08)

    if key[pygame.K_ESCAPE]:
        run = False

    # Window reset
    win.fill(0)

    # Scoreboard zeichnen
    pygame.draw.rect(win, (255, 255, 255), (7, 11, 60, 49))
    score_str = str(int(score - 19))
    score_text = font.render(score_str, False, (0, 0, 0))
    highscore_text = font.render(str(int(highscore + 1)), False, (0, 0, 0))
    win.blit(score_text, (10, 10))
    win.blit(highscore_text, (10, 30))

    # Del back Snake
    if score <= len(snake_x):
        del snake_x[0]
        del snake_y[0]

    # Move Head
    x += vel_x
    y += vel_y

    # Check Snake Collide with Snake
    for i in range(len(snake_x)):
        if (x, y) == (snake_x[i], snake_y[i]):
            run = False

    # Add Head to Body
    snake_x.append(x)
    snake_y.append(y)

    # Draw Snake
    for i in range(len(snake_x)):
        pygame.draw.rect(win, (255, 0, 0), (snake_x[i], snake_y[i], size_x, size_y))

    # Update the Display
    pygame.display.update()

# Pygame close
pygame.quit()

# **Save Highscore
if score > highscore:
    filew = open("Snake/HighScore.txt", "w")
    filew.write(str(score - 20))
    filew.close()
