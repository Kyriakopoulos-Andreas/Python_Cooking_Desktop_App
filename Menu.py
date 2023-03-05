from imports import *


class Menu(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pop_up_window = None
        self.pop_up = None

        self.dialog = None
        self.search = customtkinter.StringVar()
        self.title("Let's Cook")
        self.geometry(f"{1400}x{800}")
        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")

        self.image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")
        self.photoImage = ImageTk.PhotoImage(self.image)

        # Create a label and place it in the window
        label = tk.Label(self, image=self.photoImage)
        self.photoLabel = label
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Bind a function to the window resize event to update the image size
        self.bind("<Configure>", self.resize_image)









        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2,4), weight=1)








        # left frae
        self.left_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.left_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)
        # logo frame
        self.logo_label = customtkinter.CTkLabel(self.left_frame, text="Let's   Cook",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        # Buttons
        self.button1 = customtkinter.CTkButton(self.left_frame, text="Registration Recipe", command=self.button_click, width=120, height=40)
        self.button1.grid(row=1, column=0, padx=20, pady=20,)
        self.button2 = customtkinter.CTkButton(self.left_frame, text="Editing", width=130, height=40)
        self.button2.grid(row=2, column=0, padx=20, pady=10,)
        # Search window button
        self.search_button = customtkinter.CTkButton(self.left_frame, text="Recipe Search", width=130, height=40,
                                                     command=self.search_button_click)
        self.search_button.grid(row=3, column=0, padx=0, pady=20,)
        # Delete Button
        self.button3 = customtkinter.CTkButton(self.left_frame, text="Delete", width=130, height=40)
        self.button3.grid(row=4, column=0, padx=0, pady=10,)



        # exit button
        self.exit_button = customtkinter.CTkButton(self, text="Exit", width=120, height=40,
                                                   command=self.exit_app)
        self.exit_button.grid(row=5, column=2, padx=0, pady=0)


        self.option_value = customtkinter.StringVar()
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_frame, text="Appearance Mode:", width=10,
                                                            height=55, anchor="nw", font=("TkDefaultFont:", 15))
        self.appearance_mode_label.grid(row=7, column=0, padx=10, pady=0, sticky="n")

        self.option_button = customtkinter.CTkOptionMenu(self.left_frame, values=["Dark", "Light", "System"],
                                                         command=self.change_skin,font=("Arial", 12))
        self.option_button.grid(row=7, column=0, padx=5, pady=20, sticky="s")


    def search_button_click(self):
        search_text = self.search.get()
        self.dialog = customtkinter.CTkInputDialog(text="Search for something delicious", title="Recipe Search")
        print(f"Searching for '{search_text}'...")
        dialog_width = 400
        dialog_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - dialog_width) // 2
        y = (screen_height - dialog_height) // 2
        self.dialog.geometry(f"{dialog_width}x{dialog_height}+{x}+{y}")

    def resize_image(self, event):
        # Get the new size of the window
        width = event.width
        height = event.height

        # Start a new thread to resize the image
        threading.Thread(target=self._resize_image_thread, args=(width, height)).start()

    def _resize_image_thread(self, width, height):
        # Resize the image to fit the new size of the window
        image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")
        image = image.resize((width, height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.photoLabel.configure(image=photo_image)
        self.photoLabel.image = photo_image


    def exit_app(self):
        user_input = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if user_input:
            self.destroy()


    def change_skin(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def button_click(self):

        self.pop_up = customtkinter.CTk()
        self.withdraw()
        self.pop_up.geometry(f"{1000}x{600}")
        self.pop_up_window = customtkinter.CTkLabel(self.pop_up, text="Home Page", font=('Century Gothic', 60))
        self.pop_up_window.grid(row=1, column=2)
        self.pop_up.mainloop()



