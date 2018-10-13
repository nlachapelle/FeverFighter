import pygame

class Canvas:
    def __init__(self, game, width, height):
        self.game = game
        self.WIDTH = width
        self.HEIGHT = height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.image.load("res/" + "Background_Complete.png")
        self.background = pygame.transform.scale(self.background, (800, 600))

    def render(self):
        self.screen.blit(self.background, (0, 0))
        for entity in self.game.get_entities():
            entity.draw(self.screen)
