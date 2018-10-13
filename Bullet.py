#Bullet class

import Player

class Bullet(Player):
    def __init__(self):
        (Player.Player).__init__(self)
        self._bulletsShot = 0
        self._bulletX = self._gunX
        self._bulletY = self._gunY
        self._showBullet = False

    def moveBulletX(self, moveX):
        self._bulletX += moveX

    def shoot(self):
		if self._cartridge > 0:
			self._bulletY = self._gunY
			self._bulletX = self._gunX
			self._showBullet = True
			self._cartridge -= 1
			self._bulletsShot += 1

    def disappearBullet(self):
        self._showBullet = False

	def get_bulletsFired(self):
		return self._bulletsShot

	def reload(self):
		self._cartridge = self._maxCartridge