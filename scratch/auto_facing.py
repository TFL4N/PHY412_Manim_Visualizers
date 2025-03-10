from manim import *

class AxesFacingCamera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)

        # Create labels and store them in a dictionary for easy access
        labels = {
            "x": axes.get_x_axis_label("x"),
            "y": axes.get_y_axis_label("y"),
            "z": axes.get_z_axis_label("z"),
        }
        for label in labels.values():
            self.add(label) # Add them to the scene

        # Function to update label orientation
        def update_label_orientation(label):
            camera_position = self.camera.frame_center  # Get camera's position
            label_position = label.get_center() # Get the label's position

            # Vector from label to camera
            vector_to_camera = camera_position - label_position

            # Calculate the rotation needed to make the label face the camera
            # (We use -vector_to_camera because rotate_vector takes the rotation FROM a vector.)
            rotation_angle = -np.arctan2(vector_to_camera[1], vector_to_camera[0])

            # Apply rotation around the z-axis (assuming labels are initially flat)
            label.set_z_index(1) # Ensure labels are on top
            label.rotate(rotation_angle, axis=OUT)

        # Make the labels always redraw and update
        for label in labels.values():
            label.add_updater(update_label_orientation)
            #label.always_redraw()

        # Example camera movement (to demonstrate the labels facing the screen)
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.play(self.rotate(phi=0, theta=60 * DEGREES), run_time=3)
        # self.wait(1)

        self.begin_ambient_camera_rotation()
        self.wait()
        
        # self.play(self.camera.rotate(phi=360 * DEGREES, theta=30 * DEGREES), run_time=5)
        # self.wait(1)
