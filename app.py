# Import Statements
import pygame
import draw_functions as draw
from settings import Settings
import landmarks as l
from Particle import Particle
from Particle import mean_error
from Particle import create_particles
from Event_and_Movement import button_event
from Event_and_Movement import move_particle
from Event_and_Movement import get_weights
from Event_and_Movement import resample_particles

def main():
    ## Import Settings
    s = Settings()
    # Import Landmarks
    landmarks = l.choose_landmark_loop(s.display_width, s.display_height)
    
    # Initiate Pygame Attrributes
    win = pygame.display.set_mode((s.display_width, s.display_height))
    pygame.display.set_caption("Particle Filter: Cat on Roomba")
    clock = pygame.time.Clock()
    image = pygame.image.load('resources/cat_roomba2.png')
    
    # Set up main Avatar - Cat on Roomba
    roomba = Particle(s.displacement, s.display_width, s.display_height)
    
    
    # Creates Particles for the particle filter
    particles = create_particles(s.num_particles, 
                                 s.displacement, 
                                 s.forward_variance, 
                                 s.turn_variance, 
                                 s.sensor_variance,
                                 s.display_width,
                                 s.display_height)
    
    # Draw initial game window, particles, and avatar
    draw.game_window(255, win, landmarks, s.display_width, s.display_height)
    draw.particle(particles, win)
    draw.avatar(image, roomba.x, roomba.y, roomba.angle, win)
    pygame.display.flip()
    
    app_status = True
    while app_status:
        """This is the main loop that runs the entire application"""
        
        # This controls quitting the application
        # For some reason it doesn't like getting put into
        # another definition
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app_status = False
        
        # Controls the speed and direction of avatar
        turn = 0.0
        keys = pygame.key.get_pressed()
        s.displacement, turn = button_event(keys, turn, s.displacement)
        roomba = roomba.move(turn, s.displacement, 
                             s.display_width, s.display_height)
    
        # Gets distances of landmarks from avatar
        observations = roomba.sense(landmarks)
    
        # Changes position of particles the same way the avatar moves
        particles = move_particle(particles, 
                                  turn, 
                                  s.displacement,  
                                  s.display_width, 
                                  s.display_height)
        
        # Gets the weight of each particle 
        # Essentially a measure of how close to ideal it is
        weights = get_weights(particles, observations, landmarks)
        
        # Creates new generation of particles based on old one
        # Best ones have higher probability of surviving
        particles = resample_particles(particles, weights, s.num_particles)
        
        # Calculate Error
        error = mean_error(roomba, particles, s.display_width, s.display_height)
    
        #Draws updated Windows/Particles/Avatar
        draw.game_window(error, win, landmarks, s.display_width, s.display_height)
        draw.particle(particles, win)
        draw.avatar(image, roomba.x, roomba.y, roomba.angle, win)
        pygame.display.flip()
        
        # Reduces the speed of the loop so it doesn't use to much CPu
        clock.tick(s.refresh_rate)
    
# Quits game once app_status = False
if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()