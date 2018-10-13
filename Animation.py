import pygame

class Animation:
    def __init__(self, list_of_image_paths):
        self.sprites = []
        for path in list_of_image_paths:
            image = pygame.image.load("res/" + path)
            image = pygame.transform.scale(image, (60, 60))
            self.sprites.append(image)

        self.current_sprite = 0
        self.timer = 0

    def increment_timer(self):
        self.timer += 1
        if self.timer == 5:
            self.next_sprite()
            self.timer = 0

    def next_sprite(self):
        self.current_sprite = (self.current_sprite + 1) % (len(self.sprites))

    def get_current_sprite(self):
        return self.sprites[self.current_sprite]
