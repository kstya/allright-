from pygame import *
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, x, y, window):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

        self.width = width

        self.height = height

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.window = window

    def draw_wall(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))
