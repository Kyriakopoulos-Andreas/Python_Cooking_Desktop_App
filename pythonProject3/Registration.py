import tkinter

from imports import *
import sqlite3
import os
file_path = os.path.dirname(__file__)
conn = sqlite3.connect("Recipes.db")
#conn.execute("drop table Recipe")
#conn.execute("drop table Step")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Recipe(recipeId INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT,cuisine TEXT, category TEXT, difficulty TEXT, duration INTEGER,ingredients TEXT) ")
cursor.execute("CREATE TABLE IF NOT EXISTS Step(stepId INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, instructions TEXT, time INTEGER,recipeId INTEGER, FOREIGN KEY (recipeId) REFERENCES Recipe(recipeId)) ")
conn.commit()
total_minutes = 0
total_minutes1 = 0

class Registration(customtkinter.CTk):
    def __init__(self, parent_menu, photo_label, buttons_frame, exit_button):
        super().__init__()
        self.parent = parent_menu  # Δημιουργία μεταβλητή parent για αναφορά στον γονέα
        # Ορίζουμε τις νέες μεταβλητές που θα χρησιμοποιήσουμε για να αναφερθούμε στα αντικείμενα του Μενού
        self.photoLabel = photo_label
        self.buttons_frame = buttons_frame
        self.exit_button = exit_button
        # Αρχικοποιήσεις
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
        # Μεταβλητή για την αύξηση του χρόνου της διάρκειας της συνταγής και των βημάτων της
        self.step_size = 3
        self.parent.title("Let's Cook-Registration")  # Αλλαγή της επικεφαλίδας της εφαρμογής
        self.iconbitmap(str(file_path)+"\\logo\\image.ico")
        self.title("Let's Cook-Registration Recipe")
        # Δημιουργία του εξωτερικού frame που μπαίνει πάνω στο parent
        self.outside_frame = customtkinter.CTkFrame(self.parent, height=600)
        self.outside_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15),
                             sticky="nsew")
        self.outside_frame.grid_rowconfigure(4, weight=1)  # Ορίζουμε το διάγραμμα του Frame σε γραμμές στήλες
        self.outside_frame.grid_columnconfigure(4, weight=0)
        # Δημιουργία main frame πάνω στο outside frame
        self.main_frame = customtkinter.CTkFrame(self.outside_frame, width=2000, corner_radius=20, height=80)
        self.main_frame.grid(row=0, column=1, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15),
                             sticky="nsew")
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)  # Ορίζουμε το διάγραμμα του Frame σε γραμμές στήλες
        self.main_frame.grid_columnconfigure((0, 1, 2, 4, 5), weight=1)
        # Δημιουργία Frame σε στιλ κουρτίνας, και ορισμός ονομάτων του κάθε παραθύρου
        self.tabview = customtkinter.CTkTabview(self.main_frame, border_width=5, corner_radius=30, width=1550)
        self.tabview.grid(row=0, column=1, rowspan=3, columnspan=4, padx=(10, 160), pady=(20, 20), sticky="nsew")
        self.tabview.add("step 1")
        self.tabview.add("step 2")
        self.tabview.add("step 3")
        # Δημιουργία διαγράμματος για το κάθε step με γραμμές και στήλες
        for tab_name in ["step 1", "step 2", "step 3"]:
            tab_frame = self.tabview.tab(tab_name)
            tab_frame.grid_columnconfigure(0, weight=0)
            tab_frame.grid_columnconfigure(1, weight=0)
            tab_frame.grid_rowconfigure(0, weight=0)
            tab_frame.grid_rowconfigure(1, weight=0)

        # Κουμπί για αποθήκευση συνταγής
        self.Save_Button = customtkinter.CTkButton(self.main_frame, text="Save Recipe", font=('Arial', 13, 'bold'),
                                                   command=self.save_registration, corner_radius=20)
        self.Save_Button.grid(row=3, column=2,pady=(1, 15), padx=(1, 165), sticky="nsew")
        # Κουμπί για επιστροφή στο Μενού
        self.Back_Button = customtkinter.CTkButton(self.main_frame, text="←  back ", font=('Arial', 13, 'bold'),
                                                   height=27, width=130, corner_radius=7, command=self.return_to_menu)
        self.Back_Button.grid(row=0, column=0, pady=(10, 1), padx=(10, 1), sticky="nw")
        # Δημιουργία widget για επιλογή Κουζίνας
        self.cuisine_box = customtkinter.CTkOptionMenu(self.tabview.tab("step 1"), width=400, height=25, corner_radius=10,
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
        self.cuisine_box.set(f"{'Choose Cuisine':>40}")  # Αρχικοποιούμε το option menu να δείχνει σε choose cuisine
        # Δημιουργία λιστών για τις κατηγορίες πιάτων της κάθε κουζίνας
        self.chinese_categories = ["BaoBan", "Noodles", "Sushi", "Ramen", "Soups", "Rice Dish", "Bowl",
                                   "Street Food"]
        self.mexican_categories = ["Tacos", "Burritos", "Enchiladas", "Fajitas", "Quesadilla", "Nachos"]
        self.italian_categories = ["Pizza", "Pasta", "Lasagna", "Risotto", "Dessert"]
        self.mediterranean_categories = ["Sea Food", "Meet", "Salad", "Vegetable", "Legumes", "Pie", "Pasta's",
                                         "Dessert"]
        self.thai_categories = ["Sea Food", "Soups", "Curries", "Pounded", "Noodles", "Rice Dish", "Salads"]
        self.arabic_categories = ["Shakshuka", "Lahmacun", "Falafel", "Hummus", "Kebab", "Salad", "Dessert"
                                  ]
        # Περνάμε τις λίστες μέσα σε μια άλλη λίστα για ευκολότερη διαχείριση
        self.format_categories = [
            self.chinese_categories,
            self.mexican_categories,
            self.italian_categories,
            self.mediterranean_categories,
            self.thai_categories,
            self.arabic_categories
        ]

        # Διατρέχουμε ένα βρόγχο για πιο όμορφη μορφοποίηση με τα σωστά κενά έτσι ώστε φαίνονται στη μέση του OptionMenu
        for category in self.format_categories:
            for i in range(len(category)):
                # Apply the formatting to each element in the category list
                category[i] = f"{category[i]:^82}"
        # Δημιουργία Option Menu widget για την επιλογή κατηγορίας πιάτου
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
        self.category_box.set(f"{'Choose Category':>48}")  # Αρχικοποίηση με Choose Category
        self.category_box.grid(row=3, column=0, padx=(420, 1), pady=(10, 1), sticky="s")

        # Δημιουργία Option Menu widget για την επιλογή δυσκολίας της συνταγής
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
        self.difficulty_box.set(f"{'Choose Level':>47}")  # Αρχικοποίηση με Choose Category
        # Δημιουργία Widget καταχώρισης για την εισαγωγή του ονόματος της συνταγής
        self.Recipe_name = customtkinter.CTkEntry(self.tabview.tab("step 1"),
                                                  placeholder_text="                    "
                                                                   "                     "
                                                                   "                      "
                                                                   "Enter Recipe Name", width=500,
                                                  height=25,
                                                  border_width=1, corner_radius=10)
        self.Recipe_name.grid(row=2, column=0, padx=(420, 1), pady=10, sticky="s")
        # Δημιουργία WIDGET τύπου Μετρητή χρόνου
        # Δημιουργία κουμπιών προσθαφαίρεσης χρόνου και σημείου προβολής του χρόνου
        self.subtract_button = customtkinter.CTkButton(self.tabview.tab("step 1"), text="-", width=100 - 6,
                                                       height=32 - 6,
                                                       command=self.step1_subtract)
        self.subtract_button.grid(row=7, column=0, padx=(274, 200), pady=3)

        self.time_var = tk.StringVar()
        self.time_displayer = customtkinter.CTkEntry(self.tabview.tab("step 1"), width=250, height=26, border_width=0,
                                                     textvariable=self.time_var, state="readonly")
        self.time_displayer.grid(row=7, column=0, padx=(620, 1), pady=1, sticky="w")

        self.add_button = customtkinter.CTkButton(self.tabview.tab("step 1"), text="+", width=100 - 6, height=32 - 6,
                                                  command=self.step1_add)
        self.add_button.grid(row=7, column=0, padx=(740, 1), pady=3)

        self.time_var.set("                                  0:00") # Αρχικοποίηση μετρητή στο 0

        # Τίτλοι και επικεφαλίδες STEP 1
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

        # Τίτλος STEP 2 για τα υλικά της συνταγής
        self.second_step = customtkinter.CTkLabel(self.tabview.tab("step 2"),
                                                  text="Enter the ingredients of the recipe:",
                                                  font=('Century Gothic', 24))
        self.second_step.grid(row=0, column=0, columnspan=4, padx=(1, 400), pady=(25, 1), sticky="n")

        # Δημιουργία Κουτιού καταχώρισης για εισαγωγή υλικών από τον χρήστη
        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("step 2"), width=1000, corner_radius=12,
                                                height=600, border_width=5, border_spacing=25,
                                                border_color=("#3673F8", "orange"),
                                                scrollbar_button_color=("#3673F8", "orange"), font=('Arial', 35))
        self.textbox.grid(row=1, column=1, padx=(250, 1), pady=(60, 1), sticky="nsew")
        self.textbox.insert("0.0", "A recipe has no soul.\nYou, as the cook, must bring soul to the recipe!")

        # Όταν ο χρήστης κάνει focus(Κάνει κλικ μέσα στο text box) το event πραγματοποιείτε και καλεί την συνάρτηση
        # Clear text η οποία σβήνει το περιεχόμενο του Text box
        self.textbox.bind("<FocusIn>", self.clear_text)

        # Τίτλος τρίτου βήματος
        self.third_step = customtkinter.CTkLabel(self.tabview.tab("step 3"),
                                                 text="Enter the recipe steps:",
                                                 font=('Century Gothic', 24))
        self.third_step.grid(row=0, column=0, columnspan=4, padx=(1, 550), pady=(25, 1), sticky="n")

        # Δημιουργία scrollable frame με slider
        self.tab_frame = customtkinter.CTkScrollableFrame(self.tabview.tab("step 3"), height=565,
                                                          scrollbar_button_hover_color="#3786D9",
                                                          width=970, corner_radius=12, border_width=5,
                                                          border_color=("#3673F8", "orange",)
                                                          )
        self.tab_frame.grid(row=1, column=1, padx=(250, 1), pady=(60, 1), sticky="nsew")
        self.tab_frame.grid_columnconfigure(0, weight=1)
        self.tab_frame.grid_rowconfigure(3, weight=1)

        # Τίτλος του scrollable frame
        self.third_step = customtkinter.CTkLabel(self.tab_frame,
                                                 text="Use slider for number of steps:",
                                                 font=('Century Gothic', 24))
        self.third_step.grid(row=0, column=0, columnspan=4, padx=(25, 1), pady=(150, 50), sticky="nsew")

        # Δημιουργία Slider για την επιλογή βημάτων από τον χρήστη
        self.slider = customtkinter.CTkSlider(self.tab_frame, from_=0, to=30, progress_color="orange", width=400,
                                              height=18, border_width=1)

        self.slider.grid(row=2, column=0, padx=(300, 1), pady=1, sticky="nw")
        self.slider.bind("<ButtonRelease-1>",
                         self.update_count)
        self.slider.set(0)  # Αρχικοποιούμε την τιμή του slider σε 0

        self.slider_count = customtkinter.CTkLabel(self.tab_frame, text="0",
                                                   font=('Arial', 18,))  # create the label to display the count
        self.slider_count.grid(row=2, column=1, pady=(1, 50))
        # Όσο ο χρήστης κρατάει παρατεταμένα το αριστερό κουμπί του ποντικιού η συνάρτηση update count συνδέετε με τον
        # slider και αυξομειώνει τα βήματα τα οποία προβάλλονται στο slider count label
        self.slider.bind("<B1-Motion>", self.update_count)

        # Κουμπί για τη δημιουργία των βημάτων
        self.slider_button = customtkinter.CTkButton(self.tab_frame, text="Apply Steps",
                                                     width=150, border_width=0, corner_radius=8,
                                                     font=('Arial', 13, 'bold'), command=self.create_text_boxes)
        self.slider_button.grid(row=5, column=0, padx=(415, 1), pady=(1, 50), sticky="w")

    def create_text_boxes(self):

        # Κρατάμε τα βήματα που προβάλλονται στο slider count σε μια μεταβλητή
        slider_value = int(self.slider_count.cget('text'))

        # Χρησιμοποιούμε την τιμή για να κρύψουμε ή να εμφανίσουμε τους έξτρα τίτλους που δημιουργούνται
        # Καλούμε τις κατάλληλες συναρτήσεις
        if slider_value == 0:
            # If count is 0, hide the extra titles
            self.hide_extra_titles()
        else:
            # If count is non-zero, show the extra titles
            self.show_extra_titles()
        # Κρατάμε όλα τα widget σε μια μεταβλητή για να τα διατρέχουμε όλα μαζί
        widgets_to_remove = self.step_entry_boxes + self.subtract_button_timers + self.timers + self.add_button_timers + self.step_message_array + self.step_title_boxes
        text_boxes_counter = 0  # Μετρητής βημάτων

        for widget in widgets_to_remove: # Διατρέχουμε και καταστρέφουμε τα widgets
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

        number_of_rec = int(self.slider.get())  # Κρατάμε την τιμή του slider

        # Δημιουργούμε τα βήματα σύμφωνα με τη με την επιλογή του χρήστη (μέσω της μεταβλητής)
        for i in range(number_of_rec):
            text_boxes_counter += 1 # Μετράμε τα βήματα κάθε φορά για τη σωστή ανανέωση τους
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
            entry_third_step.insert(0, "          0:00")
            entry_third_step.configure(state='readonly')

            add_button_third_step = customtkinter.CTkButton(self.tab_frame, text="+", width=100 - 6, height=32 - 6,
                                                            command=lambda index=i: self.add_button_callback(index))
            add_button_third_step.grid(row=8 + i, column=0, padx=(228, 1), pady=(250, 1))

            # Προσθέτουμε τα widgets σε πίνακες για καλύτερη διαχείριση
            self.timers.append(entry_third_step)
            self.subtract_button_timers.append(subtract_button_third_step)
            self.add_button_timers.append(add_button_third_step)
            self.step_entry_boxes.append(textbox)
            self.step_message_array.append(step_message)
            self.step_title_boxes.append(title_textbox)
            self.counter_of_text_boxes = text_boxes_counter

    def show_extra_titles(self):  # Μέθοδος που δημιουργεί τα extra titles όταν το κουμπί Apply steps πατηθεί
        if self.extra_title is None:  # Έαν τα titles έχουν δημιουργηθεί δεν ξανά δημιουργούνται με το πάτημα του button
            self.extra_title = customtkinter.CTkLabel(self.tab_frame,
                                                      text="Enter the steps below:",
                                                      font=('Century Gothic', 24))
            self.extra_title.grid(row=6, column=0, columnspan=4, padx=(17, 1), pady=(1, 1), sticky="nsew")
            self.extra_title2 = customtkinter.CTkLabel(self.tab_frame,
                                                       text="Use timers for the duration of each step:",
                                                       font=('Century Gothic', 12))
            self.extra_title2.grid(row=7, column=0, columnspan=4, padx=(1, 1), pady=(1, 1), sticky="nsew")

    def hide_extra_titles(self):# Μέθοδος που κρύβει τα extra titles όταν ο slider είναι στο 0 και το button ξανά
        # πατηθεί
        if self.extra_title is not None:
            # Hide the extra title labels
            self.extra_title.grid_forget()
            self.extra_title2.grid_forget()
            self.extra_title = None
            self.extra_title2 = None

    # Μέθοδος που προσθέτει χρόνο στον κατάλληλο μετρητή περνώντας ως όρισμα κάθε φορά στη συνάρτηση change_spinbox_value
    # Τον κατάλληλο times και το βήμα του χρόνου

    def add_button_callback(self, index):  # Μέθοδος που προσθέτει χρόνο στον κατάλληλο μετρητή
        self.change_spinbox_value(self.timers[index], self.step_size)
        global total_minutes
        total_minutes += 3
        if total_minutes > total_minutes1:
            messagebox.showerror("Error", "Ο χρόνος των βημάτων ξεπερνά τον συνολικό χρόνο εκτέλεσης της συνταγής.")
    # Μέθοδος που αφαιρεί χρόνο στον κατάλληλο μετρητή περνώντας ως όρισμα κάθε φορά στη συνάρτηση change_spinbox_value
    # Τον κατάλληλο times και το βήμα του χρόνου
    def subtract_button_callback(self, index):
        self.change_spinbox_value(self.timers[index], -self.step_size)
        # Update the cumulative sum
        global total_minutes
        total_minutes -= 3

    def change_spinbox_value(self, entry_third_step, increment):
        if entry_third_step.winfo_exists():
            try:
                current_value = entry_third_step.get()  # Παίρνει τον χρόνο και τον περνάει σε μια μεταβλητή
                hours, minutes = map(int, current_value.split(':')) # Κάνει split σε λεπτά και ώρες και επιστρέφει int
            # Δημιουργία αντικειμένου timedelta για τη σωστή αναπαράσταση του χρόνου
                current_time = timedelta(hours=hours, minutes=minutes)
                new_time = current_time + timedelta(minutes=increment)  # αυξάνει τα λεπτά

                # Έλεγχος για χρόνο μεγαλύτερο ή ίσο του μηδέν
                if new_time < timedelta():
                    new_time = timedelta()

                hours, minutes = divmod(new_time.seconds // 60, 60)  # Υπολογισμός των λεπτών και των ωρών του νέου χρόνου
                formatted_time = f"{hours:11}:{minutes:02}"  # Δημιουργία νέας σύμβολο σειράς με τα σωστά κενά

                entry_third_step.configure(state='normal')  # Enable the widget temporarily
                entry_third_step.delete(0, "end")
                entry_third_step.insert(0, formatted_time)
                entry_third_step.configure(state='readonly')  # Disable the widget again

            except ValueError:
                pass

    def step1_time_changer(self, increment):
        try:
            current_value = self.time_var.get()
            hours, minutes = map(int, current_value.strip().split(':'))
            current_time = timedelta(hours=hours, minutes=minutes)
            new_time = current_time + timedelta(minutes=increment)

            # Έλεγχος για χρόνο μεγαλύτερο ή ίσο του μηδέν
            if new_time < timedelta():
                new_time = timedelta()

            hours, minutes = divmod(new_time.seconds // 60, 60)
            formatted_time = f"{hours:35}:{minutes:02}"

            self.time_var.set(formatted_time)
        except ValueError:
            pass

    def step1_add(self):
            self.step1_time_changer(self.step_size)
            global total_minutes1
            total_minutes1 += 3

    def step1_subtract(self):
            self.step1_time_changer(-self.step_size)
            global total_minutes1
            total_minutes1 -= 3

    def update_count(self, event):
        # Ανανεώνει το label που δείχνει τα βήματα του counter

        self.slider_count.configure(text="{:01d}".format(int(self.slider.get())))  # format counter value

    def clear_text(self, event):  # Μόλις το event πραγματοποιηθεί διαγράφει το περιεχόμενο του text box
        if self.textbox.get("1.0",
                            "end-1c") == "A recipe has no soul.\nYou, as the cook, must bring soul to the recipe!":
            self.second_step.place_forget()
            self.textbox.delete("1.0", "end")
            self.textbox.unbind("<FocusIn>", None)
    # Μέθοδος για την ανανέωση της κάθε κατηγορίας ανάλογα με την επιλεγμένη κουζίνα
    def display_categories(self, event):
        selected_cuisine = self.cuisine_box.get().strip()  # Περνάμε την επιλογή κουζίνας σε μεταβλητή

        categories = [] # αρχικοποίηση πίνακα
        # Ανάλογα με την επιλογή κουζίνας περνάμε την κατάλληλη κατηγορία μέσα στο categories
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

        # Ανανεώνουμε το spinbox
        self.category_box.set(f"{'Choose Category':>48}")
        # Περνάμε τις κατάλληλες τιμές στην κατηγορία
        self.category_box.configure(values=categories)

    def return_to_menu(self):   # Επιστροφή στο μενού
        # Καταστρέφουμε τα frames,widgets,grids του registration και επαναφέρουμε του menu
        self.main_frame.destroy()
        for after_id in self.tk.eval('after info').split():
            self.after_cancel(after_id)
        self.outside_frame.destroy()
        for after_id in self.tk.eval('after info').split():
            self.after_cancel(after_id)
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.buttons_frame.grid()
        self.exit_button.grid(row=5, column=2, padx=0, pady=0)
        self.parent.title("Let's Cook-Menu")
        global total_minutes, total_minutes1
        total_minutes = 0
        total_minutes1 = 0


    def save_registration(self):
        # Αμυντικός για κενά πεδία με αναδυόμενα παράθυρα
        if self.Recipe_name.get() == "":
            messagebox.showerror("Error", "Recipe name cannot be empty.")

        elif self.textbox.get('1.0', 'end-1c') == "" \
                or self.textbox.get('1.0', 'end-1c') == "A recipe has no soul.\nYou," \
                                                        " as the cook, must bring soul to the recipe!":
            messagebox.showerror("Error", "Textbox cannot be empty.")

        elif self.cuisine_box.get() == f"{'Choose Cuisine':>40}":
            messagebox.showerror("Error", "Recipe Cuisine cannot be empty.")

        elif self.category_box.get() == f"{'Choose Category':>48}":
            messagebox.showerror("Error", "Recipe Category cannot be empty.")

        elif self.difficulty_box.get() == f"{'Choose Level':>47}":
            messagebox.showerror("Error", "Recipe Level cannot be empty.")

        elif self.time_displayer.get() == "                             0:00":
            messagebox.showerror("Error", "Recipe Duration cannot be empty.")

        elif self.slider.get() == 0:
            messagebox.showerror("Error", "Steps cannot be zero.")

        elif total_minutes > total_minutes1:
            messagebox.showerror("Error", "Step Timers cannot take more time than the total recipe time.")
            return

        else:
            for textbox in self.step_entry_boxes:
                if textbox.get() == "":
                    messagebox.showerror("Error", "Step cannot be empty.")
                    return

            for title_textbox in self.step_title_boxes:
                if title_textbox.get() == "":
                    messagebox.showerror("Error", "Step Title  cannot be empty.")
                    return

            for timer in self.timers:
                if timer.get() == "" or timer.get() == "          0:00":
                    messagebox.showerror("Error", "Step Timer cannot be zero.")
                    return

            cursor.execute("INSERT INTO Recipe (name,cuisine, category , difficulty , duration ,ingredients) VALUES(?, ?, ?, ?, ?, ?)",(self.Recipe_name.get(), self.cuisine_box.get().strip(),self.category_box.get().strip(),self.difficulty_box.get().strip(), str(self.time_displayer.get().strip()), self.textbox.get("1.0",tkinter.END)))
            recipeId  = cursor.lastrowid
            for counter in range(self.counter_of_text_boxes):
                cursor.execute("INSERT INTO STEP(title, instructions, time, recipeId) VALUES(?, ?, ?, ?)", (self.step_title_boxes[counter].get(), self.step_entry_boxes[counter].get(), str(self.timers[counter].get().strip()), recipeId))

            conn.commit()
            self.return_to_menu()

