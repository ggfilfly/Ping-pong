from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_image, speed, height, width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y < 620:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        
        if keys[K_s] and self.rect.y < 620:
            self.rect.y += self.speed

ball = GameSprite(275, 225, "ball.png", 10, 50, 50)
racket1 = Player(520, 200, "платформа.png",10, 150, 50)
racket2 = Player(30, 200, "платформа.png",10,  150, 50)

win_width = 600
win_height = 500
back = (56, 125, 119)
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
window.fill(back)
clock = time.Clock()
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if not finish:
            window.fill(back)
            ball.draw()
            racket1.draw()
            racket2.draw()
            racket1.update()
            racket2.update2()
    display.update()
    clock.tick(60)
