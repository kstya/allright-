from GameSprite import GameSprite
from random import randint
lost = 0

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 700:
            self.rect.x = randint(0+20, 700-85)
            self.rect.y = 0
            lost += 1
def return_lost():
    global lost
    return lost