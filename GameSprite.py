from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, window):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)

        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.coords = (self.rect.x, self.rect.y)

        self.window = window

    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
