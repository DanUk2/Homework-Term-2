import pygame,sys
from pygame.locals import*
import random

pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
cloud_image = pygame.image.load("cloud.png").convert_alpha()
human_image = pygame.image.load("human.png").convert_alpha()
umb_image = pygame.image.load("umbrella.png").convert_alpha()


clock = pygame.time.Clock()
humanPos = 320
cloudX = -40

rainDrops = []

clouds = []

keyPressed = False





class rainDrop:

    def __init__(self):
        self.xpos = random.randint(cloudX + 30, cloudX + 275)
        self.ypos = 100
        self.scale = random.randint(1, 5)

    def draw(self):
        self.r = random.randint(1,255)
        self.g = random.randint(1,255)
        self.b = random.randint(1,255)

        pygame.draw.circle(screen,(230,240,230), (self.xpos,self.ypos), self.scale, self.scale)

    def fall(self):
        self.speed = random.randint(5, 10)
        self.ypos += self.speed
        if self.ypos > 450:
            rainDrops.remove(i)
        if self.xpos == humanPos:
            screen.blit(umb_image, (humanPos - 20, 250))
# class cloud:
#
#     def __init__(self):
#         self.xpos = -40
#         self.ypos = 0
#
#     def spawn(self):
#         screen.blit(cloud_image, (self.xpos,self.ypos))
#
#     def move(self):
#         self.speed = random.randint(3, 6)
#         self.xpos += self.speed
#         if self.xpos > 650:
#             clouds.remove(f)

# def spawn():
#
#     clouds.append(cloud())
#
#     for f in clouds:
#         f.spawn()
#         f.move()

while 1:

    clock.tick(60) #sets the FPS by calling clock tick once per frame

    pressed_key = pygame.key.get_pressed() # returns a list of booleans representing every key pressed

    screen.fill((169,169,169)) #fill screen with colour

    screen.blit(human_image, (humanPos, 320))




    cloudX += 3
    if cloudX > 600:
        cloudX = -460

    if pressed_key[K_RIGHT]:
        humanPos += 5
    if pressed_key[K_LEFT]:
        humanPos -= 5
    if humanPos > 640:
        humanPos = -40
    if humanPos < -40:
        humanPos = 640

    rainDrops.append(rainDrop())

    for i in rainDrops:
        i.draw()
        i.fall()

    screen.blit(cloud_image, (cloudX, 0))






    # if pressed_key[K_RIGHT]:
    #     xpos += 1
    # if pressed_key[K_LEFT]:
    #         xpos -= 1
    # if pressed_key[K_UP]:
    #     ypos -= 1
    # if pressed_key[K_DOWN]:
    #     ypos += 1
    # if xpos > 640:
    #     xpos = 0
    # if xpos < 0:
    #     xpos = 640
    # if ypos > 480:
    #     ypos = 0
    # if ypos < 0:
    #     ypos = 480

    for event in pygame.event.get(): #quiting game
        if event.type == pygame.QUIT:
            sys.exit()
    #This happens after all drawing commands
    pygame.display.update()
