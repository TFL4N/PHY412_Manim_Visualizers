from manim import *
import numpy as np




class EllipticPolarization(ThreeDScene):
    def construct(self):
        # time range
        t_start = 0
        t_end = 10*PI

        # build electric field coordinates
        phase = PI/4
        def total_e(t):
            return np.array([t, np.cos(t), np.cos(t+phase)])
    
    
        # 3D coordinate system
        axes = ThreeDAxes(
            x_range=[t_start,t_end,PI/4],
            y_range=[-2,2,1],
            z_range=[-2,2,1],
            x_length=15,
            y_length=10,
            z_length=10
        )

        # animate time value
        t_val = ValueTracker(t_start)

        # electric field vs time
        graph = always_redraw(lambda :
                              axes.plot_parametric_curve(total_e,
                                                         t_range=[t_start,t_val.get_value(),0.5],
                                                         color=RED)
                              )

        # electric field projected into yz plane
        def proj_e(x, t):
            e = total_e(t)
            e[0] = x
            return e
        circle = always_redraw(lambda :
                               axes.plot_parametric_curve(lambda t: proj_e(t_val.get_value(), t),
                                                          t_range=[0,2*PI,0.5],
                                                          color=RED
                                                          )
                               )

        # electric field vector in projection
        def radial_arrow(t):
            return Arrow3D(
                start=axes.c2p(t, 0, 0),
                end=axes.c2p(*total_e(t)),
                resolution=8,
                color=BLUE
            )
                

        radial = always_redraw(lambda : radial_arrow(t_val.get_value()))

        # electric field vector checkpoints
        lines = VGroup()
        dx_line = 0.5
        
        def update_lines(group, alpha):
            line_pos = int(alpha * (t_end-t_start) / dx_line)
            if line_pos > len(group.submobjects):
                new_line = Arrow3D(
                    start=axes.c2p(line_pos*dx_line, 0, 0),
                    end=axes.c2p(*total_e(line_pos*dx_line)),
                    resolution=8,
                    color=BLUE
                )
                lines.add(new_line)
                
        # add objects to scene
        self.add(axes, graph, lines, circle, radial)
                
    
        # init camera position
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES,
                                    zoom=0.6)
        #self.begin_ambient_camera_rotation(rate=0.1)
    
        # animate
        self.play(t_val.animate.set_value(t_end),
                  UpdateFromAlphaFunc(graph, update_lines),
                  run_time=5,
                  rate_func=linear)
        self.wait()
