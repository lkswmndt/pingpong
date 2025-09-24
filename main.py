from pygame import *
from time import time as timer

win_width = 600
win_height = 500
display.set_caption('Ping Pong')
window = display.set_mode((win_width, win_height))
background = (85, 255, 255)
window.fill(background)

font.init()
font_game = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 72)
right_win = font2.render('PLAYER 1 WIN', True, (255,255,0))
left_win = font2.render('PLAYER 2 WIN', True, (255,0,0))

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

left_platform = Player('left_platform.png', 10, win_height/2,20,100,20)
right_platform = Player('right_platform.png', win_width-30, win_height/2,20,100,20)
tennis = GameSprite('tennis_ball.png',win_width/2,win_height/2,30,30,20)

finish = False
run = True
tennis_speedx = 10
tennis_speedy = 8
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(background)
        left_platform.update_left()
        right_platform.update_right()

        tennis.rect.x += tennis_speedx
        tennis.rect.y += tennis_speedy

        if sprite.collide_rect(left_platform, tennis):
            tennis_speedx *= -1
            offset = (tennis.rect.centery - left_platform.rect.centery) / (left_platform.rect.height / 2)
            tennis_speedy += int(offset * 5)

        
        if sprite.collide_rect(right_platform, tennis):
            tennis_speedx *= -1
            offset = (tennis.rect.centery - right_platform.rect.centery) / (right_platform.rect.height / 2)
            tennis_speedy += int(offset * 5)
        
        if tennis.rect.y > win_height-30 or tennis.rect.y < 0:
            tennis_speedy *= -1

        if tennis.rect.x < 0:
            finish = True
            window.blit(right_win, (100,win_height/2))

        if tennis.rect.x > win_width:
            finish = True
            window.blit(left_win, (100,win_height/2))

        tennis.reset()
        left_platform.reset()
        right_platform.reset()

    display.update()
    time.delay(50)
