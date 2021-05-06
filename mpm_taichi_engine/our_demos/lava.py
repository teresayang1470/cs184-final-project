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

# mpm.add_ellipsoid(center=[0.4, 0.3], radius=0.05, material=MPMSolver.material_elastic, color=0xED553B)
# mpm.add_ellipsoid(center=[0.6, 0.3], radius=0.05, material=MPMSolver.material_rigid, color=0xFFFF00)

mpm.add_cube(lower_corner=[0.1, 0.1], cube_size=[0.2, 0.2], material=MPMSolver.material_lava,  color=0xFF8C00)

for frame in range(200):
    mpm.step(8e-3)
    particles = mpm.particle_info()

    gui.circles(particles['position'], radius=1.5, color=particles['color'])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)