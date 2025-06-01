from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_x, player_y, player_image, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

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
    display.update()
    clock.tick()