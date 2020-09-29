from tkinter import Radiobutton, W, NSEW, font, BooleanVar


class RadioCollection:
    def __init__(self, frame_dict):
        default_font = font.Font(family="Helvetica", size=12)
        bg_color = "#202020"
        fg_color = "#969696"

        self.hyperthreading = BooleanVar()

        self.radio_yes = Radiobutton(frame_dict["hypervisor_parameters_frame"],
                                     variable=self.hyperthreading,
                                     value=True,
                                     text="Yes",
                                     font=default_font,
                                     bg=bg_color,
                                     activebackground=bg_color,
                                     highlightbackground="#aaaaaa",
                                     fg=fg_color,
                                     activeforeground=fg_color
                                     )

        self.radio_no = Radiobutton(frame_dict["hypervisor_parameters_frame"],
                                    variable=self.hyperthreading,
                                    value=False,
                                    text="No",
                                    font=default_font,
                                    bg=bg_color,
                                    activebackground=bg_color,
                                    fg=fg_color,
                                    activeforeground=fg_color
                                    )

    def init_radios(self):
        self.radio_yes.grid_propagate(False)
        self.radio_yes.grid(column=2, row=4, sticky=NSEW)
        self.radio_yes.select()

        self.radio_no.grid_propagate(False)
        self.radio_no.grid(column=1, row=4, sticky=W)
