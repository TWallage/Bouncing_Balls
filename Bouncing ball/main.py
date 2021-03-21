import pygame
import sys
import random as rand
from pygame.math import Vector2

class Ball:
    def __init__(self, x, y, vel_x=1, vel_y=0, accell=(0,0.15), ball_radius=20):
        self.pos = Vector2(x,y) #position
        self.vel = Vector2(vel_x,vel_y) #velocity
        self.acc = Vector2(accell) #accelleration
        self.ball_radius = ball_radius

    def draw_ball(self):
        self.fc = pygame.Color(200,50,50) #pastel red
        self.bc = pygame.Color(30,30,30) #dark grey
        pygame.draw.circle(window, self.bc, (self.pos.x, self.pos.y), self.ball_radius) #border
        pygame.draw.circle(window, self.fc, (self.pos.x, self.pos.y), self.ball_radius-2) #face

    def update(self):
        self.vel += self.acc
        self.pos += self.vel

        self.check_border_collision()

        self.draw_ball()
    
    def check_border_collision(self):
        if self.pos.y >= height-self.ball_radius and self.vel.y > 0: #check bottom border
            self.vel.y = -self.vel.y - self.acc.y
        elif self.pos.y <= 0+self.ball_radius and self.vel.y < 0: #check top border
            self.vel.y = -self.vel.y - self.acc.y

        if self.pos.x >= width-self.ball_radius and self.vel.x > 0: #check right border
            self.vel.x = -self.vel.x - self.acc.x
        elif self.pos.x <= 0+self.ball_radius and self.vel.x < 0: #check left border
            self.vel.x = -self.vel.x - self.acc.x 

win_size = width, height = 1000, 1000
BG_COLOUR = pygame.Color(150,200,255) #light pastel blue

window = pygame.display.set_mode(win_size)
pygame.display.set_caption('Bouncing Ball')
clock = pygame.time.Clock()

balls = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print('Exiting')
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(*pygame.mouse.get_pos(), vel_x=rand.uniform(-3,3), ball_radius=rand.triangular(15,20,70)))
    window.fill(BG_COLOUR)
    for ball in balls:
        ball.update()
    pygame.display.update()
    clock.tick(120)

