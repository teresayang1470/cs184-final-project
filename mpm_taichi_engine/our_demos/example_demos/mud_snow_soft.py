import taichi as ti
import numpy as np
import os
import utils
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu)

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(64, 64, 64), size=10)

mpm.add_ellipsoid(center=[2, 4, 3],
                  radius=1,
                  material=MPMSolver.material_snow,
                  velocity=[0, -10, 0])
mpm.add_cube(lower_corner=[2, 6, 3],
             cube_size=[1, 1, 3],
             material=MPMSolver.material_elastic)
mpm.add_cube(lower_corner=[2, 8, 3],
             cube_size=[1, 1, 3],
             material=MPMSolver.material_sand)

mpm.set_gravity((0, -50, 0))

for frame in range(500):
    mpm.step(4e-3)
    colors = np.array([0x068587, 0xED553B, 0xEEEEF0, 0xFFFF00],
                      dtype=np.uint32)
    particles = mpm.particle_info()
    np_x = particles['position'] / 10.0

    # simple camera transform
    screen_x = ((np_x[:, 0] + np_x[:, 2]) / 2**0.5) - 0.2
    screen_y = (np_x[:, 1])

    screen_pos = np.stack([screen_x, screen_y], axis=-1)

    gui.circles(screen_pos, radius=1.5, color=colors[particles['material']])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif=True)
