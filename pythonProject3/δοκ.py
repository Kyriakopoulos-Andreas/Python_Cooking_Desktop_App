class Menu(customtkinter.CTk):
    def __init__(self, prev_x, prev_y, intro_width, intro_height, counter, intro):
        super().__init__()

        self.recipe_search_window = None
        self._resize_image_callback = None
        self.information_window = None
        self.textboxes = None
        self.slider_count = None
        self.slider_button = None
        self.slider = None
        self.register_photo = None
        self.reg_image = None
        self.combobox_tittle = None
        self.combobox = None
        self.entry2 = None
        self.Save_Button = None
        self.Recipe_name = None
        self.recipe_tittle = None
        self.mid_frame = None
        self.tittle = None
        self.pop_up = None
        self.counter = counter
        self.parent = intro

        self.dialog = None
        self.search = customtkinter.StringVar()
        self.title("Let's Cook")

        self.geometry("{0}x{1}+{2}+{3}".format(intro_width, intro_height, prev_x, prev_y, ))

        self.resizable(True, True)
        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")

        self.image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")
        self.photoImage = ImageTk.PhotoImage(self.image)

        # Create a label and place it in the window
        self.label = tk.Label(self, image=self.photoImage)
        self.photoLabel = self.label
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Schedule the first image resize

        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 4), weight=1)

        # left frame
        self.left_frame = customtkinter.CTkFrame(self.parent, width=200, corner_radius=0)
        self.left_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)
        # logo frame
        self.logo_label = customtkinter.CTkLabel(self.left_frame, text="Let's   Cook",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Buttons
        self.button1 = customtkinter.CTkButton(self.left_frame, text="Registration Recipe",
                                               command=self.registration_window,
                                               width=120, height=40)
        self.button1.grid(row=1, column=0, padx=20, pady=(80, 20), )
        self.button2 = customtkinter.CTkButton(self.left_frame, text="Editing", width=130, height=40)
        self.button2.grid(row=2, column=0, padx=20, pady=10)
        # Search window button
        self.search_button = customtkinter.CTkButton(self.left_frame, text="Recipe Search", width=130, height=40,
                                                     command=self.search_button_click)
        self.search_button.grid(row=3, column=0, padx=0, pady=20, )
        # Delete Button
        self.button3 = customtkinter.CTkButton(self.left_frame, text="Word's Cuisines",
                                               width=130, height=40, command=self.word_cuisine)
        self.button3.grid(row=4, column=0, padx=0, pady=10, )

        # exit button
        self.exit_button = customtkinter.CTkButton(self, text="Exit", width=120, height=40,
                                                   command=self.exit_app)
        self.exit_button.grid(row=5, column=2, padx=0, pady=0)

        self.option_value = customtkinter.StringVar()
        self.appearance_mode_label = customtkinter.CTkLabel(self.left_frame, text="Appearance Mode:", width=10,
                                                            height=55, anchor="nw", font=("TkDefaultFont:", 15))
        self.appearance_mode_label.grid(row=7, column=0, padx=10, pady=0, sticky="n")

        self.option_button = customtkinter.CTkOptionMenu(self.left_frame, values=["Dark", "Light", "System"],
                                                         command=self.change_skin, font=("Arial", 12))
        self.option_button.grid(row=7, column=0, padx=5, pady=20, sticky="s")

    def search_button_click(self):
        # Get the position and size of the current window
        prev_x = self.winfo_x()
        prev_y = self.winfo_y()
        intro_width = self.winfo_width()
        intro_height = self.winfo_height()

        # Destroy the current window
        self.destroy()

        # Create a new instance of Recipe_search with the position and size information
        self.recipe_search_window = Recipe_search(prev_x, prev_y, intro_width, intro_height, self.counter)

        # Start the main loop for the new window
        self.recipe_search_window.mainloop()

    def exit_app(self):
        user_input = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if user_input:
            self.destroy()

    def change_skin(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def registration_window(self):
        # Get the position and size of the current window
        prev_x = self.winfo_x()
        prev_y = self.winfo_y()
        intro_width = self.winfo_width()
        intro_height = self.winfo_height()

        # Destroy the current window
        self.destroy()

        # Create a new instance of RegistrationDef with the position and size information
        self.registration_window = Registration(prev_x, prev_y, intro_width, intro_height)

        # Start the main loop for the new window
        self.registration_window.mainloop()

    def word_cuisine(self):
        self.information_window = Word_cuisine()
        self.information_window.mainloop()