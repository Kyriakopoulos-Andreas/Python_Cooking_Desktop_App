import tkinter

from imports import *
import sqlite3

conn = sqlite3.connect("Recipes.db")
# conn.execute("drop table Recipe")
# conn.execute("drop table Step")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Recipe(recipeId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,cuisine TEXT, category TEXT, difficulty TEXT, duration INTEGER,ingredients TEXT) ")
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Step(stepId INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, instructions TEXT, time INTEGER,recipeId INTEGER, FOREIGN KEY (recipeId) REFERENCES Recipe(recipeId)) ")
conn.commit()


class Registration(customtkinter.CTk):
    def __init__(self, parent_menu, photo_label, buttons_frame, exit_button):
        super().__init__()
        self.parent = parent_menu
        self.parent = parent_menu
        self.photoLabel = photo_label
        self.buttons_frame = buttons_frame
        self.exit_button = exit_button
        self.extra_title = None
        self.extra_title2 = None

        self.counter_of_text_boxes = None
        self.format_categoriess = None
        self.extra_title2 = None
        self.entry_third_step = None
        self.extra_title = None
        self.step_entry_boxes = []
        self.timers = []
        self.subtract_button_timers = []
        self.step_title_boxes = []
        self.add_button_timers = []
        self.step_message_array = []
        self.back = None
        self.main_frame = None
        self.recipe_tittle = None
        self.current_timer_index = 0
        self.text_boxes_counter = 0

        self.step_size = 3
        # Set window size to full screen
        self.parent.title("Let's Cook-Registration")

        # Set window position and size

        # self.reg_image = Image.open(r"C:\Users\Admin\Desktop\logo\reg_small_image.jpg")
        # self.register_photo = ImageTk.PhotoImage(self.reg_image)
        # self.photoLabel = tk.Label(self.pop_up)
        # self.photoLabel.image = self.register_photo  # keep reference to avoid garbage collection
        # self.photoLabel.config(image=self.register_photo)  # display the image
        # self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.iconbitmap(r"C:/Users/Admin/PycharmProjects/pythonProject3/logo/image.ico")
        self.title("Let's Cook-Registration Recipe")
        self.outside_frame = customtkinter.CTkFrame(self.parent, height=600)
        self.outside_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15),
                                sticky="nsew")
        self.outside_frame.grid_rowconfigure(4, weight=1)
        self.outside_frame.grid_columnconfigure(4, weight=0)

        self.main_frame = customtkinter.CTkFrame(self.outside_frame, width=2000, corner_radius=20, height=80)
        self.main_frame.grid(row=0, column=1, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15),
                             sticky="nsew")
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_columnconfigure((0, 1, 2, 4, 5), weight=1)

        self.tabview = customtkinter.CTkTabview(self.main_frame, border_width=5, corner_radius=30, width=1550)
        self.tabview.grid(row=0, column=1, rowspan=3, columnspan=4, padx=(10, 160), pady=(20, 20), sticky="nsew")
        self.tabview.add("step 1")
        self.tabview.add("step 2")
        self.tabview.add("step 3")
        for tab_name in ["step 1", "step 2", "step 3"]:
            tab_frame = self.tabview.tab(tab_name)
            tab_frame.grid_columnconfigure(0, weight=0)
            tab_frame.grid_columnconfigure(1, weight=0)
            tab_frame.grid_rowconfigure(0, weight=0)
            tab_frame.grid_rowconfigure(1, weight=0)

        # Buttons

        self.Save_Button = customtkinter.CTkButton(self.main_frame, text="Save Recipe", font=('Arial', 13, 'bold'),
                                                   command=self.save_registration, corner_radius=20)
        self.Save_Button.grid(row=3, column=2, pady=(1, 15), padx=(1, 165), sticky="nsew")

        self.Back_Button = customtkinter.CTkButton(self.main_frame, text="←  back ", font=('Arial', 13, 'bold'),
                                                   height=27, width=130, corner_radius=7, command=self.return_to_menu)
        self.Back_Button.grid(row=0, column=0, pady=(10, 1), padx=(10, 1), sticky="nw")

        self.cuisine_box = customtkinter.CTkOptionMenu(self.tabview.tab("step 1"), width=400, height=25,
                                                       corner_radius=10,
                                                       dropdown_hover_color="#A4A4A4", dynamic_resizing=False,
                                                       dropdown_font=('bold', 18), font=('Arial', 18, 'bold'),
                                                       command=self.display_categories,
                                                       values=[
                                                           f"{'Mediterranean':^65}",
                                                           f"{'Chinese':^70}",
                                                           f"{'Mexican':^70}",
                                                           f"{'Arabic':^70}",
                                                           f"{'Thai':^70}"])

        self.cuisine_box.grid(row=1, column=0, padx=(500, 90), pady=(20, 60), sticky="s")
        self.cuisine_box.set(f"{'Choose Cuisine':>40}")

        self.chinese_categories = ["BaoBan", "Noodles", "Sushi", "Ramen", "Soups", "Rice Dish", "Bowl",
                                   "Street Food"]
        self.mexican_categories = ["Tacos", "Burritos", "Enchiladas", "Fajitas", "Quesadilla", "Nachos"]
        self.italian_categories = ["Pizza", "Pasta", "Lasagna", "Risotto", "Dessert"]
        self.mediterranean_categories = ["Sea Food", "Meet", "Salad", "Vegetable", "Legumes", "Pie", "Pasta's",
                                         "Dessert"]
        self.thai_categories = ["Sea Food", "Soups", "Curries", "Pounded", "Noodles", "Rice Dish", "Salads"]
        self.arabic_categories = ["Shakshuka", "Lahmacun", "Falafel", "Hummus", "Kebab", "Salad", "Dessert"
                                  ]

        self.format_categories = [
            self.chinese_categories,
            self.mexican_categories,
            self.italian_categories,
            self.mediterranean_categories,
            self.thai_categories,
            self.arabic_categories
        ]

        # Loop through each category list
        for category in self.format_categories:
            for i in range(len(category)):
                # Apply the formatting to each element in the category list
                category[i] = f"{category[i]:^82}"

        self.category_box = customtkinter.CTkOptionMenu(self.tabview.tab("step 1"),
                                                        width=500, height=25, corner_radius=10,
                                                        dropdown_hover_color="#A4A4A4", dynamic_resizing=False,
                                                        dropdown_font=('bold', 18), font=('Arial', 18, 'bold'),
                                                        values=[
                                                            f"{'Sea Food':^82}",
                                                            f"{'Meet':^82}",
                                                            f"{'Salad':^82}",
                                                            f"{'Vegetable':^82}",
                                                            f"{'Legumes':^82}",
                                                            f"{'Pie':^82}",
                                                            f"{'Pasta':^82}",
                                                            f"{'Dessert':^82}"])
        self.category_box.set(f"{'Choose Category':>48}")
        self.category_box.grid(row=3, column=0, padx=(420, 1), pady=(10, 1), sticky="s")

        # Bind the <<ComboboxSelected>> event to the display_categories method

        self.difficulty_box = customtkinter.CTkOptionMenu(self.tabview.tab("step 1"),
                                                          width=500, height=25, corner_radius=10,
                                                          dropdown_hover_color="#A4A4A4", dynamic_resizing=False,
                                                          dropdown_font=('bold', 18), font=('Arial', 18, 'bold'),
                                                          values=[
                                                              f"{'Easy':^85}",
                                                              f"{'Medium':^82}",
                                                              f"{'Difficult':^86}",
                                                          ], )
        self.difficulty_box.grid(row=4, column=0, padx=(420, 1), pady=(10, 1), sticky="s")
        self.difficulty_box.set(f"{'Choose Level':>47}")

        self.Recipe_name = customtkinter.CTkEntry(self.tabview.tab("step 1"),
                                                  placeholder_text="                    "
                                                                   "                     "
                                                                   "                      "
                                                                   "Enter Recipe Name", width=500,
                                                  height=25,
                                                  border_width=1, corner_radius=10)
        self.Recipe_name.grid(row=2, column=0, padx=(420, 1), pady=10, sticky="s")

        self.subtract_button = customtkinter.CTkButton(self.tabview.tab("step 1"), text="-", width=100 - 6,
                                                       height=32 - 6,
                                                       command=self.step1_subtract)
        self.subtract_button.grid(row=7, column=0, padx=(274, 200), pady=3)

        self.time_displayer = customtkinter.CTkEntry(self.tabview.tab("step 1"), width=250, height=26,
                                                     border_width=0)
        self.time_displayer.grid(row=7, column=0, padx=(620, 1), pady=1, sticky="w")

        self.add_button = customtkinter.CTkButton(self.tabview.tab("step 1"), text="+", width=100 - 6, height=32 - 6,
                                                  command=self.step1_add)
        self.add_button.grid(row=7, column=0, padx=(740, 1), pady=3)
        # default value
        self.time_displayer.insert(0, "                                  0:00")

        # Titles
        self.tittle = customtkinter.CTkLabel(self.main_frame, text="Registration Recipe", font=('Century Gothic', 20))
        self.tittle.grid(row=0, column=1, columnspan=4, padx=(1, 150), pady=1, sticky="n")
        self.combobox_tittle = customtkinter.CTkLabel(self.tabview.tab("step 1"), text="Cuisine:",
                                                      font=('Century Gothic', 24))
        self.combobox_tittle.grid(row=0, column=0, padx=(705, 290), pady=0, sticky="nsew")

        self.recipe_tittle = customtkinter.CTkLabel(self.tabview.tab("step 1"), text="Recipe Name:",
                                                    font=('Century Gothic', 22))
        self.recipe_tittle.grid(row=2, column=0, padx=(220, 1), pady=60, sticky="nw")

        self.recipe_category = customtkinter.CTkLabel(self.tabview.tab("step 1"), text="Recipe Category:",
                                                      font=('Century Gothic', 22))
        self.recipe_category.grid(row=3, column=0, padx=(220, 1), pady=(50, 60), sticky="nw")

        self.difficulty_tittle = customtkinter.CTkLabel(self.tabview.tab("step 1"), text="Degree Of Difficulty:",
                                                        font=('Century Gothic', 22))
        self.difficulty_tittle.grid(row=4, column=0, padx=(220, 1), pady=(50, 60), sticky="nw")

        self.time_duration = customtkinter.CTkLabel(self.tabview.tab("step 1"), text="Recipe Duration:",
                                                    font=('Century Gothic', 22))
        self.time_duration.grid(row=5, column=0, padx=(220, 1), pady=(50, 40), sticky="nw")

        # Second Step Tittles
        self.second_step = customtkinter.CTkLabel(self.tabview.tab("step 2"),
                                                  text="Enter the ingredients of the recipe:",
                                                  font=('Century Gothic', 24))
        self.second_step.grid(row=0, column=0, columnspan=4, padx=(1, 400), pady=(25, 1), sticky="n")

        # Step 2
        # Ctk text box

        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("step 2"), width=1000, corner_radius=12,
                                                height=600, border_width=5, border_spacing=25,
                                                border_color=("#3673F8", "orange"),
                                                scrollbar_button_color=("#3673F8", "orange"), font=('Arial', 35))
        self.textbox.grid(row=1, column=1, padx=(250, 1), pady=(60, 1), sticky="nsew")
        self.textbox.insert("0.0", "A recipe has no soul.\nYou, as the cook, must bring soul to the recipe!")

        # Bind the <FocusIn> event to the text box
        self.textbox.bind("<FocusIn>", self.clear_text)

        # step 3

        # Tittle
        self.third_step = customtkinter.CTkLabel(self.tabview.tab("step 3"),
                                                 text="Enter the recipe steps:",
                                                 font=('Century Gothic', 24))
        self.third_step.grid(row=0, column=0, columnspan=4, padx=(1, 550), pady=(25, 1), sticky="n")

        # Inside Tab Frame

        self.tab_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("step 3"), height=565,
                                                          scrollbar_button_hover_color="#3786D9",
                                                          width=970, corner_radius=12, border_width=5,
                                                          border_color=("#3673F8", "orange",)
                                                          )
        self.tab_frame.grid(row=1, column=1, padx=(250, 1), pady=(60, 1), sticky="nsew")
        self.tab_frame.grid_columnconfigure(0, weight=1)
        self.tab_frame.grid_rowconfigure(3, weight=1)

        # Inside Bar Tittles

        self.third_step = customtkinter.CTkLabel(self.tab_frame,
                                                 text="Use slider for number of steps:",
                                                 font=('Century Gothic', 24))
        self.third_step.grid(row=0, column=0, columnspan=4, padx=(25, 1), pady=(150, 50), sticky="nsew")

        # Slider
        self.slider = customtkinter.CTkSlider(self.tab_frame, from_=0, to=30, progress_color="orange", width=400,
                                              height=18, border_width=1)

        self.slider.grid(row=2, column=0, padx=(300, 1), pady=1, sticky="nw")
        self.slider.bind("<ButtonRelease-1>",
                         self.update_count)  # bind the slider to a function to update the count label
        self.slider.set(0)

        self.slider_count = customtkinter.CTkLabel(self.tab_frame, text="0",
                                                   font=('Arial', 18,))  # create the label to display the count
        self.slider_count.grid(row=2, column=1, pady=(1, 50))
        self.slider.bind("<B1-Motion>", self.update_count)

        # Apply Steps Button
        self.slider_button = customtkinter.CTkButton(self.tab_frame, text="Apply Steps",
                                                     width=150, border_width=0, corner_radius=8,
                                                     font=('Arial', 13, 'bold'), command=self.create_text_boxes)
        self.slider_button.grid(row=5, column=0, padx=(415, 1), pady=(1, 50), sticky="w")

    def create_text_boxes(self):

        # We use the value of slider
        slider_value = int(self.slider_count.cget('text'))

        # Check if the slider count is 0
        if slider_value == 0:
            # If count is 0, hide the extra titles
            self.hide_extra_titles()
        else:
            # If count is non-zero, show the extra titles
            self.show_extra_titles()

        widgets_to_remove = self.step_entry_boxes + self.subtract_button_timers + self.timers + self.add_button_timers + self.step_message_array + self.step_title_boxes
        text_boxes_counter = 0
        # Remove old textboxes
        for widget in widgets_to_remove:
            widget.destroy()
            if widget in self.timers:
                self.timers.remove(widget)
            if widget in self.step_entry_boxes:
                self.step_entry_boxes.remove(widget)
            if widget in self.subtract_button_timers:
                self.subtract_button_timers.remove(widget)
            if widget in self.add_button_timers:
                self.add_button_timers.remove(widget)
            if widget in self.step_message_array:
                self.step_message_array.remove(widget)
            if widget in self.step_title_boxes:
                self.step_title_boxes.remove(widget)

        number_of_rec = int(self.slider.get())

        # Create new textboxes
        for i in range(number_of_rec):
            text_boxes_counter += 1
            textbox = customtkinter.CTkEntry(self.tab_frame, width=830, font=('Arial', 12), height=100)
            textbox.grid(row=8 + i, column=0, columnspan=5, pady=(20, 20), padx=(1, 1))

            title_textbox = customtkinter.CTkEntry(self.tab_frame, width=300, font=('Arial', 12), height=50,
                                                   corner_radius=18,
                                                   placeholder_text=f"        "
                                                                    f"        "
                                                                    f"Please enter the title of {i + 1} step:")
            title_textbox.grid(row=8 + i, column=0, columnspan=5, pady=(50, 300), padx=(20, 1))

            step_message = customtkinter.CTkLabel(self.tab_frame, text=f"Please enter the {i + 1} step:",
                                                  font=('Arial', 14))
            step_message.grid(row=8 + i, column=0, padx=(1, 100), pady=(1, 130), sticky="w")
            subtract_button_third_step = customtkinter.CTkButton(self.tab_frame, text="-", width=100 - 6, height=32 - 6,
                                                                 command=lambda index=i: self.subtract_button_callback(
                                                                     index))
            subtract_button_third_step.grid(row=8 + i, column=0, padx=(1, 170), pady=(250, 1))

            entry_third_step = customtkinter.CTkEntry(self.tab_frame, width=180 - (2 * 32), height=32 - 6,
                                                      border_width=0)

            entry_third_step.grid(row=8 + i, column=0, padx=(40, 1), pady=(250, 1))
            entry_third_step.insert(0, f"          0:00")

            add_button_third_step = customtkinter.CTkButton(self.tab_frame, text="+", width=100 - 6, height=32 - 6,
                                                            command=lambda index=i: self.add_button_callback(index))
            add_button_third_step.grid(row=8 + i, column=0, padx=(228, 1), pady=(250, 1))
            # default value

            self.timers.append(entry_third_step)
            self.subtract_button_timers.append(subtract_button_third_step)
            self.add_button_timers.append(add_button_third_step)
            self.step_entry_boxes.append(textbox)
            self.step_message_array.append(step_message)
            self.step_title_boxes.append(title_textbox)
            self.counter_of_text_boxes = text_boxes_counter

    def show_extra_titles(self):
        if self.extra_title is None:
            # Create the extra title labels
            self.extra_title = customtkinter.CTkLabel(self.tab_frame,
                                                      text="Enter the steps below:",
                                                      font=('Century Gothic', 24))
            self.extra_title.grid(row=6, column=0, columnspan=4, padx=(17, 1), pady=(1, 1), sticky="nsew")
            self.extra_title2 = customtkinter.CTkLabel(self.tab_frame,
                                                       text="Use timers for the duration of each step:",
                                                       font=('Century Gothic', 12))
            self.extra_title2.grid(row=7, column=0, columnspan=4, padx=(1, 1), pady=(1, 1), sticky="nsew")

    def hide_extra_titles(self):
        if self.extra_title is not None:
            # Hide the extra title labels
            self.extra_title.grid_forget()
            self.extra_title2.grid_forget()
            self.extra_title = None
            self.extra_title2 = None

    def add_button_callback(self, index):
        if self.command is not None:
            self.command()
        self.change_spinbox_value(self.timers[index], self.step_size)
        self.current_timer_index = index

    def subtract_button_callback(self, index):
        if self.command is not None:
            self.command()
        self.change_spinbox_value(self.timers[index], -self.step_size)
        self.current_timer_index = index

    def change_spinbox_value(self, entry_third_step, increment):
        try:
            current_value = entry_third_step.get()
            hours, minutes = map(int, current_value.split(':'))
            current_time = timedelta(hours=hours, minutes=minutes)
            new_time = current_time + timedelta(minutes=increment)

            # Ensure that the time will be equal or higher of 00:00
            if new_time < timedelta():
                new_time = timedelta()

            hours, minutes = divmod(new_time.seconds // 60, 60)
            formatted_time = f"{hours:11}:{minutes:02}"

            entry_third_step.delete(0, "end")
            entry_third_step.insert(0, formatted_time)
        except ValueError:
            pass

    def step1_time_changer(self, increment):
        try:
            current_value = self.time_displayer.get()
            hours, minutes = map(int, current_value.split(':'))
            current_time = timedelta(hours=hours, minutes=minutes)
            new_time = current_time + timedelta(minutes=increment)

            # Ensure that the time will be equal or higher of 00:00
            if new_time < timedelta():
                new_time = timedelta()

            hours, minutes = divmod(new_time.seconds // 60, 60)
            formatted_time = f"{hours:35}:{minutes:02}"

            self.time_displayer.delete(0, "end")
            self.time_displayer.insert(0, formatted_time)
        except ValueError:
            pass

    def step1_add(self):
        if self.command is not None:
            self.command()
            self.step1_time_changer(self.step_size)

    def step1_subtract(self):
        if self.command is not None:
            self.command()
            self.step1_time_changer(-self.step_size)

    def update_count(self, event):
        # update the count label with the current slider value

        self.slider_count.configure(text="{:01d}".format(int(self.slider.get())))  # format counter value

    def clear_text(self, event):
        if self.textbox.get("1.0",
                            "end-1c") == "A recipe has no soul.\nYou, as the cook, must bring soul to the recipe!":
            self.textbox.delete("1.0", "end")

    def display_categories(self, event):
        selected_cuisine = self.cuisine_box.get().strip()

        categories = []

        if selected_cuisine == "Chinese":
            categories = self.chinese_categories
        elif selected_cuisine == "Mexican":
            categories = self.mexican_categories
        elif selected_cuisine == "Mediterranean":
            categories = self.mediterranean_categories
        elif selected_cuisine == "Thai":
            categories = self.thai_categories
        elif selected_cuisine == "Arabic":
            categories = self.arabic_categories

        # Clear the old categories from category_box
        self.category_box.set(f"{'Choose Category':>48}")
        # Set the categories as the values of category_box combobox
        self.category_box.configure(values=categories)

    def return_to_menu(self):
        self.main_frame.destroy()
        self.outside_frame.destroy()
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.buttons_frame.grid()
        self.exit_button.grid(row=5, column=2, padx=0, pady=0)
        self.parent.title("Let's Cook-Menu")

    def save_registration(self):
        if self.Recipe_name.get() == "":
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Recipe name cannot be empty.")
        elif self.textbox.get('1.0', 'end-1c') == "" \
                or self.textbox.get('1.0', 'end-1c') == "A recipe has no soul.\nYou," \
                                                        " as the cook, must bring soul to the recipe!":
            # Display message to user that textbox is empty
            messagebox.showerror("Error", "Ingredients cannot be empty.")
            # Special string arguments used to represent the starting and ending positions of a text widget's content.
        elif self.cuisine_box.get() == f"{'Choose Cuisine':>40}":
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Recipe Cuisine cannot be empty.")
        elif self.category_box.get() == f"{'Choose Category':>48}":
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Recipe Category cannot be empty.")

        elif self.difficulty_box.get() == f"{'Choose Level':>47}":
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Recipe Level cannot be empty.")

        elif self.time_displayer.get() == "                             0:00":
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Recipe Duration cannot be empty.")
        #  self.slider.set(0)
        elif self.slider.get() == 0:
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Steps cannot be zero.")

        else:
            for textbox in self.step_entry_boxes:
                if textbox.get() == "":
                    # Display message to user that textbox is empty
                    messagebox.showerror("Error", "Step cannot be empty.")
                    return  # Stop execution if any textbox is empty

            # Check for empty title text boxes
            for title_textbox in self.step_title_boxes:
                if title_textbox.get() == "":
                    # Display message to user that title textbox is empty
                    messagebox.showerror("Error", "Step Title  cannot be empty.")
                    return  # Stop execution if any title textbox is empty

            for timer in self.timers:
                if timer.get() == "" or timer.get() == "          0:00":
                    # Display message to user that title textbox is empty
                    messagebox.showerror("Error", "Step Timer cannot be zero.")
                    return

            cursor.execute(
                "INSERT INTO Recipe (name,cuisine, category , difficulty , duration ,ingredients) VALUES(?, ?, ?, ?, ?, ?)",
                (self.Recipe_name.get(), self.cuisine_box.get().strip(), self.category_box.get().strip(),
                 self.difficulty_box.get().strip(), str(self.time_displayer.get().strip()),
                 self.textbox.get("1.0", tkinter.END)))
            recipeId = cursor.lastrowid
            for counter in range(self.counter_of_text_boxes):
                cursor.execute("INSERT INTO STEP(title, instructions, time, recipeId) VALUES(?, ?, ?, ?)", (
                    self.step_title_boxes[counter].get(), self.step_entry_boxes[counter].get(),
                    str(self.timers[counter].get().strip()), recipeId))

            conn.commit()
            self.return_to_menu()
