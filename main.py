from pygame import*

#display setting
window = display.set_mode((700, 500))


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

    def update_B(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
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
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
      
FPS = 60
game = True
clock  = time.Clock()
#class realase 
player1 = Player("player.png",  20, 200, 50, 200, 5)
player2 = Player("player.png", 500, 350, 50, 200, 5)

ball = GameSprite("ball.png", 150,150, 50, 50, 2)

#game while
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((255, 255, 255))
    player1.reset()
    player2.reset()
    ball.reset()

    player1.update_L()
    player2.update_R()
    ball.update_B()
    #Ifs
    if sprite.collide_rect(player1, ball):
        ball.rect.x += ball.speed
        ball.rect.y += ball.speed

    if sprite.collide_rect(player2, ball ):
        ball.rect.x -= ball.speed
        ball.rect.y -= ball.speed

    if ball.rect.x >= 500:
        ball.rect.x -= ball.speed

    if ball.rect.y >= 700:
        ball.rect.y -= ball.speed

    if ball.rect.x >= 0:
        ball.rect.x += ball.speed

    if ball.rect.y >= 0:
        ball.rect.y += ball.speed    
    
    
    display.update()
    clock.tick(FPS) 
