from tkinter import Entry, E, font


class TextLineCollection:
    def __init__(self, frame_dict):
        default_font = font.Font(family="Helvetica", size=12)
        default_width = 10

        self.processor_quantity_entry = Entry(frame_dict['host_hardware_frame'],
                                              width=default_width,
                                              font=default_font,
                                              )
        self.number_of_cores_entry = Entry(frame_dict['host_hardware_frame'],
                                           width=default_width,
                                           font=default_font,
                                           )
        self.gigahertz_entry = Entry(frame_dict['host_hardware_frame'],
                                     width=default_width,
                                     font=default_font,
                                     )

        self.ram_per_host_entry = Entry(frame_dict['host_hardware_frame'],
                                        width=default_width,
                                        font=default_font
                                        )

        self.vcpu_to_core_ratio_entry = Entry(frame_dict['hypervisor_parameters_frame'],
                                              width=default_width,
                                              font=default_font,
                                              )

        self.cores_assigned_to_hypervisor_entry = Entry(frame_dict['hypervisor_parameters_frame'],
                                                        width=default_width,
                                                        font=default_font,
                                                        )

        self.ram_assigned_to_hypervisor_entry = Entry(frame_dict['hypervisor_parameters_frame'],
                                                      width=default_width,
                                                      font=default_font,
                                                      )

        self.guest_vcpus_assigned_entry = Entry(frame_dict['vm_parameters_frame'],
                                                width=default_width,
                                                font=default_font,
                                                )

        self.ram_per_guest_entry = Entry(frame_dict['vm_parameters_frame'],
                                         width=default_width,
                                         font=default_font,
                                         )

    def init_text_lines(self):
        self.processor_quantity_entry.grid(column=1, row=1, sticky=E)
        self.number_of_cores_entry.grid(column=1, row=2, sticky=E)
        self.gigahertz_entry.grid(column=1, row=3, sticky=E)
        self.ram_per_host_entry.grid(column=1, row=4, sticky=E)

        self.vcpu_to_core_ratio_entry.grid(column=1, columnspan=2, row=1, sticky=E, padx=(1, 15))
        self.cores_assigned_to_hypervisor_entry.grid(column=1, columnspan=2, row=2, sticky=E, padx=(1, 15))
        self.ram_assigned_to_hypervisor_entry.grid(column=1, columnspan=2, row=3, sticky=E, padx=(1, 15))

        self.guest_vcpus_assigned_entry.grid(column=1, row=1, sticky=E)
        self.ram_per_guest_entry.grid(column=1, row=2, sticky=E)

    def get_input(self):
        line_list = [self.processor_quantity_entry, self.number_of_cores_entry, self.ram_per_host_entry,
                     self.vcpu_to_core_ratio_entry, self.cores_assigned_to_hypervisor_entry, self.ram_assigned_to_hypervisor_entry,
                     self.guest_vcpus_assigned_entry, self.ram_per_guest_entry]

        value_list = []

        normal_color = "#ffffff"
        error_color = "#f7162d"
        error = False

        for line in line_list:
            try:
                result = int(line.get())
            except ValueError:
                line.configure(bg=error_color)
                error = True
            else:
                line.configure(bg=normal_color)
                value_list.append(result)

        try:
            result = float(self.gigahertz_entry.get())
        except ValueError:
            self.gigahertz_entry.configure(bg=error_color)
            error = True
        else:
            self.gigahertz_entry.configure(bg=normal_color)
            value_list.append(result)

        if error:
            return False
        else:
            return value_list
