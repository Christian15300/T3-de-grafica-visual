import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rombo Relleno - Rasterizado por Scanlines (Morado)")


def put_pixel(x, y, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        screen.set_at((x, y), color)


def draw_filled_rhombus(cx, cy, r, color):
    for y in range(cy - r, cy + r + 1):
        dy = abs(y - cy)       
        span = r - dy          

        x_start = cx - span
        x_end = cx + span

        for x in range(x_start, x_end + 1):
            put_pixel(x, y, color)


def main():

    background = (0, 0, 0)
    rombo_color = (128, 0, 128)   

   
    cx, cy = WIDTH // 2, HEIGHT // 2
    r = 120  

    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(background)

        draw_filled_rhombus(cx, cy, r, rombo_color)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
