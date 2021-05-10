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

# mpm.add_ellipsoid(center=[0.5, 0.5], radius=0.1, material=MPMSolver.material_snow, color=0xEEEEF0)

mpm.add_ellipsoid(center=[0.5, 0.5], radius=0.1, material=MPMSolver.material_playdough, color=0x29A55A)

mpm.add_ellipsoid(center=[0.2, 0.2], radius=0.05, material=MPMSolver.material_rigid, color=0xFFFF00, velocity=[3, 3])

mpm.add_ellipsoid(center=[0.8, 0.2], radius=0.05, material=MPMSolver.material_elastic, color=0xED553B, velocity=[-3, 3])


# mpm.add_ellipsoid(center=[0.2, 0.8], radius=0.05, material=MPMSolver.material_playdough, color=0x29A55A, velocity=[3, -3])

mpm.add_ellipsoid(center=[0.2, 0.8], radius=0.05, material=MPMSolver.material_snow, color=0xEEEEF0, velocity=[3, -3])

mpm.add_ellipsoid(center=[0.8, 0.8], radius=0.05, material=MPMSolver.material_bread, color=0x8B4513, velocity=[-3, -3])

for frame in range(200):
    mpm.step(8e-3)
    particles = mpm.particle_info()

    gui.circles(particles['position'], radius=1.5, color=particles['color'])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)