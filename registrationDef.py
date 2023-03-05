import customtkinter as ctk
from Menu import Menu
from imports import *

app = Menu()

class Reg(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def button_click():
        pop_up = ctk.CTk()
        pop_up.geometry(f"{1400}x{800}")
        pop_up_window = ctk.CTkLabel(pop_up, text="Home Page", font=('Century Gothic', 60))
        pop_up_window.grid(row=1, column=2)
        app.withdraw()
        pop_up.mainloop()

