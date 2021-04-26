import taichi as ti
import numpy as np
import utils
import math
from engine.mpm_solver import MPMSolver

write_to_disk = False

ti.init(arch=ti.cuda)  # Try to run on GPU

gui = ti.GUI("Taichi Elements", res=512, background_color=0x112F41)

mpm = MPMSolver(res=(128, 128))

mpm.add_cube(lower_corner=[0.1, 0.0],
             cube_size=[0.5, 0.1],
             material=MPMSolver.material_rigid,
             sample_density=25)

mpm.add_cube(lower_corner=[0.25, 0.8],
                 cube_size=[0.1, 0.1],
                 material=MPMSolver.material_elastic,
                 sample_density=25)

for frame in range(500):
    mpm.step(8e-3)
    colors = np.array([0x068587, 0xED553B, 0xEEEEF0, 0xFFFF00, 0xFFFF00],
                      dtype=np.uint32)
    particles = mpm.particle_info()
    gui.circles(particles['position'],
                radius=1.5,
                color=colors[particles['material']])
    gui.show(f'{frame:06d}.png' if write_to_disk else None)
