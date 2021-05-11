import taichi as ti
import numpy as np
import os
import utils
import math
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu) 

gui = ti.GUI("Taichi MLS-MPM", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(128, 128), gui = gui, unbounded=True)
mpm.add_surface_collider(point=(0.0, 0.3), normal=(0.3, 1), surface=mpm.surface_slip)

for frame in range(200):
    mpm.step(8e-3)
    if 10 < frame < 200:
        mpm.add_cube(lower_corner=[0.3, 0.7], cube_size=[0.2, 0.01], material=MPMSolver.material_water,color = 0x068587, velocity=[math.sin(frame * 0.1), 0])

    # colors = np.array([0x068587, 0xED553B, 0xEEEEF0, 0xFFFF00], dtype=np.uint32)
    # particles = mpm.particle_info()
    # pos = particles['position'] * 0.4 + 0.3
    # gui.circles(pos, radius=0.75, color=colors[particles['material']])

    particles = mpm.particle_info()
    gui.circles(particles['position'], radius=1.5, color=particles['color'])

    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)
