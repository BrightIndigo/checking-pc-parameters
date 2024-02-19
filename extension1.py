import customtkinter as ctk
import random

def details():
    pass

window = ctk.CTk()
window.title("Animated Widgets")
window.geometry('1000x700')
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def layout1():

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.1, relheight=0.01, relwidth=1, anchor='center')

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.2, relheight=0.01, relwidth=1, anchor='center')

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.3, relheight=0.01, relwidth=1, anchor='center')

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.4, relheight=0.01, relwidth=1, anchor='center')

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, relheight=0.01, relwidth=1, anchor='center')

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.6, relheight=0.01, relwidth=1, anchor='center')

    frame = ctk.CTkFrame(master=window, corner_radius=10)
    frame.place(relx=0.5, rely=0.7, relheight=0.01, relwidth=1, anchor='center')

    button_x = 0.5
    button = ctk.CTkButton(window, text='details', command=details)
    button.place(relx=button_x, rely=0.8, relheight=0.1, relwidth=0.5, anchor='center')

layout1()

window.mainloop()

