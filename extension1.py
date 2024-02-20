import customtkinter as ctk
import random
import main

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
    pass

window = ctk.CTk()
window.title("Animated Widgets")
window.geometry('1000x700')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def layout1():
    label = ctk.CTkLabel(master=window, text=f"CPU usage: {cpu_usage}")
    label.place(relx=0.5, rely=0.05, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.1, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"Total Memory: {memory_total}")
    label.place(relx=0.5, rely=0.15, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.2, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"Available Memory: {memory_available}")
    label.place(relx=0.5, rely=0.25, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.3, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"Used Memory: {memory_used}")
    label.place(relx=0.5, rely=0.35, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.4, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"Memory Percentage: {memory_percent}")
    label.place(relx=0.5, rely=0.45, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"System Info: {system_info}")
    label.place(relx=0.5, rely=0.55, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.6, relheight=0.01, relwidth=1, anchor='center')

    label = ctk.CTkLabel(master=window, text=f"CPU Info: {cpu_info}")
    label.place(relx=0.5, rely=0.65, relheight=0.05, relwidth=1, anchor='center')
    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.7, relheight=0.01, relwidth=1, anchor='center')

    button_x = 0.5
    button = ctk.CTkButton(window, text='details', command=details)
    button.place(relx=button_x, rely=0.8, relheight=0.1, relwidth=0.5, anchor='center')

layout1()

window.mainloop()

