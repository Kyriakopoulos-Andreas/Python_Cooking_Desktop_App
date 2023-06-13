from imports import *
import sqlite3
import textwrap
conn = sqlite3.connect("Recipes.db")
cursor = conn.cursor()


class Lets_Cook(customtkinter.CTk):
    def __init__(self, parent, center_frame, left_frame, recipeId):
        super().__init__()
        # Αρχικοποιήσεις
        self.number_of_step_label = None
        self.instructions_label = None
        self.step_title_label = None
        self.step_duration_label = None
        self.right_button = None
        self.numberOfStep = None
        self.left_button = None
        self.parent_class = parent
        self.left_frame = left_frame
        self.center_frame = center_frame
        self.recipeId = recipeId
        self.stepCounter = 1

        self.parent_class.title("Let's Cook")  # Αλλαγή επικεφαλίδας προγράμματος

        # Δημιουργία του πίσω frame
        self.behind_frame = customtkinter.CTkFrame(self.parent_class, width=850, height=150)
        self.behind_frame.grid(row=0, column=0, columnspan=4, rowspan=5, sticky="nsew", padx=(1, 1), pady=(1, 1))
        self.behind_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.behind_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)

        # Δημιουργία main frame
        self.main_frame = customtkinter.CTkFrame(self.behind_frame, width=900, corner_radius=20, height=80)
        self.main_frame.grid(row=0, column=1, columnspan=4, rowspan=5, sticky="nsew", padx=(50, 1), pady=(15, 15))
        self.main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        # Τίτλος Παραθύρου
        self.tittle = customtkinter.CTkLabel(self.main_frame, text="Let's Give Soul To The Recipe", font=('Bold', 27))
        self.tittle.grid(row=0, column=0, columnspan=4, padx=(1, 10), pady=(10, 1), sticky="n")

        # Κουμπί επιστροφής στο μενού
        self.back_editing_button = customtkinter.CTkButton(self.main_frame, text="          ←  back          ",
                                                           width=70, height=30,
                                                           corner_radius=15,
                                                           command=self.back)

        self.back_editing_button.grid(row=5, column=0, padx=(1, 350), pady=(1, 1), sticky="s")

        # Δημιουργία Scrollable frame
        self.information_frame = customtkinter.CTkScrollableFrame(self.main_frame, height=810,
                                                                  scrollbar_button_hover_color="#3786D9",
                                                                  width=10, corner_radius=12, border_width=5,
                                                                  border_color=("#3673F8", "orange",)
                                                                  )
        self.information_frame.grid(row=0, column=0, columnspan=3, rowspan=5, padx=(167, 165), pady=(50, 10),
                                    sticky="nsew")
        self.information_frame.grid_rowconfigure(1, weight=1)
        self.information_frame.grid_columnconfigure(1, weight=1)
        sql_query = "SELECT * FROM Step WHERE recipeId=?"
        cursor.execute(sql_query, (recipeId,))
        self.steps = cursor.fetchall()
        sql_query = "SELECT COUNT(*) FROM Step WHERE recipeId=?"
        cursor.execute(sql_query, (recipeId,))
        self.numberOfSteps = cursor.fetchone()
        sql_query = "SELECT * FROM Recipe WHERE recipeId=?"
        cursor.execute(sql_query, (recipeId,))
        recipe = cursor.fetchall()

        self.character_limit = 35  # Όριο χαρακτήρων ενός string

        # Δημιουργία label για εμφάνιση του ονόματος της συνταγής με textwrap για έλεγχο αλλαγής γραμμής και σωστή
        # μορφοποίηση
        self.recipe_name_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Recipe Name: \n{textwrap.fill(recipe[0][1], self.character_limit)}",
            font=('Arial', 45),
            wraplength=600,
            justify="left",
            width=60
        )
        self.recipe_name_label.grid(row=0, column=1, padx=(1, 1), pady=(40, 100), sticky="nsew")

        # Μετά το όριο χαρακτήρων που ορίσαμε αλλάζουμε γραμμή και δημιουργούμε μια λίστα με τις γραμμές
        self.wrapped_ingredients = textwrap.fill(recipe[0][6], self.character_limit)
        lines = self.wrapped_ingredients.split('\n')
        self.wrapped_ingredients_modified = '\n'.join(lines)

        # Δημιουργούμε Label για την εμφάνιση των υλικών της συνταγής
        self.ingredients_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Ingredients: \n{self.wrapped_ingredients_modified}",
            font=('Arial', 45),
            justify="center",
            width=60
        )
        self.ingredients_label.grid(row=2, column=1, padx=(1, 1), pady=(80, 50), sticky="nsew")

        # Δημιουργούμε Label για την εμφάνιση της διάρκειας της συνταγής
        self.duration_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Recipe Duration: {textwrap.fill(recipe[0][5], self.character_limit)}",
            font=('Arial', 35),
            wraplength=600,
            justify="left",
            width=60
        )
        self.duration_label.grid(row=1, column=1, padx=(40, 1), pady=10, sticky="w")

        # Φορτώνουμε την εικόνα από τον δίσκο
        self.img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\image.ico")
        self.photo = customtkinter.CTkImage(self.img)

        # Δημιουργία του κουμπιού έναρξης της συνταγής και τοποθέτηση της εικόνας
        self.start_button = customtkinter.CTkButton(self.information_frame, text="Let's Start", image=self.photo,
                                                    font=('Arial', 18, 'bold'),
                                                    height=35
                                                    , width=500, corner_radius=100, command=self.start)
        self.start_button.grid(row=6, column=1, sticky="w", pady=(150, 1), padx=(450, 1),)
        # Δημιουργία μπάρας προόδου
        self.progressbar = customtkinter.CTkProgressBar(self.main_frame, orientation="horizontal", height=18,
                                                        width=600)

        self.progressbar.grid(row=7, column=1, padx=(80, 650), pady=(1, 15),
                              sticky="nsew")
        self.progressbar.set(0)
        # Δημιουργία Label για τον τίτλο του progressbar
        self.progress_tittle = customtkinter.CTkLabel(self.main_frame, text="Recipe Progress", font=('Bold', 24))
        self.progress_tittle.grid(row=5, column=1, padx=(130, 670), pady=(1, 5),
                                  sticky="nsew")

    def start(self):
        # Κάνουμε remove στα labels των στοιχείων της εισαγωγής
        self.start_button.grid_remove()
        self.ingredients_label.grid_remove()
        self.duration_label.grid_remove()
        self.ingredients_label.grid_remove()
        self.recipe_name_label.grid_remove()
        # Μετρητές για τον αριθμό των βημάτων
        self.stepCounter = 1
        self.numberOfStep = 0
        # Καλούμε τη συνάρτηση για να αυξήσουμε την μπάρα προόδου
        self.updateProgressBar()
        # Δημιουργία των κατάλληλων labels για την εμφάνιση του κάθε βήματος
        self.step_duration_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Step Duration: {self.steps[self.numberOfStep][3]}",
            font=('Arial', 35),
            wraplength=600,
            justify="left",
            width=60
        )
        self.step_duration_label.grid(row=2, column=1, padx=(30, 1), pady=10, sticky="w")

        self.step_title_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Title Of The Step \n{self.steps[self.numberOfStep][1]}",
            font=('Arial', 45),
            wraplength=600,
            justify="center",
            width=60
        )
        self.step_title_label.grid(row=0, column=1, padx=(1, 1), pady=(40, 100), sticky="nsew")


        self.number_of_step_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Number Of Step: {1}",
            font=('Arial', 35),
            wraplength=600,
            justify="left",
            width=60
        )
        self.number_of_step_label.grid(row=1, column=1, padx=(30, 1), pady=10, sticky="w")

        self.instructions_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Step Instructions: \n{self.steps[self.numberOfStep][2]}",
            font=('Arial', 45),
            wraplength=600,
            justify="center",
            width=60
        )
        self.instructions_label.grid(row=3, column=1, padx=(1, 1), pady=(40, 100), sticky="nsew")

        # Δημιουργία δύο κουμπιών για την πλοήγηση στα βήματα της συνταγής
        self.right_button = customtkinter.CTkButton(self.main_frame, text="     Next Step    ",
                                                    font=('Arial', 18, 'bold'),
                                                    height=27, width=30, corner_radius=100, command=self.nextStep)
        self.right_button.grid(row=1, column=1, sticky="e", pady=(80, 1), padx=(1, 1))

        self.left_button = customtkinter.CTkButton(self.main_frame, text=" Previous Step ",
                                                   font=('Arial', 18, 'bold'),
                                                   height=27, width=30, corner_radius=100, command=self.previousStep)
        self.left_button.grid(row=1, column=0, sticky="w", pady=(80, 1), padx=(1, 1))

    def nextStep(self):  # Μέθοδος επόμενου βήματος
        self.stepCounter += 1
        self.numberOfStep += 1
        if self.stepCounter > self.numberOfSteps[0]:

            self.stepCounter = self.numberOfSteps[0]
            self.numberOfStep = self.numberOfSteps[0] - 1
            return False
        # Με τη μέθοδο configure εμφανίζουμε κάθε φορά το κάθε νέο βήμα
        self.updateProgressBar()
        self.number_of_step_label.configure(text=f"Number of steps:  {self.stepCounter}")
        self.step_title_label.configure(text=f"Title Of The Step \n {self.steps[self.numberOfStep][1]}")
        self.instructions_label.configure(text=f"Step Instructions: \n{self.steps[self.numberOfStep][2]}")
        self.step_duration_label.configure(text=f"Step Duration: {self.steps[self.numberOfStep][3]}", )

    def previousStep(self):  # Μέθοδος προηγούμενου βήματος
        self.stepCounter -= 1
        self.numberOfStep -= 1
        if self.stepCounter < 1:
            self.stepCounter = 1
            self.numberOfStep = 0
            return False
        # Καλούμε τη συνάρτηση για να μειώσουμε την μπάρα προόδου
        self.updateProgressBar()
        self.number_of_step_label.configure(text=f"Number of steps:  {self.stepCounter}")
        self.step_title_label.configure(text=f"Title Of The Step \n{self.steps[self.numberOfStep][1]}")
        self.instructions_label.configure(text=f"Step Instructions: \n{self.steps[self.numberOfStep][2]}")
        self.step_duration_label.configure(text=f"Step Duration: {self.steps[self.numberOfStep][3]}", )

    def updateProgressBar(self):  # Η μέθοδος ενημερώνει την μπάρα προόδου της συνταγής
        total_steps = self.numberOfSteps[0]  # Ο συνολικός αριθμός βημάτων της συνταγής
        current_step = self.stepCounter  # Ο τρέχον αριθμός βήματος
        progress_value = current_step / total_steps  # Υπολογισμός προόδου συνταγής
        self.progressbar.set(progress_value)   # αυξομειώνουμε την μπάρα προόδου







    def back(self):    # Επιστροφή στο recipe search
        self.behind_frame.destroy()
        self.main_frame.destroy()
        self.center_frame.grid()
        self.left_frame.grid()
        self.parent_class.title("Let's Cook-Recipe Search")
