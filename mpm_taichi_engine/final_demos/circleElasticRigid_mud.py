import taichi as ti
import numpy as np
import os
import utils
import math
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu) 

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(128, 128), gui = gui)

mpm.add_cube(lower_corner=[0.0, 0.0], cube_size=[0.4, 0.4], material=MPMSolver.material_water,  color = 0x068587, velocity=[1, 0])
mpm.add_cube(lower_corner=[0.4, 0.2], cube_size=[0.2, 0.2], material=MPMSolver.material_water,  color = 0x068587, velocity=[3, 0])

mpm.add_cube(lower_corner=[0.6, 0.0], cube_size=[0.4, 0.4], material=MPMSolver.material_honey,  color = 0xD2A307, velocity=[-1, 0])
mpm.add_cube(lower_corner=[0.4, 0.0], cube_size=[0.2, 0.2],  material=MPMSolver.material_honey,  color = 0xD2A307, velocity=[-3, 0])



for frame in range(200):
    mpm.step(8e-3)
    particles = mpm.particle_info()

    gui.circles(particles['position'], radius=1.5, color=particles['color'])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)