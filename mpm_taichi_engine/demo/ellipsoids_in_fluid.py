import taichi as ti
import numpy as np
import os
import utils
import math
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu) 

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(128, 128))

mpm.add_ellipsoid(center=[0.4, 0.3],
             radius=0.05,
             material=MPMSolver.material_elastic)
mpm.add_ellipsoid(center=[0.6, 0.3],
             radius=0.05,
             material=MPMSolver.material_elastic)

mpm.add_cube(lower_corner=[0.1, 0.6],
             cube_size=[0.7, 0.4],
             material=MPMSolver.material_water,
             velocity=[math.sin(0.1), 0])

for frame in range(200):
    mpm.step(8e-3)
    colors = np.array([0x068587, 0xED553B, 0xEEEEF0, 0xFFFF00, 0xFFFF00],
                      dtype=np.uint32)
    particles = mpm.particle_info()
    gui.circles(particles['position'],
                radius=1.5,
                color=colors[particles['material']])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif=True)