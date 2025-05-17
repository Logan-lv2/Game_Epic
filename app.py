import pygame
import random
import json
from enum import Enum

# Initialisation
pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption("EPIC GAME - RPG Solo")
clock = pygame.time.Clock()

# États du jeu
class GameState(Enum):
    MENU = 0
    CHARACTER_CREATION = 1
    EXPLORATION = 2
    COMBAT = 3
    INVENTORY = 4
    LEVEL_UP = 5

class RPGGame:
    def __init__(self):
        self.state = GameState.MENU
        self.player = None
        self.current_floor = 1
        self.font = pygame.font.SysFont('Arial', 24)
        
    def run(self):
        running = True
        while running:
            dt = clock.tick(60) / 1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.handle_input(event)
            
            self.update(dt)
            self.render()
            
        pygame.quit()

    def handle_input(self, event):
        # Gestion des entrées selon l'état
        pass

    def update(self, dt):
        # Logique de mise à jour
        pass

    def render(self):
        screen.fill((0, 0, 30))
        
        # Affichage selon l'état
        if self.state == GameState.MENU:
            self.render_menu()
        elif self.state == GameState.CHARACTER_CREATION:
            self.render_character_creation()
        # ... autres états
        
        pygame.display.flip()

    def render_menu(self):
        title = self.font.render("EPIC GAME - La Tour de la Désolation", True, (255, 215, 0))
        screen.blit(title, (1024//2 - title.get_width()//2, 100))
        

if __name__ == "__main__":
    game = RPGGame()
    game.run()
