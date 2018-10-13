import pygame
import Canvas, InputHandler#, Player, Enemy

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fever Fighter")
        self.clock = pygame.time.Clock()

        self.game_canvas = Canvas.Canvas(self, 800, 600)
        self.input_handler = InputHandler.InputHandler(self)
        #self.player = Player.Player()
        #self.enemy = Enemy.Enemy()

        self.entities = []
        #self.entities.append(player)
        #self.entities.append(enemy)

        self.running = True

    def update(self):
        x = 5

    def render(self):
        self.game_canvas.render()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.input_handler.handle(pygame.event.get())
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def get_entities(self):
        return self.entities

game = Game()
game.run()
