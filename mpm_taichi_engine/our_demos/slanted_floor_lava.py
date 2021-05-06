import taichi as ti
import numpy as np
import os
import utils
import math
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu) 

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(128, 128), unbounded=True, gui=gui)
mpm.add_surface_collider(point=(-0.5, 0.8),
                         normal=(0, 1),
                         surface=mpm.surface_slip)
mpm.add_surface_collider(point=(-0.5, 0.0),
                         normal=(0, 1),
                         surface=mpm.surface_slip)

for frame in range(300):
    mpm.step(8e-3)
    mpm.add_cube(lower_corner=[-0.5, 0.8],
                     cube_size=[0.01, 0.05],
                     velocity=[1, 0],
                     color=0xffa500,
                     material=MPMSolver.material_lava)
    mpm.add_cube(lower_corner=[-0.5, 0.0],
                     cube_size=[0.01, 0.05],
                     velocity=[1, 0],
                     color=0x068587,
                     material=MPMSolver.material_water)

    particles = mpm.particle_info()
    pos = particles['position'] * 0.4 + 0.3
    gui.circles(pos, radius=0.75, color=particles['color'])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif=True)
