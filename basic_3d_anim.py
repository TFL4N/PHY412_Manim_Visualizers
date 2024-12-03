from manim import *
import numpy as np


#print(dir(ThreeDAxes))

class EllipticPolar(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-2,2,PI/4],
            y_range=[-2,2,PI/4],
            z_range=[-6,6,1],
            x_length=2,
            y_length=2,
            z_length=6
            )


        theta = ValueTracker(0)
        
        graph = always_redraw(lambda :
        axes.plot(lambda x: np.cos(x), x_range=[0,theta.get_value(),1], color=RED)
                              )

        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        self.add(axes, graph)
        self.begin_ambient_camera_rotation(rate=0.1)
        #self.wait(5)
        self.play(theta.animate.set_value(2*PI), run_time=5)
        self.wait()
