def button_click(self):
    self.pop_up = customtkinter.CTk()
    self.withdraw()
    self.pop_up.geometry(f"{1000}x{800}")
    # self.reg_image = Image.open(r"C:\Users\Admin\Desktop\logo\reg_small_image.jpg")
    # self.register_photo = ImageTk.PhotoImage(self.reg_image)
    # self.photoLabel = tk.Label(self.pop_up)
    # self.photoLabel.image = self.register_photo  # keep reference to avoid garbage collection
    # self.photoLabel.config(image=self.register_photo)  # display the image
    # self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    self.pop_up.grid_columnconfigure((0, 1, 2, 3), weight=1)
    self.pop_up.grid_rowconfigure((0, 1, 2, 3), weight=1)

    self.pop_up.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")
    self.pop_up.title("Let's Cook-Registration Recipe")
    self.main_frame = customtkinter.CTkScrollableFrame(self.pop_up, height=20,
                                                       scrollbar_button_hover_color="orange", )
    self.main_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    self.main_frame.grid_columnconfigure(0, weight=1)
    self.main_frame.grid_columnconfigure(1, weight=0)
    self.main_frame.grid_rowconfigure(3, weight=1)
    self.tittle = customtkinter.CTkLabel(self.pop_up, text="Registration Recipe", font=('Century Gothic', 30))
    self.tittle.grid(row=0, column=2, padx=10, pady=10, sticky="n")
    # Choice Menu
    self.combobox = customtkinter.CTkOptionMenu(self.main_frame, width=50, height=25, corner_radius=10,
                                                dropdown_hover_color="#A4A4A4",
                                                dropdown_font=('Arial', 15), font=('Arial', 18, 'bold'),
                                                values=["Mediterranean", "Chinese", "Mexican", "Arabic",
                                                        "Thai"], )
    self.combobox.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

    # Slider
    self.slider = customtkinter.CTkSlider(self.main_frame, from_=0, to=30, progress_color="orange",
                                          height=13, border_width=1)

    self.slider.grid(row=5, column=0, padx=10, pady=10, sticky="nw")
    self.slider.bind("<ButtonRelease-1>",
                     self.update_count)  # bind the slider to a function to update the count label

    self.slider_count = customtkinter.CTkLabel(self.main_frame, text="00",
                                               font=('Arial', 18,))  # create the label to display the count
    self.slider_count.grid(row=5, column=1, padx=5, pady=5, sticky="w")
    self.slider.bind("<B1-Motion>", self.update_count)

    self.Recipe_name = customtkinter.CTkEntry(self.main_frame, placeholder_text="Enter Recipe Name", width=50,
                                              height=25,
                                              border_width=1, corner_radius=10)
    self.Recipe_name.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

    # Titles
    self.combobox_tittle = customtkinter.CTkLabel(self.main_frame, text="Choose Cuisine:")
    self.combobox_tittle.grid(row=0, column=0, padx=0, pady=0, sticky="w")

    self.recipe_tittle = customtkinter.CTkLabel(self.main_frame, text="Recipe Name:")
    self.recipe_tittle.grid(row=2, column=0, padx=0, pady=0, sticky="w")

    self.recipe_tittle = customtkinter.CTkLabel(self.main_frame, text="Recipe Steps:")
    self.recipe_tittle.grid(row=4, column=0, padx=0, pady=0, sticky="w")

    # Buttons
    self.Save_Button = customtkinter.CTkButton(self.pop_up, text="Save Recipe",
                                               font=('Arial', 13, 'bold'),
                                               command=self.return_to_menu)
    self.Save_Button.grid(row=2, column=3, pady=20, sticky="s")

    self.slider_button = customtkinter.CTkButton(self.main_frame, text="Aply Steps",
                                                 width=30, border_width=0, corner_radius=8,
                                                 font=('Arial', 13, 'bold'), command=self.create_textboxes)
    self.slider_button.grid(row=6, column=0, sticky="nw")

    self.pop_up.mainloop()


def create_textboxes(self):
    number_of_rec = int(self.slider.get())  # We use the value of slider
    print(f"numb: {number_of_rec}")

    self.tab3_text_boxes = []

    # Create new textboxes
    for i in range(number_of_rec):
        textbox = customtkinter.CTkEntry(self.main_frame, width=30, font=('Arial', 12))
        textbox.grid(row=7 + i, column=0, pady=5, padx=5, sticky="nsew")
        self.tab3_text_boxes.append(textbox)


def update_count(self, event):
    # update the count label with the current slider value

    self.slider_count.configure(text="{:02d}".format(int(self.slider.get())))  # format counter value


def return_to_menu(self):
    self.deiconify()
    self.pop_up.destroy()


#self.left_frame = customtkinter.CTkFrame(self.main_frame, fg_color=("#ffffff", "#353839"))
#self.left_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
#self.left_frame.grid_rowconfigure(4, weight=1)

#self.tittle = customtkinter.CTkLabel(self.left_frame, text="Registration Recipe", font=('Century Gothic', 20))
#self.tittle.grid(row=0, column=0, padx=10, pady=30, sticky="n")