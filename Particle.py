import random
import math

class Particle:
    """
    This class initializes the particle of the particle filter
    It 
    """
    def __init__(self, displacement, display_width, display_height):
        self.x = random.random() * display_width
        self.y = random.random() * display_height
        self.angle = random.random() * 2 * math.pi
        self.sense_noise   = 0.0
        self.turn_noise    = 0.0
        self.forward_noise = 0.0

    
    def place_particle(self, new_x, new_y, new_angle, display_width, display_height):
        """Mod stops values from being place out of bounds"""
        self.x = new_x % display_width
        self.y = new_y % display_height
        self.angle = new_angle % (2 * math.pi)
    
    def change_noise(self, f_noise, t_noise, s_noise):
        """Changes the noise of each particle"""
        self.forward_noise = f_noise
        self.turn_noise = t_noise
        self.sense_noise = s_noise
    
    def sense(self, landmarks):
        """Guesses at how far a landmark is based on sensor noise"""
        obs = []
        for i in range(len(landmarks)):
            distance = math.sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            distance += random.gauss(0.0, self.sense_noise)
            obs.append(distance)
        return obs
    
    def move(self, turn, displacement, display_width, display_height):
        """Moves and Turns the particles based on how the avatar moves"""
        angle = (self.angle + turn + random.gauss(0.0, self.turn_noise)) % (2 * math.pi)
        distance = displacement + random.gauss(0.0, self.forward_noise)
        x = (self.x + (math.cos(angle) * distance)) % display_width
        y = (self.y + (math.sin(angle) * distance)) % display_height
        # Update Particle
        updated_particle = Particle(displacement, display_width, display_height)
        updated_particle.place_particle(x, y, angle, display_width, display_height)
        updated_particle.change_noise(self.forward_noise, self.turn_noise, self.sense_noise)
        return updated_particle
    
    def measurement_prob(self, measurement, landmarks):
        """Calculates the gaussian of the measurements """
        prob = 1.0
        for i in range(len(landmarks)):
            dist = math.sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.gaussian(dist, self.sense_noise, measurement[i])
        return prob
    
    def gaussian(self, mu, sigma, x):
        """Actually calculates the gaussian"""
        return math.exp(-((x - mu)/sigma)**2/2) / math.sqrt(2*math.pi*sigma**2)
    
def mean_error(roomba, particles, display_width, display_height):
    """Calcualtes the mean error"""
    sum_error = 0.0
    for p in particles:
        error_x = (p.x - roomba.x + (display_width/2.0)) % display_width - (display_width/2.0)
        error_y = (p.y - roomba.y + (display_height/2.0)) % display_height - (display_height/2.0)
        error = math.sqrt(error_x**2 + error_y**2)
        sum_error += error
    return sum_error / len(particles)

def create_particles(num_particles, 
                    displacement, 
                    forward_variance, 
                    turn_variance, 
                    sensor_variance, 
                    display_width, 
                    display_height):
    """ Creates all the particles for the filter"""
    particles = []
    for i in range(num_particles):
        add_particle = Particle(displacement, display_width, display_height)
        add_particle.change_noise(forward_variance, turn_variance, sensor_variance)
        particles.append(add_particle) 
    return particles
    
