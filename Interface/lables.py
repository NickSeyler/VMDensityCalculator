from tkinter import Label, NSEW, E, font


class LabelCollection:
    def __init__(self, text_frame_dict):
        default_font = font.Font(family="Helvetica", size=12)
        large_font = font.Font(family="Helvetica", size=18)
        middle_font = font.Font(family="Helvetica", size=14)
        bg_color = "#202020"
        fg_color = "#969696"
        constrained_color = "#f7162d"

        self.host_hardware_label = Label(text_frame_dict['host_hardware_frame'],
                                         text="Hardware Parameters",
                                         font=large_font,
                                         bd=10,
                                         bg=bg_color,
                                         fg=fg_color
                                         )

        self.processor_quantity_label = Label(text_frame_dict['host_hardware_frame'],
                                              text="Processor Quantity: ",
                                              font=default_font,
                                              bd=5,
                                              bg=bg_color,
                                              fg=fg_color
                                              )

        self.number_of_cores_label = Label(text_frame_dict['host_hardware_frame'],
                                           text="Number of Cores: ",
                                           font=default_font,
                                           bd=5,
                                           bg=bg_color,
                                           fg=fg_color
                                           )
        self.gigahertz_label = Label(text_frame_dict['host_hardware_frame'],
                                     text="GHz: ",
                                     font=default_font,
                                     bd=5,
                                     bg=bg_color,
                                     fg=fg_color
                                     )

        self.ram_per_host_label = Label(text_frame_dict['host_hardware_frame'],
                                        text="RAM per host: ",
                                        font=default_font,
                                        bd=5,
                                        bg=bg_color,
                                        fg=fg_color
                                        )

        self.hypervisor_parameters_label = Label(text_frame_dict['hypervisor_parameters_frame'],
                                                 text="Hypervisor Parameters",
                                                 font=large_font,
                                                 bd=10,
                                                 bg=bg_color,
                                                 fg=fg_color
                                                 )

        self.vcpu_to_core_ratio_label = Label(text_frame_dict['hypervisor_parameters_frame'],
                                              text="vCPU to Core Ratio: ",
                                              font=default_font,
                                              bd=5,
                                              bg=bg_color,
                                              fg=fg_color
                                              )

        self.cores_assigned_to_hypervisor_label = Label(text_frame_dict['hypervisor_parameters_frame'],
                                                        text="Cores assigned to Hypervisor: ",
                                                        font=default_font,
                                                        bd=5,
                                                        bg=bg_color,
                                                        fg=fg_color
                                                        )

        self.ram_assigned_to_hypervisor_label = Label(text_frame_dict['hypervisor_parameters_frame'],
                                                      text="RAM assigned to Hypervisor: ",
                                                      font=default_font,
                                                      bd=5,
                                                      bg=bg_color,
                                                      fg=fg_color
                                                      )

        self.hyperthreading_label = Label(text_frame_dict['hypervisor_parameters_frame'],
                                          text="Hyperthreading: ",
                                          font=default_font,
                                          bd=5,
                                          bg=bg_color,
                                          fg=fg_color
                                          )

        self.vm_parameters_label = Label(text_frame_dict['vm_parameters_frame'],
                                         text="VM Parameters",
                                         font=large_font,
                                         bd=10,
                                         bg=bg_color,
                                         fg=fg_color
                                         )

        self.guest_vcpus_assigned_label = Label(text_frame_dict['vm_parameters_frame'],
                                                text="Guest vCPUs assigned: ",
                                                font=default_font,
                                                bd=5,
                                                bg=bg_color,
                                                fg=fg_color
                                                )

        self.ram_per_guest_label = Label(text_frame_dict['vm_parameters_frame'],
                                         text="RAM per Guest: ",
                                         font=default_font,
                                         bd=5,
                                         bg=bg_color,
                                         fg=fg_color
                                         )

        self.total_number_of_vms_label = Label(text_frame_dict['results_frame'],
                                               text="Total Number of VMs: 0",
                                               font=middle_font,
                                               bd=0,
                                               bg=bg_color,
                                               fg=fg_color
                                               )

        self.constrained_label = Label(text_frame_dict['results_frame'],
                                       text="",
                                       font=middle_font,
                                       bd=0,
                                       bg=bg_color,
                                       fg=constrained_color
                                       )

        self.cores_per_vm_label = Label(text_frame_dict['results_frame'],
                                        text="Cores per VM: 0",
                                        font=middle_font,
                                        bd=30,
                                        bg=bg_color,
                                        fg=fg_color
                                        )

        self.megahertz_per_vm_label = Label(text_frame_dict['results_frame'],
                                            text="MHz per VM: 0",
                                            font=middle_font,
                                            bd=30,
                                            bg=bg_color,
                                            fg=fg_color
                                            )

    def init_labels(self):
        self.host_hardware_label.grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=(50, 1))
        self.processor_quantity_label.grid(column=0, row=1, sticky=E)
        self.number_of_cores_label.grid(column=0, row=2, sticky=E)
        self.gigahertz_label.grid(column=0, row=3, sticky=E)
        self.ram_per_host_label.grid(column=0, row=4, sticky=E)

        self.hypervisor_parameters_label.grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=(30, 1))
        self.vcpu_to_core_ratio_label.grid(column=0, row=1, sticky=E)
        self.cores_assigned_to_hypervisor_label.grid(column=0, row=2, sticky=E)
        self.ram_assigned_to_hypervisor_label.grid(column=0, row=3, sticky=E)
        self.hyperthreading_label.grid(column=0, row=4, sticky=E)

        self.vm_parameters_label.grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=(30, 1))
        self.guest_vcpus_assigned_label.grid(column=0, row=1, sticky=E)
        self.ram_per_guest_label.grid(column=0, row=2, sticky=E)

        self.total_number_of_vms_label.grid_propagate(False)
        self.total_number_of_vms_label.grid(column=0, row=1, sticky=NSEW, pady=(65, 0))
        self.constrained_label.grid_propagate(False)
        self.constrained_label.grid(column=0, row=2, sticky=NSEW)
        self.cores_per_vm_label.grid_propagate(False)
        self.cores_per_vm_label.grid(column=0, row=3, sticky=NSEW)
        self.megahertz_per_vm_label.grid_propagate(False)
        self.megahertz_per_vm_label.grid(column=0, row=4, sticky=NSEW)
