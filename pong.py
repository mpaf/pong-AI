import pygame
from pygame.locals import *
from sys import exit
import random
import math

WIDTH = 900
HEIGHT = 600

paddle_height = 30
paddle_width = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):

    image = pygame.Surface([5, 5])

    direction = random.randrange(90, 135)
    
    x = random.randrange(50, 500)
    y = random.randrange(100, 200)

    speed = 8

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image.fill(BLACK)

        self.rect = self.image.get_rect()

    def update(self):

        direction_radians = math.radians(self.direction)

        self.x += self.speed * math.sin(direction_radians)
        self.y += self.speed * math.cos(direction_radians)

        self.rect.x = self.x
        self.rect.y = self.y

        if self.y <= 0:

           self.direction = (180-self.direction)%360

        if self.y >= HEIGHT:

           self.direction = (180-self.direction)%360

        if self.x >= WIDTH:

           self.direction = (360-self.direction)%360

class Paddle(pygame.sprite.Sprite):

    image = pygame.Surface([paddle_width, paddle_height]) 

    speed = 0

    def __init__(self, starty=HEIGHT/2):

        pygame.sprite.Sprite.__init__(self)
        
        # center position of sprite
        self.pos = (paddle_width/2, starty)

        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()

    def move_up(self):

        self.speed = -5

    def move_down(self):

        self.speed = 5

    def update(self):

        self.rect.centery = self.rect.centery + self.speed

        self.rect.clamp_ip(screen.get_rect())

paddle_left = Paddle()

ball = Ball()

paddles = pygame.sprite.Group()
balls = pygame.sprite.Group()

paddles.add(paddle_left)
balls.add(ball)

gameon = True

while gameon:
	
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
	    
            gameon = False
        
        elif event.type == KEYDOWN:
        
            if event.key == K_DOWN:
            
                paddle_left.move_down()
                
            elif event.key == K_UP:
            
                paddle_left.move_up()

        elif event.type == KEYUP:

            paddle_left.speed = 0
 
    screen.fill(WHITE) 
    
    clock.tick(60)
    
    paddles.update()
    balls.update()
    paddles.draw(screen)
    balls.draw(screen)

    pygame.display.set_caption("fps: " + str(clock.get_fps()))
    	
    pygame.display.flip()

