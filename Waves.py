"""
Waves class
Waves.py
"""
import Enemy
import random
class Waves:
    def __init__(self):
        self.wave_num = 1
        self.num_enemies = 0
        self.enemies_left = 0

    def wave_over(self):
        return self.num_enemies == 0


    def spawn_enemies(self):
        num = ((wave_num*1.5) +1)%1
        for i in range(num)
            x= random.randint(1,0)
            if x == 1:
                x=800
            Enemy.Enemy(image, width, height, x)

    def increase_wave_num(self):
        self.wave_num +=1


    def determine_initial_x(self):
        num = random.randint(0, 1)
        if num == 1:
            return 0
        else:
            return 800