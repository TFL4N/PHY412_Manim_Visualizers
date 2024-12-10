from manim import *
import numpy as np


print(dir(ThreeDAxes))

class EllipticPolar(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[0,6*PI,PI/4],
            y_range=[0,6*PI,PI/4],
            z_range=[-6,6,1],
            x_length=6*PI,
            y_length=6*PI,
            z_length=6
            )


        theta = ValueTracker(0)
        
        graph = always_redraw(lambda :
        axes.plot(lambda x: np.cos(x), x_range=[0,theta.get_value(),1], color=RED)
                              )

        curve = always_redraw(lambda :
        axes.plot_parametric_curve(lambda x: [0, np.cos(x), 0], t_range=[0,theta.get_value(),1], color=RED)
                              )


        # curve = ParametricCurve3D(
        #     lambda t: np.array([t, np.sin(t), np.cos(t)]),
        #     t_range=[0, theta.get_value()],
        #     color=BLUE
        # )
        
        
        # plane = Surface(
        #     lambda u, v: axes.c2p(np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), u])),
        #     u_range=(-5, 5),
        #     v_range=(-5, 5),
        #     color=GRAY
        # )

        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        self.add(axes, graph, curve)
        self.begin_ambient_camera_rotation(rate=0.1)
        #self.wait(5)
        self.play(theta.animate.set_value(6*PI), run_time=5)
        self.wait()
