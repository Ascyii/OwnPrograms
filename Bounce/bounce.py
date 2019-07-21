import pygame

# Fenster erstellen
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Bounce")
icon = pygame.image.load("Bounce\BounceIcon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# Init Values
board_start_x = 400
board_start_y = 450
board_size_x = 200
board_size_y = 10
board_start_vel = 10

board_x = board_start_x
board_y = board_start_y
board_vel = board_start_vel

run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_RIGHT]:
        board_x += board_vel
    if key[pygame.K_LEFT]:
        board_x -= board_vel
    if key[pygame.K_ESCAPE]:
        run = False

    if board_x < 0 or board_x > 800:
        if board_x < 0:
            board_x = 0
        if board_x > 800:
            board_x = 800

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (0, 0, 0), (board_x, board_y, board_size_x, board_size_y))
    pygame.display.update()

pygame.quit()
