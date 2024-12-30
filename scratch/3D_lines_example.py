from manim import *
import numpy as np



def total_e(t):
        return np.array([t, np.cos(t), np.cos(t+PI/2)])


class EllipticPolar(ThreeDScene):
    
    
    def construct(self):
        t_start = 0
        t_end = 6*PI
        
        axes = ThreeDAxes(
            x_range=[0,6*PI,PI/4],
            y_range=[0,6*PI,PI/4],
            z_range=[-6,6,1],
            x_length=10,
            y_length=10,
            z_length=10
            )


        # theta = ValueTracker(t_start)
        
        # graph = always_redraw(lambda :
        # axes.plot_parametric_curve(total_e,
        #                            t_range=[t_start,theta.get_value(),0.5], color=RED)
        #                       )

        lines = VGroup()

        dt = 0.5
        for i in range(10):
            e = total_e(i*dt)
            line = Arrow3D(
                start=axes.c2p(i*dt, 0, 0),
                end=axes.c2p(e[0], e[1], e[2]),
                resolution=8,
                color=BLUE
            )
 
            lines.add(line)

        


        
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES,
                                    zoom=0.8)

        self.add(axes, lines)
#        self.add(axes, graph, lines)
        #self.begin_ambient_camera_rotation(rate=0.1)
        #self.wait(5)

        anim_time = 1
#        self.play(UpdateFromAlphaFunc(graph, update_lines), run_time=anim_time)
        self.wait()
