from manim import *
import numpy as np

# scene types
NO_COMPS = 0
VERT_ONLY = 1
HORZ_ONLY = 2
SUPER_POS = 3

class CircularPolarization(ThreeDScene):
    def construct(self):
        scene_type = VERT_ONLY
        
        # time range of propagation segment
        t_range = 10*PI
        t_init = 0
        t_final = t_range
        
        # animate time value
        t_end = ValueTracker(t_init)
        
        # build electric field coordinates
        phase = PI/4
        def total_e(t):
            return np.array([t, np.cos(t), np.cos(t+phase)])

    
        # 3D coordinate system
        axes = ThreeDAxes(
            x_range=[0,t_range,PI/4],
            y_range=[-2,2,1],
            z_range=[-2,2,1],
            x_length=15,
            y_length=10,
            z_length=10
        )

        # propagating electric field vs time
        graph = always_redraw(lambda :
                              axes.plot_parametric_curve(total_e,
                                                         t_range=[t_end.get_value()-t_range, t_end.get_value(), 0.5],
                                                         color=RED)
                              )

        self.add(axes, graph)

        #
        # Objects per scene type
        #
        if scene_type == VERT_ONLY:
            # vertical component of electric field
            def comp_vector(t):
                padding = 1.5
                e = total_e(t)
                e[1] = padding

                return Arrow3D(
                    start=axes.c2p(t, padding, 0),
                    end=axes.c2p(*e),
                    resolution=8,
                    color=BLUE
                )

            comp = always_redraw(lambda : comp_vector(t_end.get_value()))
            self.add(comp)
            
        elif scene_type == SUPER_POS:
            # electric field y & z components translated by x
            def proj_e(x, t):
                e = total_e(t)
                e[0] = x
                return e

            circle = always_redraw(lambda :
                                   axes.plot_parametric_curve(lambda t: proj_e(t_end.get_value(), t),
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
                
            radial = always_redraw(lambda : radial_arrow(t_end.get_value()))
            self.add(circle, radial)
        
            
        # electric field vector checkpoints
        lines = VGroup()
        dx_line = 0.5
        
        def update_lines(group, alpha):
            line_pos = int(alpha * t_range / dx_line)
            if line_pos > len(group.submobjects):
                new_line = Arrow3D(
                    start=axes.c2p(line_pos*dx_line, 0, 0),
                    end=axes.c2p(*total_e(line_pos*dx_line)),
                    resolution=8,
                    color=BLUE
                )
                lines.add(new_line)
                
        self.add(lines)
        

        #
        # Begin animations
        #
    
        # init camera position
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES,
                                    zoom=0.6)
        #self.begin_ambient_camera_rotation(rate=0.1)
    
        # animate
        self.play(t_end.animate.set_value(t_final),
                  UpdateFromAlphaFunc(graph, update_lines),
                  run_time=5,
                  rate_func=linear)
        self.wait()
