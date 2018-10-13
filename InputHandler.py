import pygame

class InputHandler:
    def __init__(self, game):
        self.game = game

    def handle(self, pygame_events):
        for event in pygame_events:
            if event.type == pygame.QUIT:
                self.game.running = False
