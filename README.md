# ParticleFilter2DDemo

### ~~ In Progress ~~
## General Summary
The particle filter is used in many applications. The inspiration for this implementation is locating a robot in known space (or map). This project utilizes a main avatar (Cat on Roomba) as the actual location. The other smaller dots represent guesses as to where the robot thinks it actually is based on known landmarks which can be choosen inside the code. The user controls the actual robot's speed with the up and down arrows. There is not max limit, but the roomba will never go lower than zero. Direction is controlled with the left and right arrow keys. 

## Theory
In application, robots equipped with sensors are never 100% sure of where they are. Even with the most advanced cameras or sensors, a robots "idea" of its location is probabalistic. 

