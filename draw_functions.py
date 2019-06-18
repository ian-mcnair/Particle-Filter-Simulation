# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:05:58 2019

@author: imcna
"""

import pygame
import math

def game_window(error, win, landmarks, display_width, display_height):
    black = (0, 0, 0)
    if error > 254:
        error = 255
    color = (int(error), 255-error, 50)
    win.fill(color)
    pygame.draw.line(win, black, (display_width/4, display_height/4), (3 * display_width/4, 3*display_height/4), 1)
    pygame.draw.line(win, black, (3 * display_width/4, display_height/4), (display_width/4, 3* display_height/4), 1)
    for i in range(len(landmarks)):
        pygame.draw.circle(win, black, landmarks[i] , 20)
        
def avatar(image, x, y, angle, win):
    #print('X = ' , x , '   Y = ', y, '   Direction = ', direction)
    rotated = pygame.transform.rotate(image, -angle*(180/math.pi))
    actual_pos = (x - rotated.get_rect().width/2, 
                  y - rotated.get_rect().height/2)
    win.blit(rotated, actual_pos)
    
def particle(particles, win):
    blue = (0,0,255)
    for p in particles:
        pos = (int(p.x), int(p.y))
        pygame.draw.circle(win, blue, pos , 5)    