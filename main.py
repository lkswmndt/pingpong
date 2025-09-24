from pygame import *
from time import time as timer

win_width = 600
win_height = 500
display.set_caption('Ping Pong')
window = display.set_mode((win_width, win_height))
background = (85, 255, 255)
window.fill(background)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed

left_platform = Player('left_platform.png', 10, win_height/2,20,80,20)
right_platform = Player('right_platform.png', win_width-30, win_height/2,20,80,20)

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        left_platform.update_left()
        right_platform.update_right()
        left_platform.reset()
        right_platform.reset()

    display.update()
    time.delay(50)
