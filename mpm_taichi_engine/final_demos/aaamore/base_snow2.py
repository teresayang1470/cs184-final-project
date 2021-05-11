import taichi as ti
import numpy as np
import os
import utils
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu)

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res = (128, 128), gui = gui, unbounded=True)

mpm.add_ellipsoid(radius = .1, center = [0.1, 0.4], material=MPMSolver.material_snow, color=0xEEEEF0, sample_density=25)
mpm.add_surface_collider(point=(0.0, 0.3), normal=(0.3, 1), surface=mpm.surface_sticky)


for frame in range(200):
    mpm.step(8e-3)
    particles = mpm.particle_info()
    gui.circles(particles['position'], radius=1.5, color=particles['color'])
   
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)



