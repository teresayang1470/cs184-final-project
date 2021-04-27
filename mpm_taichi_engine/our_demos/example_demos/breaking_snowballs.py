import taichi as ti
import numpy as np
import os
import utils
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu)

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(128, 128))
mpm.set_gravity([0, 0])

mpm.add_ellipsoid(center=[0.25, 0.45],
                  radius=0.07,
                  velocity=[1, 0],
                  color=0xAAAAFF,
                  material=MPMSolver.material_snow)

mpm.add_ellipsoid(center=[0.55, 0.52],
                  radius=0.07,
                  velocity=[-1, 0],
                  color=0xFFAAAA,
                  material=MPMSolver.material_snow)

for frame in range(200):
    mpm.step(8e-3)
    particles = mpm.particle_info()
    gui.circles(particles['position'], radius=1.5, color=particles['color'])
    
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)
