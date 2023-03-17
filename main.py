import pygame
import os

# Set parameters
WIDTH, HEIGHT = 800, 700
WHITE = (255, 255, 255)
BLOCK_SIZE = (30, 30)
BOARD_START_POINT = (100, 100)

# Create a window

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLOXORZ")



BLACK_BLOCK = pygame.image.load(os.path.join("Assets", "Images", "Void block.png"))
BLACK_BLOCK = pygame.transform.scale(BLACK_BLOCK, BLOCK_SIZE)

FPS = 60

def draw_stage():

def draw_window():
    WINDOW.fill(WHITE)
    WINDOW.blit(BLACK_BLOCK, BOARD_START_POINT)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()