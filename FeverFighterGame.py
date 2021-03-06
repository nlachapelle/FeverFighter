import pygame
import Canvas, InputHandler, Player, Enemy
import Enemy
import Waves
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Fever Fighter")
        self.clock = pygame.time.Clock()

        self.game_canvas = Canvas.Canvas(self, 800, 600)
        self.input_handler = InputHandler.InputHandler(self)
        self.player = Player.Player(100, 100, 30, 30, 100, 100)
        #self.enemy = Enemy.Enemy()

        self.entities = []
        self.entities.append(self.player)
        #self.entities.append(enemy)

        self.running = True

        self.wave = Waves.Waves()

    def update(self):
        if self.wave.wave_over:
            self.wave.spawn_enemies
            self.wave.increase_wave_num

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
