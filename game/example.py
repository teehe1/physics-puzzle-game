import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

trashman_png = pygame.image.load("trashman.png").convert()

trashman_png = pygame.transform.scale(trashman_png,
                                   (trashman_png.get_width() * 2,
                                    trashman_png.get_height() * 2)) 

running = True
x = 0
clock = pygame.time.Clock()

while running:
    screen.fill((255, 255, 255))

    screen.blit(trashman_png, (x, 30))

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time = clock.tick(60) / 1000.0
    delta_time = max(0.0001, min(0.1, delta_time))  # Cap delta_time to avoid large jumps
pygame.quit()