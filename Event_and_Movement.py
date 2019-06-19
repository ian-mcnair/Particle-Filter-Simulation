import pygame
import math
import random

def button_event(keys, turn, displacement):
    """Takes in button down events, returns translation/rotation"""
    if keys[pygame.K_LEFT]:
        turn -= 2*math.pi/50
    if keys[pygame.K_RIGHT]:
        turn += 2*math.pi/50
    if keys[pygame.K_UP]:
        displacement += 0.5
    if keys[pygame.K_DOWN]:
        if displacement > 0:
            displacement -= 0.5
    return displacement, turn

def move_particle(particles, turn, displacement, display_width, display_height):
    """ Moves the particles based on how the avatar moves """
    new_particles = []
    for p in particles:
        new_particles.append(p.move(turn, displacement,  display_width, display_height))
    return new_particles

def get_weights(particles, observations, landmarks):
    """ Weights particles based on how their measurements compare to avatars"""
    weights = []
    for p in particles:
        weights.append(p.measurement_prob(observations, landmarks))
    return weights

def resample_particles(particles, weights, num_particles):
    """ 
        Uses weights to recreate particles
        Best particles have a better chance at surviving
    """
    resampled_particles = []
    index = int(random.random() * num_particles)
    beta = 0.0
    max_weight = max(weights)
    for i in range(num_particles):
        beta += random.random() * 2.0 * max_weight
        while beta > weights[index]:
            beta -= weights[index]
            index = (index + 1) % num_particles
        resampled_particles.append(particles[index])
    return resampled_particles