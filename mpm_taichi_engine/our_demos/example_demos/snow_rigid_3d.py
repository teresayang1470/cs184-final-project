import taichi as ti
import numpy as np
import os
import utils
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu)

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res=(64, 64), size=1)

mpm.set_gravity((0, -20))

mpm.add_sphere_collider(center=(0.25, 0.5),
                        radius=0.1,
                        surface=mpm.surface_slip)
mpm.add_sphere_collider(center=(0.5, 0.5),
                        radius=0.1,
                        surface=mpm.surface_sticky)

mpm.add_sphere_collider(center=(0.75, 0.5),
                        radius=0.1,
                        surface=mpm.surface_separate)

for frame in range(80):
    gui.circle((0.75, 0.5), color = 0xFFFFFF, radius=0.1)
    mpm.add_cube((0.2, 0.8), (0.1, 0.03),
                 mpm.material_water,
                 color=0x8888FF)
    mpm.add_cube((0.45, 0.8), (0.1, 0.03),
                 mpm.material_water,
                 color=0xFF8888)
    mpm.add_cube((0.7, 0.8), (0.1, 0.03),
                 mpm.material_water,
                 color=0xFFFFFF)
    mpm.step(4e-3)
    particles = mpm.particle_info()
    np_x = particles['position'] / 1.0

    screen_pos = np.stack([screen_x, screen_y], axis=-1)

    gui.circles(screen_pos, radius=1.1, color=particles['color'])
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif=True)
