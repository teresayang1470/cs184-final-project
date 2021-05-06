import taichi as ti
import numpy as np
import os
import utils
import random
from engine.mpm_solver import MPMSolver

ti.init(arch=ti.cpu)

gui = ti.GUI("Taichi Elements", res=512, background_color=0x0D1117)
video_manager = ti.VideoManager(output_dir=os.path.basename(__file__)[:-3]+ "_render/", framerate = 30, automatic_build=False)

mpm = MPMSolver(res = (128, 128), gui = gui)


mpm.add_cube(lower_corner=[0, 0], cube_size = [1, .45], material = MPMSolver.material_confetti, color = 0x068587, sample_density = 0.5)


c = (0.5, 0.5)
r = 30

mpm.add_sphere_collider(center = c, radius = r, surface=mpm.surface_slip)

for frame in range(200):
    mpm.step(8e-3)

    if frame < 20 and frame % 10: 
        mpm.add_cube(lower_corner=[0.49, 0.5], cube_size = [0.025, 0.3], material = MPMSolver.material_confetti, color = 0x068587, velocity=[0, .01], sample_density = 0.5)


    particles = mpm.particle_info()
    rand_color = random.randint(0,4)
    rand_color = random.randint(0,4)
    rand_color = random.randint(0,4)

    chunks = np.array_split(particles['position'], 50)

    for x in chunks: 
        random_int = random.randint(0,4)
        if random_int == 0:
            this_color = 0xA864FD
        elif random_int == 1:
            this_color = 0x29CDFF
        elif random_int == 2:
            this_color = 0x78FF44
        elif random_int == 3:
            this_color = 0xFF718D
        elif random_int == 4:
            this_color = 0xFDFF69
        gui.circles(x, radius=1.5, color=this_color)

    gui.circle(c, radius=r, color=0x7C0E8F)
   
    video_manager.write_frame(gui.get_image())
    gui.show()

video_manager.make_video(mp4 = False, gif = True)
