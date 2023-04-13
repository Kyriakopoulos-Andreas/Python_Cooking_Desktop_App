from imports import *
from Menu import Menu



class Intro(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = None
        self.title("Let's Cook")


        # Set window size
        self.overrideredirect(False)  # to allow for the window decorations
        width = int(self.winfo_screenwidth() * 1.039)
        height = int(self.winfo_screenheight() * 0.941)
        x = int(self.winfo_screenwidth() / 2 - width / 2 + 25)
        y = int(self.winfo_screenheight() / 2 - height / 2 - 40)
        self.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))
        self.resizable(True, True)
        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")
        self.image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")
        self.photoImage = ImageTk.PhotoImage(self.image)

        # Create a label and place it in the window
        self.photoLabel = tk.Label(self, image=self.photoImage)
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # intro layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.img = Image.open(r"C:\Users\Admin\Desktop\logo\chef.png")
        self.img = self.img.resize((24, 24))
        self.photo = customtkinter.CTkImage(self.img)

        # Entry Button
        self.LetS_Cook_Button = customtkinter.CTkButton(self, text="Let's Cook", width=200, height=40, image=self.photo,
                                                        corner_radius=2, text_color='Black', fg_color="#A4A4A4",
                                                        font=('Arial', 20),
                                                        command=self.show_second_window)
        self.LetS_Cook_Button.grid(row=1, column=1, padx=0, pady=0)





    def show_second_window(self):
        self.destroy()
        self.menu = Menu()
        self.menu.mainloop()
