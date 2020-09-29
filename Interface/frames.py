from tkinter import Frame


class FrameCollection:
    def __init__(self, window):
        default_width = 300
        default_height = 220
        default_background = "#202020"

        self.host_hardware_frame = Frame(width=default_width, height=default_height, bg=default_background)
        self.hypervisor_parameters_frame = Frame(width=default_width + 50, height=default_height, bg=default_background)
        self.vm_parameters_frame = Frame(width=default_width, height=default_height, bg=default_background)
        self.results_frame = Frame(width=default_width, height=default_height*2, bg=default_background)

    def get_frames(self):
        return {
            'host_hardware_frame': self.host_hardware_frame,
            'hypervisor_parameters_frame': self.hypervisor_parameters_frame,
            'vm_parameters_frame': self.vm_parameters_frame,
            'results_frame': self.results_frame
        }

    def init_frames(self):
        frame_dict = self.get_frames()

        for frame in frame_dict.values():
            frame.grid_propagate(False)

        self.host_hardware_frame.place(x=95, y=50)
        self.hypervisor_parameters_frame.place(x=445, y=50)
        self.vm_parameters_frame.place(x=855, y=50)

        self.results_frame.place(x=500, y=250)
