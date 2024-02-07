import pygame
import sys


pygame.init()
 
# Константы/Constants
WIDTH = 288
HEIGHT = 512
FPS = 60
 
# Создание окна/Window creating
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
 
def main():
    # Спрайты/Sprites


    running = True
    while running:
        # Частота обновления экрана/Screen refresh rate
        clock.tick(FPS)
    
        # События/Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        # Рендеринг/Rendering
    
        # Обновление спрайтов/Updating sprites
    
        # Обновление экрана/Screen Refresh
        pygame.display.update()
 
if __name__ == "__main__":
    main()




