

from imports import *
from Menu import Menu


class Intro(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = None
        self.title("Let's Cook-Intro")

        # Set window size
        # Get the primary monitor's resolution

        primary_monitor = get_monitors()[0]
        width = int(primary_monitor.width)
        height = int(primary_monitor.height + 10)

        # Calculate the window position
        x = int((primary_monitor.width - width) / 2 - 11)
        y = int((primary_monitor.height - height) / 2 - 5)

        # Set the window geometry
        self.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))


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
                                                        command=self.on_close)
        self.LetS_Cook_Button.grid(row=1, column=1, padx=0, pady=0)

    def on_close(self):
        self.photoLabel.destroy()
        self.LetS_Cook_Button.grid_remove()
        # Hide the Intro window
        # Create the Menu window
        self.title("Let's Cook-Menu")
        self.menu = Menu(self)
