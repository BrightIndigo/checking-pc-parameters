import customtkinter as ctk
import random
import main
from cpuinfo import get_cpu_info

cpu_usage = main.cpu_usage
memory_total = main.memory.total
memory_available = main.memory.available
memory_used = main.memory.used
memory_percent = main.memory.percent
system_info = main.system_info
cpu_info = main.cpu_info
cpu_load = main.cpu_load
ram_usage = main.ram_usage
gpus = main.gpus


def details():
    for widget in window.winfo_children():
        widget.destroy()

    cpu_info_str = ""
    cpu_info_table = []
    for key, value in get_cpu_info().items():
        cpu_info_table.append("{0}: {1}\n".format(key, value))

    values_to_remove = ["python_version: 3.11.3.final.0 (64 bit)\n", 'cpuinfo_version: [9, 0, 0]\n', 'cpuinfo_version_string: 9.0.0\n', "flags: ['3dnow', 'abm', 'acpi', 'aes', 'apic', 'avx', 'avx2', 'bmi1', 'bmi2', 'clflush', 'cmov', 'cx16', 'cx8', 'dca', 'de', 'ds_cpl', 'dtes64', 'dts', 'erms', 'est', 'f16c', 'fma', 'fpu', 'fxsr', 'ht', 'ia64', 'invpcid', 'lahf_lm', 'mca', 'mce', 'mmx', 'monitor', 'movbe', 'msr', 'mtrr', 'osxsave', 'pae', 'pat', 'pbe', 'pcid', 'pclmulqdq', 'pdcm', 'pge', 'pni', 'popcnt', 'pqm', 'pse', 'pse36', 'rdrnd', 'sep', 'serial', 'smep', 'smx', 'ss', 'sse', 'sse2', 'sse4_1', 'sse4_2', 'ssse3', 'tm', 'tm2', 'tsc', 'tscdeadline', 'vme', 'vmx', 'x2apic', 'xsave', 'xtpr']\n"]  # Remove items with values 2 and 4

    cpu_info_table = [item for item in cpu_info_table if item not in values_to_remove]

    for i in cpu_info_table:
        cpu_info_str += i

    label = ctk.CTkLabel(master=window, text=cpu_info_str)
    label.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=1, anchor='center')


window = ctk.CTk()
window.title("Animated Widgets")
window.geometry('1000x700')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def cpu():
    for widget in window.winfo_children():
        widget.destroy()
    label = ctk.CTkLabel(master=window, text=f"CPU usage: {cpu_usage}")
    label.place(relx=0.5, rely=0.05, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.1, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"CPU info {cpu_info}")
    label.place(relx=0.5, rely=0.15, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.2, relheight=0.01, relwidth=1, anchor='center')

    button_x = 0.5
    button = ctk.CTkButton(window, text='details', command=details)
    button.place(relx=button_x, rely=0.8, relheight=0.1, relwidth=0.5, anchor='center')

def gpu():
    for widget in window.winfo_children():
        widget.destroy()

def memory():
    for widget in window.winfo_children():
        widget.destroy()

def systeminfo():
    for widget in window.winfo_children():
        widget.destroy()

def menu():
    for widget in window.winfo_children():
        widget.destroy()
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, relheight=0.9, relwidth=0.4, anchor='center')

    button_x = 0.5
    button = ctk.CTkButton(window, text='CPU', command=cpu)
    button.place(relx=button_x, rely=0.2, relheight=0.1, relwidth=0.2, anchor='center')

    button = ctk.CTkButton(window, text='GPU', command=gpu)
    button.place(relx=button_x, rely=0.4, relheight=0.1, relwidth=0.2, anchor='center')

    button = ctk.CTkButton(window, text='MEMORY', command=memory)
    button.place(relx=button_x, rely=0.6, relheight=0.1, relwidth=0.2, anchor='center')

    button = ctk.CTkButton(window, text='SYSTEM INFO', command=systeminfo)
    button.place(relx=button_x, rely=0.8, relheight=0.1, relwidth=0.2, anchor='center')

menu()


window.mainloop()

