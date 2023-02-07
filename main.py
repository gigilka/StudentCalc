import tkinter
import customtkinter
from classes import *
# Modes: system (default), light, dark
customtkinter.set_appearance_mode("light")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("blue")


app = App()  # create CTk window like you do with the Tk window
app.mainloop()
