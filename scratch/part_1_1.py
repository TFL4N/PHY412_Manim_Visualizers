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
            y_range=[0,2,1],
            z_range=[0,2,1],
            x_length=10,
            y_length=10,
            z_length=10,
            x_axis_config={"color": BLUE},
            y_axis_config={"color": GREEN},
            z_axis_config={"color": RED}
        )
#        axes.rotate(PI/2, axis=[0., 1., 0.])
        # axes.move_to(LEFT)
        
        ax_labels = axes.get_axis_labels(
            MathTex(r'\hat x').scale(3),
            MathTex(r'\hat y').scale(3),
            MathTex(r'\hat z').scale(3),
        )

        self.add(axes, ax_labels)

               
        #
        # Begin animations
        #
    
        # init camera position
        # print(self.camera.frame_height)
        # print(self.camera.frame_width)
        # print(self.camera.frame_center)
        # print(axes.c2p(*ORIGIN))
        # print(axes.p2c(self.camera.frame_center))
        # #self.camera.frame_center =  [-2.5, 2.5, 0.]
        # #self.camera.frame_center =  -1 * axes.c2p(*ORIGIN)
        # self.camera.frame_center =  axes.c2p(*ORIGIN)
        # print('-----')
        # print(self.camera.frame_center)
        # print(axes.c2p(*ORIGIN))
        # print(axes.p2c(self.camera.frame_center))
        

        # axes.move_to(-1 * axes.c2p(*ORIGIN))
        # #self.camera.frame_center =  [2.5, 0., 0.]
        # axes.move_to(-1 * axes.c2p(*ORIGIN) + [5., 0., 0.])
        # print("****")
        # print(axes.c2p(*ORIGIN))
        # #self.camera.frame_center = axes.c2p(*ORIGIN)
        # print(self.camera.frame_center)

        self.set_camera_orientation(phi=0 * DEGREES, # polar
                                    theta=0 * DEGREES, # azimuthal
                                    gamma=0 * DEGREES, # yaw
                                    zoom=0.4)
        #self.set_camera_orientation(zoom=0.6)
    
        # animate
        self.play(t_end.animate.set_value(t_final),
                  run_time=t_final,
                  rate_func=linear)
        self.wait()
