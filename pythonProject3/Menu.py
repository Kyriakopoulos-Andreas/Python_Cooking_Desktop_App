from imports import *




class Menu(customtkinter.CTk):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent  # Δημιουργία μεταβλητή parent για αναφορά στον γονέα
        self.recipe_search_window = None  # Αρχικοποίησεις
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
        self.dialog = None








        self.image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")  # Διαβάζουμε από τον δίσκο την εικόνα
        self.photoImage = ImageTk.PhotoImage(self.image)  # Δημιουργία αντικειμένου εικόνας


        self.label = tk.Label(self.parent, image=self.photoImage)  # Δημιουργία label για τοποθέτηση της εικόνας
        self.label.place(relx=0, rely=0, relwidth=1, relheight=1)



        # Δημιουργία Frame και διαμόρφωση της διάταξης του σε γραμμές και στήλες
        self.buttons_frame = customtkinter.CTkFrame(self.parent, width=200, corner_radius=0)
        self.buttons_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.buttons_frame.grid_rowconfigure(4, weight=1)

        # Διάβασμα της εικόνας και δημιουργία αντικειμένου
        self.img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\lets_cook1.png")
        self.resized_img = self.img.resize((100, 100))  # Resize στην εικόνα
        self.photo = ImageTk.PhotoImage(self.resized_img)

        # Τοποθέτηση της μασκότ πάνω από το κουμπί registration
        self.image_label = customtkinter.CTkLabel(self.buttons_frame, image=self.photo, text=" ")
        self.image_label.grid(row=1, column=0, padx=20, pady=(1, 22))

        # Δημιουργία Label για τον τίτλο της εφαρμογής
        self.logo_label = customtkinter.CTkLabel(self.buttons_frame, text="Let's   Cook",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Δημιουργία Κουμπιού Registration και τοποθέτηση πάνω στο frame
        self.registration_button = customtkinter.CTkButton(self.buttons_frame, text="Registration Recipe",
                                                           command=self.registration_window,
                                                           width=120, height=40)
        self.registration_button.grid(row=1, column=0, padx=20, pady=(80, 20), )
        # Δημιουργία Κουμπιού Search
        self.recipe_search_button = customtkinter.CTkButton(self.buttons_frame, text="Recipe Search", width=130, height=40,
                                                            command=self.search_button_click)
        self.recipe_search_button.grid(row=2, column=0, padx=20, pady=10)
        # Δημιουργία Κουμπιού Word's Cuisines
        self.word_cuisine_button = customtkinter.CTkButton(self.buttons_frame, text="Word's Cuisines", width=130, height=40,
                                                           command=self.word_cuisine)
        self.word_cuisine_button.grid(row=3, column=0, padx=0, pady=20, )
        # Δημιουργία Κουμπιού About us
        self.about_us_button = customtkinter.CTkButton(self.buttons_frame, text="About Us",
                                                       width=130, height=40)
        self.about_us_button.grid(row=4, column=0, padx=0, pady=10, )

        # Δημιουργία Κουμπιού Exit
        self.exit_button = customtkinter.CTkButton(self.parent, text="Exit", width=120, height=40,
                                                   command=self.exit_app)
        self.exit_button.grid(row=5, column=2, padx=0, pady=0)

        # Δημιουργία Επικεφαλίδας για το appearance mode της εφαρμογής
        self.appearance_mode_label = customtkinter.CTkLabel(self.buttons_frame, text="Appearance Mode:", width=10,
                                                            height=55, anchor="nw", font=("TkDefaultFont:", 15))
        self.appearance_mode_label.grid(row=7, column=0, padx=10, pady=0, sticky="n")

        # Δημιουργία widget τύπου option για την επιλογή mode
        self.option_button = customtkinter.CTkOptionMenu(self.buttons_frame, values=["Dark", "Light", "System"],
                                                         command=self.change_skin, font=("Arial", 12))
        self.option_button.grid(row=7, column=0, padx=5, pady=20, sticky="s")

    def search_button_click(self):  # Μέθοδος που ανοίγει το παράθυρο search


        self.label.place_forget()   # Forget στην εικόνα του menu
        self.buttons_frame.grid_remove()  # Remove στο Frame με τα κουμπιά για την εξαφάνιση τους
        self.exit_button.grid_remove()

        # Πέρασμα ορισμάτων στο στην κλάση search του parent και των frame, widget και της εικόνας για την επαναφορά
        # τους κατά την έξοδο από το παράθυρο recipe search
        Recipe_search(self.parent, self.label, self.buttons_frame, self.exit_button)

        



    def exit_app(self):  # Μέθοδος για κλείσιμο της εφαρμογής
        # Παράθυρο προειδοποιήσεις και ελέγχου εξόδου
        user_input = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if user_input:  # Αν η απάντηση είναι True κάνουμε destroy στο parent και κλείνουμε την εφαρμογή
            self.parent.destroy()

    def change_skin(self, new_appearance_mode: str):  # Μέθοδος αλλαγής mode
        # Καλούμε την μέθοδο set_appearance_mode της κλάσης Custom Tkinter για αλλαγή του Mode
        customtkinter.set_appearance_mode(new_appearance_mode)

    def registration_window(self):
        self.label.place_forget()  # Forget στην εικόνα του menu
        self.buttons_frame.grid_remove()  # Remove στο Frame με τα κουμπιά για την εξαφάνιση τους
        self.exit_button.grid_remove()

    # Πέρασμα ορισμάτων στο στην κλάση Registration του parent και των frame, widget και της εικόνας για την επαναφορά
        # τους κατά την έξοδο από το παράθυρο recipe search
        Registration(self.parent, self.label, self.buttons_frame, self.exit_button)

    def word_cuisine(self):
        self.information_window = Word_cuisine()   # Δημιουργία αντικειμένου Word_cuisine
        self.information_window.mainloop()   # Τρέχουμε τον βρόγχο του αυτόνομου παραθύρου



