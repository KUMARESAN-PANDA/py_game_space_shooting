import pygame
import time
import random
from typing import List

pygame.font.init()

# Window dimensions
WIDTH = 1000
HEIGHT = 700

# Set up display
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooting")

# Load and scale background image
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))

# Player and star properties
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
FONT = pygame.font.SysFont("comicsans", 30)

# Draw the window with the player, stars, and elapsed time
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "yellow", star)

    pygame.display.update()

# Main game loop
def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)  # Correct height usage
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0
    stars: List[pygame.Rect] = []  # Correct type for pygame.Rect
    hit = False

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        # Add new stars after every increment
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, 0, STAR_WIDTH, STAR_HEIGHT)  # Set correct initial y-position
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        # Star movement and collision detection
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        if hit:
            lost_text=FONT.render("You Lost ",1,"white")
            WIN.blit(lost_text,(WIDTH/2-lost_text.get_width()/2 , HEIGHT/2-lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()

if __name__ == "__main__":
    main()
