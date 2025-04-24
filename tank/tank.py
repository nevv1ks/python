import pygame as pg

#tank_images = [pg.image.load(f'tanks/tank2{i}.png') for i in range(1, 4)]
pg.mixer.init()


class Tank(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('tank/tank2.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vector = 2
        self.reload_time = 100

    def reload(self):
        self.vector = -2.5
        self.jump_time = pg.time.get_ticks()


    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w] and self.rect.top > 0:
            self.rect.y -= self.vector
        if keys[pg.K_s] and self.rect.bottom < 700:
            self.rect.y += self.vector
