import taichi as ti
import numpy as np
import os
import utils
import math
from engine.mpm_solver import MPMSolver

write_to_disk = False

ti.init(arch=ti.cuda)  # Try to run on GPU

gui = ti.GUI("Taichi Elements", res=512, background_color=0x112F41)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)


mpm = MPMSolver(res=(128, 128), gui=gui)

for i in range(3):
    mpm.add_cube(lower_corner=[0.2 + i * 0.1, 0.3 + i * 0.1],
                 cube_size=[0.1, 0.1],
                 material=MPMSolver.material_elastic)

for frame in range(500):
    mpm.step(8e-3)
    if frame < 500:
        mpm.add_cube(lower_corner=[0.1, 0.8],
                     cube_size=[0.01, 0.05],
                     velocity=[1, 0],
                     material=MPMSolver.material_sand)
    if 10 < frame < 100:
        mpm.add_cube(lower_corner=[0.6, 0.7],
                     cube_size=[0.2, 0.01],
                     material=MPMSolver.material_water,
                     velocity=[math.sin(frame * 0.1), 0])
    if 120 < frame < 200 and frame % 10 == 0:
        mpm.add_cube(
            lower_corner=[0.4 + frame * 0.001, 0.6 + frame // 40 * 0.02],
            cube_size=[0.2, 0.1],
            velocity=[-3, -1],
            material=MPMSolver.material_snow)
    colors = np.array([0x068587, 0xED553B, 0xEEEEF0, 0xFFFF00],
                      dtype=np.uint32)
    particles = mpm.particle_info()
    gui.circles(particles['position'],
                radius=1.5,
                color=colors[particles['material']])
    video_manager.write_frame(gui.get_image())
    gui.show(f'{frame:06d}.png' if write_to_disk else None)

video_manager.make_video(mp4 = False, gif = True)
