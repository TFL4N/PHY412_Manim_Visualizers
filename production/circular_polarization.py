from manim import *
import numpy as np

# scene types
NO_COMPS = 0
VERT_ONLY = 1 # E2 hat
HORZ_ONLY = 2 # E1 hat
SUPER_POS = 3

# polarization
RIGHT_POLAR = 1
LEFT_POLAR = 2

class CircularPolarization(ThreeDScene):
    def __init__(self, polar, comp, *args, **kwargs):
        self.scene_type = comp
        self.polar_type = polar
        super().__init__(*args, **kwargs)

        
    def construct(self):
        # x range of propagation segment
        x_init = 0
        x_final = 10*PI
        x_range = x_final - x_init
        x_end = ValueTracker(x_init) # animated value

        # time value range
        t_final = 7
        t_end = ValueTracker(0) # animated value
        
        # build electric field coordinates
        phase = PI/2 if self.polar_type == LEFT_POLAR else -PI/2
        def total_e(x, t):
            return np.array([x, np.cos(x-t+phase), np.cos(x-t)])
            
        # 3D coordinate system
        axes = ThreeDAxes(
            x_range=[0,x_range,PI/4],
            y_range=[-2,2,1],
            z_range=[-2,2,1],
            x_length=15,
            y_length=10,
            z_length=10
        )
        ax_labels = axes.get_axis_labels(
            MathTex(r'\hat x').scale(3),
            MathTex(r'\hat E_1').scale(3),
            MathTex(r'\hat E_2').scale(3),
        )

        # propagating electric field vs time
        graph = always_redraw(lambda :
                              axes.plot_parametric_curve(lambda u: total_e(u, t_end.get_value()),
                                                         t_range=[0, x_end.get_value(), 0.5],
                                                         color=RED)
                              )

        self.add(axes, ax_labels, graph)

        #
        # Objects per scene type
        #
        if self.scene_type == VERT_ONLY:
            comp_label = Tex(r"$\hat E_2 \cdot \vec E$")
            
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
            
        elif self.scene_type == HORZ_ONLY:
            comp_label = Tex(r"$\hat E_1 \cdot \vec E$")
            
            # horizontal component of electric field
            def comp_vector(x,t):
                e = total_e(x,t)
                e[2] = 0

                return Arrow3D(
                    start=axes.c2p(x, 0, 0),
                    end=axes.c2p(*e),
                    resolution=8,
                    color=BLUE
                )

            comp = always_redraw(lambda : comp_vector(x_end.get_value(),
                                                      t_end.get_value()))
            self.add(comp)
            
        elif self.scene_type == SUPER_POS:
            comp_label = Tex(r"$\vec E$")

            # electric field y & z components translated by x
            def proj_e(x,t):
                e = total_e(x,t)
                e[0] = x
                return e
            
            # electric field vector in projection
            def radial_arrow(x,t):
                return Arrow3D(
                    start=axes.c2p(x, 0, 0),
                    end=axes.c2p(*total_e(x,t)),
                    resolution=8,
                    color=BLUE
                )
                
            radial = always_redraw(lambda : radial_arrow(x_end.get_value(),
                                                         t_end.get_value()))
            self.add(radial)


        #
        # Labels
        #
        self.add_fixed_in_frame_mobjects(comp_label)
        comp_label.to_corner(DOWN + LEFT)

        hand_label = Tex(r"Right Circular Polarization")
        if self.polar_type == LEFT_POLAR:
            hand_label = Tex(r"Left Circular Polarization")
        self.add_fixed_in_frame_mobjects(hand_label)
        hand_label.to_corner(UP + RIGHT)
        
        #
        # Begin animations
        #
    
        # init camera position
        self.set_camera_orientation(phi=75 * DEGREES,
                                    theta=-45 * DEGREES,
                                    zoom=0.6)
    
        # animate
        self.play(x_end.animate.set_value(x_final),
                  t_end.animate.set_value(t_final),
                  run_time=t_final,
                  rate_func=linear)
        self.wait()


if __name__ == "__main__":
    # scene type to be rendered
    polars = [
        LEFT_POLAR,
        RIGHT_POLAR
    ]
    comps = [
        VERT_ONLY,
        HORZ_ONLY,
        SUPER_POS
    ]

    for p in polars:
        for c in comps:
            p_str = ''
            if p == LEFT_POLAR:
                p_str = 'left'
            elif p == RIGHT_POLAR:
                p_str = 'right'

            c_str = ''
            if c == VERT_ONLY:
                c_str = 'vertical'
            elif c == HORZ_ONLY:
                c_str = 'horizontal'
            elif c == SUPER_POS:
                c_str = 'superposition'
        
            file_name = 'circular_' + p_str + '_' + c_str

            with tempconfig({
                    'preview': True,
                    'quality': 'low_quality',
                    'disable_caching': True,
                    'output_file': file_name
            }):
               CircularPolarization(p,c).render()
