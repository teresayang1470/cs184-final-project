import taichi as ti
import numpy as np
import os
import utils
import random
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu)

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res = (128, 128), gui = gui)


mpm.add_cube(lower_corner=[0, 0], cube_size = [1, .3], material = MPMSolver.material_lava, color = 0xEA5C10, velocity=[0, -1])


c = (0.5, 0.5)
r = 30

mpm.add_sphere_collider(center = c, radius = r, surface=mpm.surface_separate)

for frame in range(210):
    mpm.step(8e-3)

    if frame < 100 and frame % 10 == 0: 
        mpm.add_cube(lower_corner=[0.49, 0.8], cube_size = [0.025, 0.2], material = MPMSolver.material_lava, color = 0xEA5C10, velocity=[0, .01])


    particles = mpm.particle_info()
    gui.circles(particles['position'], radius=1.5, color=particles['color'])
    gui.circle(c, radius=r, color=0x7C0E8F)
   
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)
