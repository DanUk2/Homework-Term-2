import pygame,sys
from pygame.locals import*
import random
import time

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

umbrella = False

t = - 1 #time variable



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
#
#     def rain(self):
#         rainDrops.append(rainDrop())


# def spawn():
#
#     clouds.append(cloud())
#
#     for f in clouds:
#         f.spawn()
#         f.move()

class human:

    def __init__(self):
        self.xpos = 320
        self.ypos = 320

    def draw(self):
        screen.blit(human_image, (self.xpos, self.ypos))

    def hit_by_raindrop(self, raindrop):
        return pygame.Rect(self.xpos, self.ypos, 80, 168).collidepoint((raindrop.xpos, raindrop.ypos))

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_RIGHT]:
            self.xpos += 5
        if pressed_key[K_LEFT]:
            self.xpos -= 5
        if self.xpos > 640:
            self.xpos = -40
        if self.xpos < -40:
            self.xpos = 640

player = human()

while 1:

    clock.tick(60) #sets the FPS by calling clock tick once per frame

    pressed_key = pygame.key.get_pressed() # returns a list of booleans representing every key pressed

    screen.fill((169,169,169)) #fill screen with colour


    player.draw()
    player.move()

    cloudX += 3
    if cloudX > 600:
        cloudX = -460

    if umbrella == True:
        screen.blit(umb_image, (player.xpos - 20, 250))


    if time.time() - t < 0.3: # detect if time since the last raindrop hit is > 0.3 seconds
        umbrella = True
    else:
        umbrella = False


    rainDrops.append(rainDrop())

    i = 0
    while i < len(rainDrops):
        rainDrops[i].fall()
        rainDrops[i].draw()

        if player.hit_by_raindrop(rainDrops[i]):
            t = time.time()

        if rainDrops[i].ypos > 600 or player.hit_by_raindrop(rainDrops[i]):
            del rainDrops[i]
            i -= 1

        i += 1




    # for i in rainDrops: #use while loop instead of for loop for deleting list
    #     i.draw()
    #     i.fall()

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
