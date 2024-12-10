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
        
        # x range of propagation segment
        x_init = 0
        x_final = 10*PI
        x_range = x_final - x_init
        x_end = ValueTracker(x_init) # animated value

        # time value range
        t_final = 7
        t_end = ValueTracker(0) # animated value
        
        # build electric field coordinates
        phase = PI/2
        def total_e(x, t):
            return np.array([x, np.cos(x-t), np.cos(x-t+phase)])

    
        # 3D coordinate system
        axes = ThreeDAxes(
            x_range=[0,x_range,PI/4],
            y_range=[-2,2,1],
            z_range=[-2,2,1],
            x_length=15,
            y_length=10,
            z_length=10
        )

        # propagating electric field vs time
        graph = always_redraw(lambda :
                              axes.plot_parametric_curve(lambda u: total_e(u, t_end.get_value()),
                                                         t_range=[0, x_end.get_value(), 0.5],
                                                         color=RED)
                              )

        self.add(axes, graph)

        #
        # Objects per scene type
        #
        if scene_type == VERT_ONLY:
            # vertical component of electric field
            def comp_vector(x,t):
                e = total_e(x,t)
                e[1] = 0

                return Arrow3D(
                    start=axes.c2p(x, 0, 0),
                    end=axes.c2p(*e),
                    resolution=8,
                    color=BLUE
                )

            comp = always_redraw(lambda : comp_vector(x_end.get_value(),
                                                      t_end.get_value()))
            self.add(comp)
            
        elif scene_type == SUPER_POS:
            # electric field y & z components translated by x
            def proj_e(x,t):
                e = total_e(x,t)
                e[0] = x
                return e

            circle = always_redraw(lambda :
                                   axes.plot_parametric_curve(lambda u: proj_e(x_end.get_value(), u),
                                                              t_range=[0,2*PI,0.5],
                                                              color=RED
                                                              )
                                   )
            
            # electric field vector in projection
            def radial_arrow(x):
                return Arrow3D(
                    start=axes.c2p(x, 0, 0),
                    end=axes.c2p(*total_e(x)),
                    resolution=8,
                    color=BLUE
                )
                
            radial = always_redraw(lambda : radial_arrow(x_end.get_value()))
            self.add(circle, radial)
        
        #
        # Begin animations
        #
    
        # init camera position
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES,
                                    zoom=0.6)
        #self.begin_ambient_camera_rotation(rate=0.1)
    
        # animate
        self.play(x_end.animate.set_value(x_final),
                  t_end.animate.set_value(t_final),
                  run_time=t_final,
                  rate_func=linear)
        self.wait()
