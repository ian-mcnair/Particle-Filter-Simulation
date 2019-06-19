class Settings:
    """ 
        Defines all of the static attributes of the filter
        Can be changed to see how randomness affects the performance
    """
    def __init__(self):
        self.display_width = 1000 # Should be int
        self.display_height = 800 # Should be int
        self.displacement = 10.0 # Starting Speed
        self.num_particles = 1000
        self.forward_variance = 5.
        self.turn_variance = 5.
        self.sensor_variance = 50.0
        self.refresh_rate =  20
        self.num_particles = 500
        

