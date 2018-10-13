"""
enemy class
enemy.py
"""

import pygame

import random


class Enemy:
    """Creates the enemy class"""
    def __init__(self, enemy_image, width, height, x):
        self._sprite = enemy_image
        self._show_enemy = True
        self._height = height
        self._width = width
        self._x = x
        self._y = 0

    def move_position(self):
        if self._x >= 790:
            self._x -=5
        elif self._x <= 10:
            self._x +=5
_


    def is_collided_with(self, sprite):
        self._show_enemy = False

    def determine_initial_x(self):
        num = random.randint(0,1)
        if num == 1:
            return 0
        else:
            return 800





