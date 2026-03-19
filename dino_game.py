import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

# Dino
dino_x = 80
dino_y = 300
dino_width = 40
dino_height = 40
dino_vel = 0
gravity = 1
jump = False

# Obstacle
obs_x = 800
obs_y = 310
obs_width = 30
obs_height = 30
obs_speed = 6

score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Jump
    if keys[pygame.K_SPACE] and not jump:
        dino_vel = -18
        jump = True

    dino_vel += gravity
    dino_y += dino_vel

    if dino_y >= 300:
        dino_y = 300
        jump = False

    # Obstacle movement
    obs_x -= obs_speed
    if obs_x < -30:
        obs_x = WIDTH + random.randint(100,300)
        score += 1

    # Rectangles
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    obs_rect = pygame.Rect(obs_x, obs_y, obs_width, obs_height)

    pygame.draw.rect(screen, BLACK, dino_rect)
    pygame.draw.rect(screen, BLACK, obs_rect)

    # Collision
    if dino_rect.colliderect(obs_rect):
        draw_text("GAME OVER", 320, 150)
        draw_text(f"Score: {score}", 340, 190)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    draw_text(f"Score: {score}", 20, 20)

    pygame.display.update()
    clock.tick(60)
