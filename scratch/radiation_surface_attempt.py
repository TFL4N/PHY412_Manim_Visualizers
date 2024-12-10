from manim import *
import numpy as np



class RadiationSurface(ThreeDScene):
    def construct(self):
        beta = 0.01
        def radiation(theta, phi):
            r = 1 / (1 - beta*np.cos(theta))
            return np.array([r * np.sin(theta) * np.cos(phi),
                             r * np.sin(theta) * np.sin(phi),
                             r * np.cos(theta)])


        
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*radiation(u, v)),
            u_range=[0, PI],
            v_range=[0, 2*PI],
            resolution=8,
        )
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.add(axes, surface)
        self.wait()
