import customtkinter
from Menu import Menu
from intro import INTRO


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")




if __name__ == "__main__":
    app = INTRO()
    app.mainloop()

