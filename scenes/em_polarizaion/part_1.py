from manim import *
import numpy as np


class Part1(ThreeDScene):    
    def construct(self):
        
        # time value range
        t_final = 10*PI
        t_end = ValueTracker(0) # animated value

        # t_step controls the resolution (dt) when drawing the
        # e-field curve.  Smaller t_step results in higher resolution
        # t_step = 0.5 quick generation time but sub-par resolution
        # t_step = 0.25 slow generation time but acceptable resolution
        t_step = 0.5
        
            
        # 3D coordinate system
        # Due to difficuty
        axes = ThreeDAxes(
            x_range=[0,2,1],
            y_range=[0,t_final,PI/2],
            z_range=[0,2,1],
            x_length=10,
            y_length=30,
            z_length=10,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": RED}
        )

        # switch axes around, easier than rotating camera apparently 
        #y_label = axes.get_x_axis_label(MathTex(r'\hat y').scale(3))
        z_label = axes.get_y_axis_label(MathTex(r'\hat z').scale(3))
        x_label = axes.get_z_axis_label(MathTex(r'\hat x').scale(3))

        # position labels to lay flat on screen
        x_label.rotate(PI/2, axis=[1., 0., 0.])
        x_label.rotate(-PI/2, axis=[0., 0., 1.])

        #y_label.rotate(PI/2, axis=[0., 0., 1.])
        
        # group axes and labels
        #graph_grp = VGroup(axes, x_label,y_label, z_label)
        graph_grp = VGroup(axes, x_label, z_label)

        # rotate group and reverse rotate labels
        graph_grp.rotate(-PI/2, axis=[0., 1., 0.])
        x_label.rotate(PI/2, axis=[0., 1., 0.])
        #y_label.rotate(PI/2, axis=[0., 1., 0.])
        z_label.rotate(PI/2, axis=[0., 1., 0.])
        z_label.shift(RIGHT)

        
        self.add(graph_grp)

        # move graph in position on screen
        graph_grp.shift(10*DOWN)
        
        
        
        #self.add(axes, x_label, y_label, z_label)

               
        #
        # Begin animations
        #
    
        # init camera position
        self.set_camera_orientation(phi=0 * DEGREES, # polar
                                    theta=0 * DEGREES, # azimuthal
                                    gamma=0 * DEGREES, # yaw
                                    zoom=0.2)
    
        # animate
        self.play(t_end.animate.set_value(t_final),
                  run_time=t_final,
                  rate_func=linear)
        self.wait()
