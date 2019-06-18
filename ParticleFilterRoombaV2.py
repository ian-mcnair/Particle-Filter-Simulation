# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:59:10 2018

@author: imcna
"""
import pygame
import math
import draw_functions as draw
from settings import Settings
from landmarks import choose_landmark
import random

# Setttings
s = Settings()


########### Landmarks ##############
choice = True
while choice:
    print("\n***************************************")
    print('Landmarks need to be created.\n Please input a numerical choice below:')
    print('1: Creates one landmark')
    print('2: Creates two landmarks')
    print('3: Creates three landmarks')
    print('4: Creates four landmarks')
    print('5: Creates random landmarks')
    print('6: Creates a grid of 12 landmarks')
    num = input('Input your choice:')
    try:
        num = int(num)
        if num < 7 and num > 0:
            landmarks = choose_landmark(num, s.display_width,s.display_height)
            choice = False
        else:
            print('Error: User input out of range of choices')
    except:
        print('Error: Count not convert user input to integer')
        

        
####################################################
########## Don't Change Anything Below! ############
####################################################

#### Pygame Init ####
pygame.init()
win = pygame.display.set_mode((s.display_width, s.display_height))
pygame.display.set_caption("Particle Filter: Cat on Roomba")
clock = pygame.time.Clock()
image = pygame.image.load('cat_roombaBig.png')

#### Used Colors ####
black = (0, 0, 0)
white = (255,255,255)
blue = (0,0,255)
     
class particle:
    def __init__(self, displacement):
        self.x = random.random() * s.display_width
        self.y = random.random() * s.display_height
        self.angle = random.random() * 2 * math.pi
        self.sense_noise   = 0.0
        self.turn_noise    = 0.0
        self.forward_noise = 0.0
    
    def placeParticle(self, new_x, new_y, new_angle):
        #Mod stops values from being place out of bounds
        self.x = new_x % s.display_width
        self.y = new_y % s.display_height
        self.angle = new_angle % (2 * math.pi)
    
    def changeNoise(self, f_noise, t_noise, s_noise):
        self.forward_noise = f_noise
        self.turn_noise = t_noise
        self.sense_noise = s_noise
    
    def sense(self):
        obs = []
        for i in range(len(landmarks)):
            distance = math.sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            distance += random.gauss(0.0, self.sense_noise)
            obs.append(distance)
        return obs
    
    def move(self, turn, displacement):        
        angle = (self.angle + turn + random.gauss(0.0, self.turn_noise)) % (2 * math.pi)
        distance = displacement + random.gauss(0.0, self.forward_noise)
        x = (self.x + (math.cos(angle) * distance)) % s.display_width
        y = (self.y + (math.sin(angle) * distance)) % s.display_height
        # Update Particle
        updated_particle = particle(s.displacement)
        updated_particle.placeParticle(x, y, angle)
        updated_particle.changeNoise(self.forward_noise, self.turn_noise, self.sense_noise)
        return updated_particle
    
    def measurement_prob(self, measurement):
        prob = 1.0
        for i in range(len(landmarks)):
            dist = math.sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.gaussian(dist, self.sense_noise, measurement[i])
        return prob
    
    def gaussian(self, mu, sigma, x):
        return math.exp(-((x - mu)/sigma)**2/2) / math.sqrt(2*math.pi*sigma**2)
#### End of Particle Class  ####

#### Defining Mean Error ####
def meanError(roomba, particles):
    sum_error = 0.0
    for p in particles:
        error_x = (p.x - roomba.x + (s.display_width/2.0)) % s.display_width - (s.display_width/2.0)
        error_y = (p.y - roomba.y + (s.display_height/2.0)) % s.display_height - (s.display_height/2.0)
        error = math.sqrt(error_x**2 + error_y**2)
        sum_error += error
    return sum_error / len(particles)

#### Set up Main Robot and Particles ####
roomba = particle(s.displacement)
turn = 0.0 

### Set Up Particles ###
def createParticles():
    particles = []
    for i in range(s.num_particles):
        add_particle = particle(s.displacement)
        add_particle.changeNoise(s.forward_variance, s.turn_variance,s.sensor_variance)
        particles.append(add_particle) 
    return particles

### Draw Initial Window ###
particles = createParticles()
draw.game_window(255, win, landmarks, s.display_width, s.display_height)
draw.particle(particles, win)
draw.avatar(image, roomba.x, roomba.y, roomba.angle, win)

pygame.display.flip()

app_status = True
count = 0
# Used literally to just allow the user to see initial setup
while app_status:
    count+=1
    if count > 5000000:
        app_status = False

app_status = True

while app_status:
    #If you want to see the actual error
    #print(meanError(roomba, particles))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            app_status = False
    
    turn = 0.0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        turn -= 2*math.pi/50
    if keys[pygame.K_RIGHT]:
        turn += 2*math.pi/50
    if keys[pygame.K_UP]:
        s.displacement += 0.5
    if keys[pygame.K_DOWN]:
        if s.displacement > 0:
            s.displacement -= 0.5
    
    roomba = roomba.move(turn, s.displacement)

    observations = roomba.sense()

    move_particle = []
    for p in particles:
        move_particle.append(p.move(turn, s.displacement))
    particles = move_particle

    weights = []
    for p in particles:
        weights.append(p.measurement_prob(observations))
    
    resampled_particles = []
    index = int(random.random() * s.num_particles)
    beta = 0.0
    max_weight = max(weights)
    for i in range(s.num_particles):
        beta += random.random() * 2.0 * max_weight
        while beta > weights[index]:
            beta -= weights[index]
            index = (index + 1) % s.num_particles
        resampled_particles.append(particles[index])
    particles = resampled_particles
    
    error = meanError(roomba, particles) 
    #if error > 300: #If the filter gets confused, its best to reset

    #Draw Windows
    draw.game_window(error, win, landmarks, s.display_width, s.display_height)
    draw.particle(particles, win)
    draw.avatar(image, roomba.x, roomba.y, roomba.angle, win)

    pygame.display.flip()
    
    clock.tick(s.refresh_rate)

pygame.quit()