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
    def __init__(self, polar=LEFT_POLAR, comp=SUPER_POS, *args, **kwargs):
        self.scene_type = comp
        self.polar_type = polar
        super().__init__(*args, **kwargs)

        
    def construct(self):
        #
        # Assumptions:
        # use c=1 and w=1
        # this implies k=1
        #
        # the wave front moves at speed c
        #    x=ct=t
        #
        # e-field for positions less than x=ct
        # where x is the position of the wave front
        #  x-dx = t-dx
        #
        # in other words, any x is derived from current t
        #

        
        # time value range
        t_final = 10*PI
        t_end = ValueTracker(0) # animated value

        # t_step controls the resolution (dt) when drawing the
        # e-field curve.  Smaller t_step results in higher resolution
        # t_step = 0.5 quick generation time but sub-par resolution
        # t_step = 0.25 slow generation time but acceptable resolution
        t_step = 0.25
        
        # build electric field coordinates
        phase = PI/2 if self.polar_type == LEFT_POLAR else -PI/2
        def total_e(x, t):
            return np.array([x, np.cos(x-t+phase), np.cos(x-t)])
            
        # 3D coordinate system
        axes = ThreeDAxes(
            x_range=[0,t_final,PI/4],
            y_range=[-2,2,1],
            z_range=[-2,2,1],
            x_length=15,
            y_length=10,
            z_length=10
        )
        ax_labels = axes.get_axis_labels(
            MathTex(r'\hat k').scale(3),
            MathTex(r'\hat E_1').scale(3),
            MathTex(r'\hat E_2').scale(3),
        )

        self.add(axes, ax_labels)

        
        #
        # Objects per scene type
        # - Draw these elements first so that they have low z-numbers
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

            comp = always_redraw(lambda : comp_vector(0,
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

            comp = always_redraw(lambda : comp_vector(0,
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
                
            radial = always_redraw(lambda : radial_arrow(0,
                                                         t_end.get_value()))

            # curve at x=0 for one complete period of e-field
            origin_curve = axes.plot_parametric_curve(lambda u: total_e(0, u),
                                       t_range=[0, 2*PI, t_step],
                                                      color=GREEN)
            
            self.add(radial, origin_curve)

        
        #    
        # Propagating electric field vs time
        # - draws and animates the main e-field curve
        #
        e_curve = lambda : \
            axes.plot_parametric_curve(lambda u: total_e(u, t_end.get_value()),
                                       t_range=[0, t_end.get_value(), t_step],
                                       color=RED)
        e_curve_anim = always_redraw(
            e_curve
        )

        self.add(e_curve_anim)


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
        self.play(t_end.animate.set_value(t_final),
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
