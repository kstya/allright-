from GameSprite import GameSprite
from pygame import *
from Bullet import Bullet
class Player(GameSprite):
    # метод управления стрелками
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed

    # метод выстрел
    def fire(self, group, sound):
        group.add(Bullet('bullet.png', self.rect.x+27, self.rect.y-15, 10, (15, 15), self.window))
        sound.play()


