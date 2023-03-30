import pygame

pygame.init()

#display setting
window = pygame.display.set_mode((700, 500))

#class
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, w, h, speed):

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.x -= speed
                if event.key == pygame.K_w:
                    self.y -= speed
                if event.key == pygame.K_d:
                    self.x += speed
                if event.key == pygame.K_s:
                    self.y += speed

FPS = 60
game = True
clock  = pygame.time.Clock()

player1 = Sprite()


#game while
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player1.move()

    pygame.display.update()
    clock.tick(FPS) 