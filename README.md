# ParticleFilter2DDemo

## General Summary
The particle filter is used in many applications. The inspiration for this implementation is locating a robot in a known space (or map). This project utilizes a main avatar (Cat on Roomba) as the actual location. The other smaller dots represent guesses as to where the robot thinks it actually is based on known landmarks which can be choosen inside the code. The user controls the actual robot's speed with the up and down arrows. There is not max limit, but the roomba will never move backwards. Direction is controlled with the left and right arrow keys by rotating. 

## Theory
In application, robots equipped with sensors are never 100% sure of where they are. Even with the most advanced cameras or sensors, a robots "idea" of its location is probabalistic. Consider a robot navigating an unknown area. With the sensors provided, maps can be developed pretty reliably. At the same time, its important for a robot to be able to locate itself within a space.

Particle filters solve the latter problem of localization inside a known space. At their most basic, random positions within the space are selected and assigned a probability of how likely it is for the robot to be there based on the known map. This sampling happens over an over, with the lowest probabilities dying out over time (ideally). Eventually, most of the particles will converge on a similar area, which is the guess as to where the robot actually is. More on particle filters can be read at the below link:
http://robots.stanford.edu/papers/thrun.pf-in-robotics-uai02.pdf

## Factors to Consider in the Simulation
Randomness is added to replicate the idea of a noisy sensor. The particles are drawn under the position of the actual robot. They will most likely look a bit like static because the randomness factor added is larger to allow the user to actually see the particles. Inside the code, this randomness factor can be adjusted to see the effects of a "good" versus a "bad sensor.
Some predefined landmarks are also included and commented out. At a later time, a GUI may be made and overlayed on top in order to allow the user to choose the type of landmark they want to use.

