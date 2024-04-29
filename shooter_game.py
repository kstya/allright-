from random import randint

import pygame.time
from pygame import *
from Player import Player
from Enemy import Enemy, return_lost
from Bullet import Bullet

# создай окно игры
window = display.set_mode((700, 500))

display.set_caption("Космос")
x, y = 285, 390



background = transform.scale(image.load("galaxy.jpg"), (700, 500))

# задай фон сцены, (700, 500))
mixer.init()
mixer.music.load('gimn-rossii-gimn-rossii-so-slovam2.mp3')
mixer.music.play()
fire = mixer.Sound('gimn-rossii-gimn-rossii-so-slovam2.mp3')
font.init()
font1 = font.SysFont('Arial', 40)
font2 = font.SysFont('Arial', 40)
win = font.SysFont('Arial', 40)
lose = font.SysFont('Arial', 40)






ufos = []
monsters = sprite.Group()
for i in range(5):
    ufos.append(Enemy('ufo.png', randint(0+20, 700-85), 0, randint(1, 2), (50, 50), window))
for i in range(5):
    monsters.add(ufos[i])
bullets = sprite.Group()

asteroids = []
asteroid = sprite.Group()
for i in range(3):
    asteroids.append(Enemy('asteroid.png', randint(0+20, 700-85), 0, randint(1, 2), (50, 50), window))
for i in range(3):
    asteroid.add(asteroids[i])



rocket = Player('rocket.png', x, y, 4, (60, 60), window)


score = 0
FPS = 60
clock = time.Clock()
fire_rate = 250
last_shot = pygame.time.get_ticks()
game = True
finish = False
while game:
    # Установка ФПС
    clock.tick(FPS)
    text_lose = font1.render('Пропущено:' + str(return_lost()), 1, (255, 255, 255))
    text_kill = font2.render('Повержено:' + str(score), 1, (255, 255, 255))

    for e in event.get():
        # обработай событие «клик по кнопке "Закрыть окно"»
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        window.blit(text_lose, (0, 0))
        window.blit(text_kill, (0, 40))
        rocket.update()
        monsters.update()
        monsters.draw(window)
        bullets.draw(window)
        bullets.update()
        asteroid.update()
        asteroid.draw(window)
        rocket.reset()
        keys = key.get_pressed()
        current_time = pygame.time.get_ticks()
        if keys[K_SPACE]:
            if current_time - last_shot >= fire_rate:
                rocket.fire(bullets, fire)
                last_shot = current_time
        sprite_list = sprite.groupcollide(bullets, monsters, True, True)
        for bullet in sprite_list:
            score += len(sprite_list[bullet])
            monsters.add(Enemy('ufo.png', randint(0, 700), 0,
                               randint(1, 2), (65, 65), window))

        sprite_list1 = sprite.groupcollide(bullets, asteroid, True, True)
        for bullet in sprite_list1:
            score += len(sprite_list1[bullet])
            asteroid.add(Enemy('asteroid.png', randint(0, 700), 0,
                               randint(1, 2), (65, 65), window))

        if score >= 10:
            finish = True
            win_game = font1.render("YOU WIN", 1, (255, 255, 255))
            window.blit(win_game, (250, 200))
        elif return_lost() >= 3 or sprite.spritecollide(rocket, monsters, False):
            finish = True
            lose_game = font1.render("YOU LOSE", 1, (255, 255, 255))
            window.blit(lose_game, (250, 200))
    display.update()
