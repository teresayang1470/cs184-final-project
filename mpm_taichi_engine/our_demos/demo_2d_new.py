import taichi as ti
import numpy as np
import utils
import math
from engine.mpm_solver import MPMSolver

write_to_disk = False

ti.init(arch=ti.cuda)  # Try to run on GPU

gui = ti.GUI("Taichi Elements", res=512, background_color=0x112F41)

mpm = MPMSolver(res=(128, 128), gui=gui)

for i in range(3):
    mpm.add_cube(lower_corner=[0.2 + i * 0.1, 0.3 + i * 0.1],
                 cube_size=[0.1, 0.1],
                 material=MPMSolver.material_elastic)

for frame in range(500):
    mpm.step(8e-3)
    if 10 < frame < 100:
        mpm.add_cube(lower_corner=[0.8, 0.7],
                     cube_size=[0.2, 0.01],
                     material=MPMSolver.material_water,
                     color=0x068587)
        mpm.add_cube(lower_corner=[0.2, 0.7],
                     cube_size=[0.2, 0.01],
                     material=MPMSolver.material_lava,
                     color=0xffa500)
    if 120 < frame < 200 and frame % 10 == 0:
        mpm.add_cube(
            lower_corner=[0.4 + frame * 0.001, 0.6 + frame // 40 * 0.02],
            cube_size=[0.2, 0.1],
            velocity=[-3, -1],
            material=MPMSolver.material_snow)
    particles = mpm.particle_info()
    gui.circles(particles['position'],
                radius=1.5,
                color=particles['color'])
    gui.show(f'{frame:06d}.png' if write_to_disk else None)
