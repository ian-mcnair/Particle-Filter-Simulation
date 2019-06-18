# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:32:07 2019

@author: imcna
"""
import random
def choose_landmark(choice, display_width, display_height):
    if choice == 1:
        landmarks = [[int(display_width/2), int(display_height/2)]]
    elif choice == 2:
        landmarks = [[int(display_width/4), int(display_height/2)], 
                     [int(3*display_width/4), int(display_height/2)]]
    
    elif choice == 3:
        landmarks = [[int(display_width/2),int(display_height/3)],
                     [int(display_width/3), int(2*display_height/3)],
                     [int(2*display_width/3), int(2*display_height/3)]]

    elif choice == 4:
        landmarks = [[int(display_width/4),int(display_height/4)], 
                     [int(3*display_width/4),int(display_height/4)], 
                     [int(3*display_width/4),int(3*display_height/4)], 
                     [int(display_width/4),int(3*display_height/4)]]
        
    elif choice == 5:
        landmarks = [[int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)],
                     [int(random.random()*display_width), int(random.random()*display_height)]]
        
    elif choice == 6:
        landmarks = []
        for i in range(4):
            landmarks.append([int(display_width/10 + i*275), int(display_height/6)])
            landmarks.append([int(display_width/10 + i*275), int(display_height*3/6)])
            landmarks.append([int(display_width/10 + i*275), int(display_height*5/6)])
            
    return landmarks
      