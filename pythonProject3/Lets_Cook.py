from imports import *
import sqlite3
import textwrap
conn = sqlite3.connect("Recipes.db")
cursor = conn.cursor()


class Lets_Cook(customtkinter.CTk):
    def __init__(self, parent, center_frame, left_frame, recipeId):
        super().__init__()
        self.step_duration_label = None
        self.right_button = None
        self.numberOfStep = None
        self.left_button = None
        self.parent_class = parent
        self.left_frame = left_frame
        self.center_frame = center_frame
        self.recipeId = recipeId
        self.stepCounter = 1

        self.parent_class.title("Let's Cook")

        self.behind_frame = customtkinter.CTkFrame(self.parent_class, width=850, height=150)
        self.behind_frame.grid(row=0, column=0, columnspan=4, rowspan=5, sticky="nsew", padx=(1, 1), pady=(1, 1))
        self.behind_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.behind_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)

        self.main_frame = customtkinter.CTkFrame(self.behind_frame, width=900, corner_radius=20, height=80)
        self.main_frame.grid(row=0, column=1, columnspan=4, rowspan=5, sticky="nsew", padx=(50, 1), pady=(15, 15))
        self.main_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.main_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.tittle = customtkinter.CTkLabel(self.main_frame, text="Let's Give Soul To The Recipe", font=('Bold', 27))
        self.tittle.grid(row=0, column=0, columnspan=4, padx=(1, 10), pady=(10, 1), sticky="n")

        self.back_editing_button = customtkinter.CTkButton(self.main_frame, text="          ←  back          ",
                                                           width=70, height=30,
                                                           corner_radius=15,
                                                           command=self.back)

        self.back_editing_button.grid(row=5, column=0, padx=(1, 350), pady=(1, 1), sticky="s")

        self.information_frame = customtkinter.CTkScrollableFrame(self.main_frame, height=810,
                                                                  scrollbar_button_hover_color="#3786D9",
                                                                  width=10, corner_radius=12, border_width=5,
                                                                  border_color=("#3673F8", "orange",)
                                                                  )
        self.information_frame.grid(row=0, column=0, columnspan=3, rowspan=5, padx=(167, 165), pady=(50, 10),
                                    sticky="nsew")
        self.information_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.information_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)
        sql_query = "SELECT * FROM Step WHERE recipeId=?"
        cursor.execute(sql_query, (recipeId,))
        self.steps = cursor.fetchall()
        sql_query = "SELECT COUNT(*) FROM Step WHERE recipeId=?"
        cursor.execute(sql_query, (recipeId,))
        self.numberOfSteps = cursor.fetchone()
        sql_query = "SELECT * FROM Recipe WHERE recipeId=?"
        cursor.execute(sql_query, (recipeId,))
        recipe = cursor.fetchall()
        self.character_limit = 35  # Define the number of characters to limit

        self.recipe_name_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Recipe Name: {textwrap.fill(recipe[0][1], self.character_limit)}",
            font=('Arial', 45),
            wraplength=600,
            justify="left",
            width=60
        )
        self.recipe_name_label.grid(row=0, column=1, padx=(200, 1), pady=(70, 40), sticky="w")

        self.wrapped_ingredients = textwrap.fill(recipe[0][6], self.character_limit)
        lines = self.wrapped_ingredients.split('\n')

        if len(lines) > 1:
            for i in range(1, len(lines)):
                lines[i] = '\t  ' + lines[i]

        self.wrapped_ingredients_modified = '\n'.join(lines)

        self.ingredients_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Ingredients: {self.wrapped_ingredients_modified}",
            font=('Arial', 45),
            justify="center",
            width=60
        )
        self.ingredients_label.grid(row=1, column=1, padx=(200, 1), pady=(120, 150), sticky="w")

        self.duration_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Recipe Duration: {textwrap.fill(recipe[0][5], self.character_limit)}",
            font=('Arial', 45),
            wraplength=600,
            justify="left",
            width=60
        )
        self.duration_label.grid(row=2, column=1, padx=(200, 1), pady=10, sticky="w")

        self.img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\image.ico")
        self.photo = customtkinter.CTkImage(self.img)
        self.start_button = customtkinter.CTkButton(self.information_frame, text="Let's Start", image=self.photo,
                                                    font=('Arial', 18, 'bold'),
                                                    height=35
                                                    , width=500, corner_radius=100, command=self.start)
        self.start_button.grid(row=6, column=1, sticky="w", pady=(150, 1), padx=(450, 1),)

        self.progressbar = customtkinter.CTkProgressBar(self.main_frame, orientation="horizontal", height=18,
                                                        width=600)
        self.progressbar.grid(row=7, column=1, padx=(80, 650), pady=(1, 15),
                              sticky="nsew")

        self.progress_tittle = customtkinter.CTkLabel(self.main_frame, text="Recipe Progress", font=('Bold', 24))
        self.progress_tittle.grid(row=5, column=1, padx=(130, 670), pady=(1, 5),
                                  sticky="nsew")

    def start(self):
        # Remove the start button
        self.start_button.grid_remove()
        self.stepCounter = 1
        self.numberOfStep = 0
        self.content_label.configure(text="")
        self.content_label.configure(text="Number of steps: " + str(1) + "\n" +
                                          "Title: " + str(self.steps[self.numberOfStep][1]) + "\n" +
                                          "Instructions: " + str(self.steps[self.numberOfStep][2]) + "\n" +
                                          "Duration: " + str(self.steps[self.numberOfStep][3]))

        self.step_duration_label = customtkinter.CTkLabel(
            self.information_frame,
            text=f"Step Duration: {textwrap.fill(self.steps[self.numberOfStep][3], self.character_limit)}",
            font=('Arial', 45),
            wraplength=600,
            justify="left",
            width=60
        )
        self.step_duration_label.grid(row=2, column=1, padx=(200, 1), pady=10, sticky="w")

        self.recipe_name_label.configure(text=f"Number of steps:  {1}")
        self.ingredients_label.configure(text=f"Title: {self.steps[self.numberOfStep][1]}")
        self.duration_label.configure(text=f"Instructions:   {self.steps[self.numberOfStep][2]}")
        # Create and place the new buttons
        self.right_button = customtkinter.CTkButton(self.main_frame, text="     Next Step    ",
                                                    font=('Arial', 18, 'bold'),
                                                    height=27, width=30, corner_radius=100, command=self.nextStep)
        self.right_button.grid(row=1, column=1, sticky="e", pady=(80, 1), padx=(1, 1))

        self.left_button = customtkinter.CTkButton(self.main_frame, text=" Previous Step ",
                                                   font=('Arial', 18, 'bold'),
                                                   height=27, width=30, corner_radius=100, command=self.previousStep)
        self.left_button.grid(row=1, column=0, sticky="w", pady=(80, 1), padx=(1, 1))

    def nextStep(self):
        self.stepCounter += 1
        self.numberOfStep += 1
        if self.stepCounter > self.numberOfSteps[0]:
            self.showLastStep()
            self.stepCounter = self.numberOfSteps[0]
            self.numberOfStep = self.numberOfSteps[0] - 1
            return False

        self.content_label.configure(text="")
        self.content_label.configure(text="Number of steps: " + str(self.stepCounter) + "\n" +
                                          "Title: " + str(self.steps[self.numberOfStep][1]) + "\n" +
                                          "Instructions: " + str(self.steps[self.numberOfStep][2]) + "\n" +
                                          "Duration: " + str(self.steps[self.numberOfStep][3]))

    def showLastStep(self):
        self.content_label.configure(text="")
        self.content_label.configure(text="Number of steps: " + str(self.numberOfSteps[0]) + "\n" +
                                          "Title: " + str(self.steps[self.numberOfSteps[0] - 1][1]) + "\n" +
                                          "Instructions: " + str(self.steps[self.numberOfSteps[0] - 1][2]) + "\n" +
                                          "Duration: " + str(self.steps[self.numberOfSteps[0] - 1][3]))

    def showFirstStep(self):
        self.content_label.configure(text="")
        self.content_label.configure(text="Number of steps: " + str(1) + "\n" +
                                          "Title: " + str(self.steps[0][1]) + "\n" +
                                          "Instructions: " + str(self.steps[0][2]) + "\n" +
                                          "Duration: " + str(self.steps[0][3]))

    def previousStep(self):
        self.stepCounter -= 1
        self.numberOfStep -= 1
        if self.stepCounter < 1:
            self.showFirstStep()
            self.stepCounter = 1
            self.numberOfStep = 0
            return False
        self.content_label.configure(text="")
        self.content_label.configure(text="Number of step: " + str(self.stepCounter) + "\n" +
                                          "Title: " + str(self.steps[self.numberOfStep][1]) + "\n" +
                                          "Instructions: " + str(self.steps[self.numberOfStep][2]) + "\n" +
                                          "Duration: " + str(self.steps[self.numberOfStep][3]))

    def back(self):

        self.behind_frame.destroy()
        self.main_frame.destroy()
        self.center_frame.grid()
        self.left_frame.grid()
        self.parent_class.title("Let's Cook-Recipe Search")
