from pygame import*
from random import randint
font.init()
f1 = font.Font(None,30)
w = display.set_mode((700,500))
display.set_caption('Ping-pong')
a = transform.scale(image.load('fon.jpg'),(700,500))
mixer.init()
mixer.music.load('music.ogg')
mixer.music.set_volume(0.7)
mixer.music.play()
l = 0
o = 0
class Spr(sprite.Sprite): 
    def __init__(self,image_pic, x, y,speed=7,w=70,h=100):
        super().__init__()
        self.image = transform.scale(image.load(image_pic),(w,h))
        self.speed = speed 
        self.dir = 'right'
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ret(self):
        w.blit(self.image, (self.rect.x, self.rect.y))
class Player(Spr):
    def update_r(self):
        k = key.get_pressed()
        if k[K_UP] and self.rect.y > 5:
            self.rect.y -= 5
        if k[K_DOWN] and self.rect.y < 435:
            self.rect.y += 5
    def update_l(self):
        k = key.get_pressed()
        if k[K_w] and self.rect.y > 5:
            self.rect.y -= 5
        if k[K_s] and self.rect.y < 435:
            self.rect.y += 5
c = time.Clock()
racketka1 = Player('r1-Photoroom.png',5,410,5,60,150)
racketka2 = Player('r1-Photoroom.png',645,410,5,60,150)
mach = Spr('tennis.png',350,250,7,65,65)
f = False
b = True
while b:
    if f != True:
        w.blit(a,(0,0))
        racketka1.update_l()
        racketka1.ret()
        racketka2.update_r() 
        racketka2.ret()
        mach.ret()       
    for i in event.get():
        if i.type == QUIT:
            b = False
         
    display.update()
    c.tick(60)
