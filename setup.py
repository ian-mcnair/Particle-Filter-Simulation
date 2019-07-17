"""
    Set Up Script
"""

import cx_Freeze

executables = [cx_Freeze.Executable("ParticleFilter.py")]

cx_Freeze.setup(
    name="Particle Filter Simulation",
    options={"build_exe": {"packages":["pygame", "random","math"],
                           "include_files":["racecar.png"]}},
    executables = executables

    )