from tkinter import Button, NSEW, font
import math


class ButtonCollection:
    def __init__(self, frame_dict, labels, text_lines, radios):
        large_font = font.Font(family="Helvetica", size=18)
        bg_color = "#666666"

        self.submit_button = Button(frame_dict["results_frame"],
                                    command=lambda: self.calculate(labels, text_lines, radios),
                                    text="Submit",
                                    font=large_font,
                                    bg=bg_color,
                                    activebackground=bg_color,
                                    )

    def init_buttons(self):
        self.submit_button.grid_propagate(False)
        self.submit_button.grid(column=0, row=0, sticky=NSEW)

    def calculate(self, labels, text_lines, radios):
        user_input = text_lines.get_input()
        total_number_of_vms_cpu = 0
        total_number_of_vms_ram = 0
        cores_per_vm = 0

        megahertz_per_vm = 0

        # user input's order: [0]processor quantity, [1]number of cores, [2]ram per host
        # [3]vcpu to core ratio, [4]hypervisor cores, [5]hypervisor_ram
        # [6]guest vcpus, [7]ram per guest, [8]gigahertz. See the get_input method in text_lines.py

        if user_input:
            processor_quantity = user_input[0]
            num_cores = user_input[1]
            ram_per_host = user_input[2]
            vcpu_to_core_ratio = user_input[3]
            hypervisor_cores = user_input[4]
            hypervisor_ram = user_input[5]
            guest_vcpus = user_input[6]
            ram_per_guest = user_input[7]

            gigahertz = user_input[8]

            hyperthreading = radios.hyperthreading

            total_number_of_vms_cpu = ((num_cores * processor_quantity - hypervisor_cores) * vcpu_to_core_ratio) / guest_vcpus
            total_number_of_vms_ram = (ram_per_host - hypervisor_ram) / ram_per_guest
            if hyperthreading:
                total_number_of_vms_cpu = total_number_of_vms_cpu * 1.20
            cores_per_vm = guest_vcpus / vcpu_to_core_ratio
            megahertz_per_vm = (gigahertz * 1000 * cores_per_vm)

        self.output(labels, total_number_of_vms_cpu, total_number_of_vms_ram, cores_per_vm, megahertz_per_vm)

    @staticmethod
    def output(labels, total_number_of_vms_cpu, total_number_of_vms_ram, cores_per_vm, megahertz_per_vm):
        total_number_of_vms = 0

        if total_number_of_vms_ram < total_number_of_vms_cpu:
            total_number_of_vms = ('%.2f' % total_number_of_vms_ram).rstrip('0').rstrip('.')
            labels.constrained_label.configure(text="RAM constrained")
        elif total_number_of_vms_ram > total_number_of_vms_cpu:
            total_number_of_vms = ('%.2f' % total_number_of_vms_cpu).rstrip('0').rstrip('.')
            labels.constrained_label.configure(text="CPU constrained")

        cores_per_vm = ('%.2f' % cores_per_vm).rstrip('0').rstrip('.')
        megahertz_per_vm = ('%.2f' % megahertz_per_vm).rstrip('0').rstrip('.')

        total_number_of_vms = math.floor(float(total_number_of_vms))
        megahertz_per_vm = math.floor(float(megahertz_per_vm))

        labels.total_number_of_vms_label.configure(text="Total Number of VMs: " + str(total_number_of_vms))
        labels.cores_per_vm_label.configure(text="Cores per VM: " + str(cores_per_vm))

        if megahertz_per_vm > 1000:
            gigahertz_per_vm = megahertz_per_vm/1000
            labels.megahertz_per_vm_label.configure(text="GHz per VM: " + str(gigahertz_per_vm))
        else:
            labels.megahertz_per_vm_label.configure(text="MHz per VM: " + str(megahertz_per_vm))
