import pygame
import sys
import random as rand
from pygame.math import Vector2

class Ball:
    def __init__(self, x, y, vel_x=1, vel_y=0, accell=(0,0.2), ball_radius=20):
        self.pos = Vector2(x,y) #position
        self.vel = Vector2(vel_x,vel_y) #velocity
        self.acc = Vector2(accell) #accelleration
        self.ball_radius = ball_radius
        self.fc = pygame.Color(200,50,50) #pastel red

    def draw_ball(self):
        speed_colour = self.vel.magnitude()
        speed_colour *= 13
        if speed_colour >= 359 :
            speed_colour = 359
        self.fc.hsva = (int(speed_colour),90,100,100)
        self.bc = pygame.Color(30,30,30) #dark grey
        pygame.draw.circle(window, self.bc, (self.pos.x, self.pos.y), self.ball_radius) #border
        pygame.draw.circle(window, self.fc, (self.pos.x, self.pos.y), self.ball_radius-2) #face

    def check_ball_collision(self, ball):       
        distance = (self.pos - ball.pos).magnitude_squared()
        return (distance < (self.ball_radius + ball.ball_radius)**2)

    def calculate_ball_collision(self, ball):
            vel_diff = self.vel-ball.vel
            pos_diff = self.pos - ball.pos
            try:
                self.vel -= ((vel_diff).dot(pos_diff) / (pos_diff).magnitude_squared() ) * (pos_diff)# + self.acc
                ball.vel -= ((-vel_diff).dot(-pos_diff) / (-pos_diff).magnitude_squared() ) * (-pos_diff)# + ball.acc
            except:
                pass
            self.vel *= 1
            ball.vel *= 1   
            self.pos += 0.1*pos_diff
            ball.pos -= 0.1*pos_diff

    def update(self):
        for ball in balls:
            if ball is self:
                pass
            elif self.check_ball_collision(ball):
                self.calculate_ball_collision(ball)        
        self.check_border_collision()        
        self.vel += self.acc
        self.pos += self.vel       
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
            balls.append(Ball(*pygame.mouse.get_pos(), vel_x=rand.uniform(-5,5), ball_radius=rand.triangular(10,20,50)))
    window.fill(BG_COLOUR)
    for ball in balls:
        ball.update()
    pygame.display.update()
    
    clock.tick()
    
    #print(len(balls))
    #if clock.get_fps() < 90 :
    #    print('lagging')