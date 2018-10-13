import pygame

class Canvas:
    def __init__(self, game, width, height):
        self.game = game
        self.WIDTH = width
        self.HEIGHT = height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def render(self):
        for entity in self.game.get_entities():
            entity.draw(self)
