import tkinter
import customtkinter


class LabelFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        self.label = customtkinter.CTkLabel(self, text="Разделы")
        
        self.label.grid(row=0, column=0, padx=20)
        self.button = customtkinter.CTkButton(
            self, command=self.button_click, text="Линейная алгебра")
        self.button1 = customtkinter.CTkButton(
            self, command=self.button_click1, text="Аналитическая геометрия")
        self.button.grid(row=1, column=0, padx=10, pady=10)
        self.button1.grid(row=1, column=1, padx=10, pady=20)

        # add methods to app
    def button_click(self):
        print("button click")

    def button_click1(self):
        print("button1 click")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.title("Student Calculator")
        self.iconbitmap('main.ico')
        # add widgets to app
        self.frame1 = LabelFrame(self)
        self.frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
