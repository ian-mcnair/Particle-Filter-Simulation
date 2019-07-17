"""
    Set Up Script
"""

import cx_Freeze

executables = [cx_Freeze.Executable("ParticleFilter.py")]

cx_Freeze.setup(
    name="Particle Filter Simulation",
    options={"build_exe": {"packages":["pygame", 
                                       "random", 
                                       "math"],
                           "include_files":["cat_roomba2.png",
                                            "draw_functions.py",
                                            "Event_and_Movement.py",
                                            "landmarks.py",
                                            "Particle.py",
                                            "settings.py"]}},
    executables = executables
    )