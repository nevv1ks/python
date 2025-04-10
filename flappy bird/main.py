import random
import pygame as pg
from bird import Bird
from pipe import Pipe

pg.init()
pg.font.init()

font = pg.font.SysFont('None', 100)

WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
color = (255, 255, 255)

bird = Bird(50, HEIGHT // 2)

all_sprite = pg.sprite.Group(bird)
pipes = pg.sprite.Group()

run = True

clock = pg.time.Clock()
pg.time.set_timer(pg.USEREVENT, 2000)
pg.time.set_timer(pg.USEREVENT + 1, 2000)

score = 0

pipe_scored = False

back_ground_img = pg.image.load('flappy bird.png')
back_ground = pg.surface.Surface((back_ground_img.get_width(), 600))
back_ground_x = 0
back_ground_x2 = back_ground_img.get_width()

while run:

    screen.fill('white')
    clock.tick(60)

    back_ground.blit(back_ground_img, (0, 1))
    screen.blit(back_ground, (back_ground_x, 0))
    screen.blit(back_ground, (back_ground_x2, 0))

    back_ground_x -= 1
    back_ground_x2 -= 1

    if back_ground_x < - back_ground_img.get_width():
        back_ground_x = back_ground_img.get_width()
    if back_ground_x2 < - back_ground_img.get_width():
        back_ground_x2 = back_ground_img.get_width()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            bird.jump()
        if event.type == pg.USEREVENT:
            rand_hight = 150 + random.randint(0, 50)
            pipe_up = Pipe(WIDTH, 0, 50, rand_hight, "green")
            pipe_down = Pipe(WIDTH, rand_hight + random.randint(100, 200), 50, 1000, "green")
            all_sprite.add(pipe_up, pipe_down)
            pipes.add(pipe_up, pipe_down)
        if event.type == pg.USEREVENT + 1:
            score += 1

    if pg.sprite.spritecollide(bird, pipes, False):
        run = False

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()

pg.quit()
