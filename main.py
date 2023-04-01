from pygame import*

#display setting
window = display.set_mode((700, 500))
window.fill((255, 255, 0))

#class
class GameSprite(sprite.Sprite):
    def __init__(self,image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_L(self):
        keys = key.get_pressed()

        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed

    def update_R(self):
        keys = key.get_pressed()

        if keys[K_UP]:
            self.rect.y += self.speed
        if keys[K_DOWN]:
            self.rect.y -= self.speed
      
FPS = 60
game = True
clock  = time.Clock()
#class realase 
player1 = Player("player.png",  20, 200, 50, 200, 5)
player2 = Player("player.png", 500, 350, 50, 200, 5)

ball = GameSprite("ball.png", 200,200, 50, 50, 2)

#game while
while game:
    for event in event.get():
        if event.type == QUIT:
            game = False

    player1.reset()
    player2.reset()

    player1.update_L()
    player2.update_R()

    display.update()
    clock.tick(FPS) 