from manim import *
import numpy as np


#print(dir(ThreeDAxes))

def total_e(t):
        return [t, np.cos(t), np.cos(t+PI/2)]


class EllipticPolar(ThreeDScene):
    
    
    def construct(self):
        axes = ThreeDAxes(
            x_range=[0,6*PI,PI/4],
            y_range=[0,6*PI,PI/4],
            z_range=[-6,6,1],
            x_length=10,
            y_length=10,
            z_length=10
            )


        theta = ValueTracker(0)
        
        graph = always_redraw(lambda :
        axes.plot_parametric_curve(total_e, t_range=[0,theta.get_value(),1], color=RED)
                              )


        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES,
                                    zoom=0.8)

        self.add(axes, graph)
        self.begin_ambient_camera_rotation(rate=0.1)
        #self.wait(5)
        self.play(theta.animate.set_value(6*PI), run_time=5, rate_func=linear)
        self.wait()
