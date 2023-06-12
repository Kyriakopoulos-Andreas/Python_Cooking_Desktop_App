import sqlite3
import tkinter

from imports import *
from Registration import Registration
import tkinter as tk
from tkinter import ttk
from Lets_Cook import Lets_Cook

conn = sqlite3.connect("Recipes.db")
cursor = conn.cursor()


class Recipe_search(customtkinter.CTk):
    def __init__(self, parent_menu, photo_label, buttons_frame, exit_button):
        super().__init__()
        self.counter_db = 0
        self.Recipe_name = None
        self.recipe = None
        self.values = None
        self.exit_editing = None
        self.parent = parent_menu
        self.photoLabel = photo_label
        self.buttons_frame = buttons_frame
        self.exit_button = exit_button
        # Set window size to full screen
        self.new_index = None
        self.new_step_button = None
        self.new_step_title = None
        self.steps_created = False
        self.text_box_visible = False
        self.text_box_created = False
        self.step_button_clicks = 0
        self.delete_buttons = []
        self.subtract_button_third_step = None
        self.step_message = None
        self.title_textbox = None
        self.textbox = None
        self.entry_third_step = None
        self.delete_step_photo = None
        self.delete_step_img = None
        self.add_button_third_step = None
        self.stepp_counter = None
        self.counter_of_text_boxes = None
        self.current_timer_index = None
        self.tab3_text_boxes = []
        self.subtract_button_timers = []
        self.timers = []
        self.add_button_timers = []
        self.step_message_array = []
        self.title_textbox_array = []
        self.ingredients_textbox = None
        self.steps_button = None
        self.steps_title = None
        self.ingredients_button = None
        self.ingredients_title = None
        self.entry = None
        self.step_size = 3
        self.add_button = None
        self.subtract_button = None
        self.time_duration = None
        self.recipe_title = None
        self.editing_title = None
        self.scrollable_frame = None
        self.save_changes_button = None
        self.editing_frame = None
        self.back = None
        self.search_photo = None
        self.search_img = None
        self.search_button = None
        self.registration_object = None
        self.category_box = None
        self.arabic_categories = None
        self.format_categories = None
        self.difficulty_box = None
        self.thai_categories = None
        self.mediterranean_categories = None
        self.italian_categories = None
        self.mexican_categories = None
        self.chinese_categories = None
        self.combobox = None
        self.stepp_counter = 0
        self.filtersOn = False

        self.steps_visible = False

        self.filter_counter = 0

        self.parent.title("Let's Cook-Recipe Search")

        # left frame
        self.left_frame = customtkinter.CTkFrame(self.parent, width=400, corner_radius=20)
        self.left_frame.grid(row=0, column=0, rowspan=5, columnspan=1, sticky="nsew", padx=(20, 1), pady=(20, 20))
        self.left_frame.grid_rowconfigure(4, weight=1)

        self.center_frame = customtkinter.CTkFrame(self.parent, width=850, corner_radius=20, height=80)
        self.center_frame.grid(row=0, column=1, columnspan=4, rowspan=5, sticky="nsew", padx=(3, 20), pady=(20, 20))
        self.center_frame.grid_rowconfigure(4, weight=1)
        self.center_frame.grid_columnconfigure(4, weight=1)

        self.bottom_frame = customtkinter.CTkFrame(self.center_frame, width=1500, corner_radius=20, height=80)
        self.bottom_frame.grid(row=6, column=1, columnspan=5, sticky="ew", padx=(8, 8), pady=(3, 8))
        self.bottom_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.inside_frame = customtkinter.CTkFrame(self.center_frame, width=1500, corner_radius=20, height=80)
        self.inside_frame.grid(row=0, column=1, columnspan=5, rowspan=5, sticky="nsew", padx=(8, 8), pady=(8, 5))
        self.inside_frame.grid_rowconfigure(4, weight=1)
        self.inside_frame.grid_columnconfigure(4, weight=1)

        self.left_inside_frame = customtkinter.CTkFrame(self.left_frame, width=400, corner_radius=20)
        self.left_inside_frame.grid(row=0, column=0, rowspan=5, columnspan=1, sticky="nsew", padx=(8, 8), pady=(8, 8))
        self.left_inside_frame.grid_rowconfigure((2, 3, 4), weight=1)
        self.left_inside_frame.grid_rowconfigure(1, weight=0)

        self.recipe_search_tittle = customtkinter.CTkLabel(self.left_inside_frame, text="Search for a recipe",
                                                           font=customtkinter.CTkFont(size=30, weight="bold"))
        self.recipe_search_tittle.grid(row=0, column=0, padx=(80, 80), pady=(20, 300), sticky="n")

        self.search_name = customtkinter.CTkEntry(self.left_inside_frame,
                                                  placeholder_text="                     "
                                                                   "                     "
                                                                   "Enter Recipe Name", width=400,
                                                  height=25,
                                                  border_width=1, corner_radius=10)
        self.search_name.grid(row=0, column=0, padx=(20, 20), pady=(100, 150), sticky="n")

        self.recipe_search_tittle = customtkinter.CTkLabel(self.left_inside_frame, text="Use filters to find a recipe",
                                                           font=customtkinter.CTkFont(size=20, weight="bold"))
        self.recipe_search_tittle.grid(row=0, column=0, padx=(80, 80), pady=(50, 1), sticky="ew")

        self.filter_button = customtkinter.CTkButton(self.left_inside_frame, text="Filters",
                                                     width=130, height=40, command=self.handle_filter_button)
        self.filter_button.grid(row=0, column=0, padx=0, pady=(150, 1), )

        self.back_button = customtkinter.CTkButton(self.left_inside_frame, text="←  back   ",
                                                   width=60, height=30, corner_radius=15, command=self.back_to_menu)
        self.back_button.grid(row=90, column=0, padx=0, pady=(50, 1), sticky="w")

        self.edit_img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\spoon.png")
        self.edit_img = self.edit_img.resize((24, 24))
        self.edit_photo = customtkinter.CTkImage(self.edit_img)

        self.editing_button = customtkinter.CTkButton(self.bottom_frame, text="Edit Recipe", image=self.edit_photo,
                                                      width=130, height=40, corner_radius=15, command=self.editing
                                                      )
        self.editing_button.grid(row=0, column=0, padx=(1, 10), pady=(30, 30), sticky="e")

        self.delete_img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\x.png")
        self.delete_img = self.delete_img.resize((24, 24))
        self.delete_photo = customtkinter.CTkImage(self.delete_img)

        self.delete_button = customtkinter.CTkButton(self.bottom_frame, text="Delete Recipe", image=self.delete_photo,
                                                     width=130, height=40, corner_radius=15, command=self.delete
                                                     )
        self.delete_button.grid(row=0, column=4, padx=(1, 10), pady=(30, 30), sticky="w")

        self.img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\chef.png")
        self.img = self.img.resize((24, 24))
        self.photo = customtkinter.CTkImage(self.img)

        self.cook_button = customtkinter.CTkButton(self.bottom_frame, text="Let's Cook", image=self.photo,
                                                   width=130, height=40, corner_radius=15,
                                                   command=self.lets_cook_window)
        self.cook_button.grid(row=0, column=2, padx=(1, 1), pady=(30, 30), sticky="nsew")

        self.search_img = Image.open(r"C:\Users\Admin\PycharmProjects\pythonProject3\logo\search.png")
        self.search_img = self.search_img.resize((24, 24))
        self.search_photo = customtkinter.CTkImage(self.search_img)

        self.search_button = customtkinter.CTkButton(self.left_inside_frame, text="Search", image=self.search_photo,
                                                     width=240, height=40, command=self.search_but)
        self.search_button.grid(row=3, column=0, padx=0, pady=(10, 1), )

        self.information_frame = customtkinter.CTkFrame(self.inside_frame, height=360,
                                                        width=670, border_width=3,
                                                        border_color=("#3673F8", "orange",)
                                                        )
        self.information_frame.grid(row=0, column=0, columnspan=7, rowspan=7,
                                    sticky="nsew")
        self.information_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.information_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.columns = ('id', 'recipe_name', 'cuisine', 'category', 'level')

        self.tree_view = ttk.Treeview(self.information_frame, columns=self.columns, selectmode='browse',
                                      show='headings')
        self.tree_view.grid(row=0, column=0, columnspan=8, rowspan=8, sticky="nsew", padx=(3, 3), pady=(3, 3))
        self.tree_view.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.tree_view.rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.tree_view.column('id', anchor='c', minwidth=1, width=50)  # Update column width for 'id'
        self.tree_view.column('recipe_name', anchor='c', minwidth=1, width=200)  # Update column width for 'recipe_name'
        self.tree_view.column('cuisine', anchor='c', minwidth=1, width=150)  # Update column width for 'cuisine'
        self.tree_view.column('category', anchor='c', minwidth=1, width=150)  # Update column width for 'category'
        self.tree_view.column('level', anchor='c', minwidth=1, width=100)  # Update column width for 'level'

        self.tree_view.heading('id', text='ID')
        self.tree_view.heading('recipe_name', text='Recipe Name')
        self.tree_view.heading('cuisine', text='Cuisine')
        self.tree_view.heading('category', text='Category')
        self.tree_view.heading('level', text='Level')

        # Insert items and values into tree view
        cursor.execute("SELECT * FROM Recipe")
        recipes = cursor.fetchall()

        for recipe in recipes:
            print(recipe[6])
            self.tree_view.insert("", "end", text="Item 1",
                                  values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))
        self.appearance_mode = ctk.get_appearance_mode()
        # Define colors based on appearance mode
        self.style = ttk.Style(self.tree_view)

        if self.appearance_mode == "Dark":
            self.style.theme_use("default")  # Set the 'default' theme for Treeview in dark mode
            self.treeview_backround = "#2a2d2e"
            self.treeview_foreground = "white"
            self.treeview_fieldbackground = "#343638"
            self.treeview_bordercolor = "#343638"

            self.treeview_heading_background = "#447183"
            self.treeview_heading_foreground = "white"
            self.style.map("Treeview.Heading",
                           background=[('active', '#3484F0')])
            self.style.map('Treeview', background=[('selected', '#22559b')])
            self.scrollbar_space = (40, 1)
            self.scrollbar_color = "#447183"



        elif self.appearance_mode == "Light":
            self.treeview_backround = "#D0D3D4"
            self.treeview_foreground = "#000000"
            self.treeview_fieldbackground = "#343638"
            self.treeview_bordercolor = "#343638"
            self.style.theme_use("vista")  # Set the 'clam' theme for Treeview in light mode

            self.treeview_heading_background = "#3484F0"
            self.treeview_heading_foreground = "#000000"
            self.style.map("Treeview.Heading",
                           background=[('active', '#00116E')])
            self.style.map('Treeview', background=[('selected', '#22559b')])
            self.scrollbar_space = (25, 1)
            self.scrollbar_color = "#3484F0"

        self.style.configure("Treeview",
                             background=self.treeview_backround,
                             foreground=self.treeview_foreground,
                             rowheight=25,
                             fieldbackground=self.treeview_fieldbackground,
                             bordercolor=self.treeview_bordercolor,
                             borderwidth=1, font=('Century Gothic', 12, 'bold'), )

        self.style.configure("Treeview.Heading",
                             background=self.treeview_heading_background,
                             foreground=self.treeview_heading_foreground,
                             borderwidth=7,
                             relief="flat", font=('Arial', 14, 'bold'))

        # Create vertical scrollbar for tree view
        self.scrollbar = customtkinter.CTkScrollbar(self.tree_view, corner_radius=6,
                                                    fg_color="#343638", height=2000, border_spacing=1,
                                                    button_hover_color=self.scrollbar_color)
        self.scrollbar.grid(row=0, column=6, sticky="ns", pady=self.scrollbar_space, padx=(50, 1))
        self.tree_view.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.tree_view.yview)

    def display_filters(self):

        self.combobox = customtkinter.CTkOptionMenu(self.left_inside_frame, width=300, height=30, corner_radius=10,
                                                    dropdown_hover_color="#A4A4A4", dynamic_resizing=False,
                                                    dropdown_font=('bold', 18), font=('Arial', 18, 'bold'),
                                                    command=self.display_categories,
                                                    values=[
                                                        f"{'Mediterranean':^42}",
                                                        f"{'Chinese':^45}",
                                                        f"{'Mexican':^45}",
                                                        f"{'Arabic':^45}",
                                                        f"{'Thai':^45}"])

        self.combobox.grid(row=1, column=0, padx=(1, 1), pady=(1, 20))

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
                category[i] = f"{category[i]:^40}"

        self.category_box = customtkinter.CTkOptionMenu(self.left_inside_frame,
                                                        width=300, height=30, corner_radius=10,
                                                        dropdown_hover_color="#A4A4A4", dynamic_resizing=False,
                                                        dropdown_font=('bold', 18), font=('Arial', 18, 'bold'),
                                                        values=[
                                                            f"{'Sea Food':^40}",
                                                            f"{'Meet':^40}",
                                                            f"{'Salad':^40}",
                                                            f"{'Vegetable':^40}",
                                                            f"{'Legumes':^40}",
                                                            f"{'Pie':^40}",
                                                            f"{'Pasta':^40}",
                                                            f"{'Dessert':^40}"])
        self.category_box.set(f"{'Choose Category':>27}")
        self.category_box.grid(row=2, column=0, padx=(20, 20), pady=(1, 100))

        # Bind the <<ComboboxSelected>> event to the display_categories method

        self.difficulty_box = customtkinter.CTkOptionMenu(self.left_inside_frame,
                                                          width=300, height=30, corner_radius=10,
                                                          dropdown_hover_color="#A4A4A4", dynamic_resizing=False,
                                                          dropdown_font=('bold', 18), font=('Arial', 18, 'bold'),
                                                          values=[
                                                              f"{'Easy':^42}",
                                                              f"{'Medium':^40}",
                                                              f"{'Difficult':^44}",
                                                          ], )
        self.difficulty_box.grid(row=2, column=0, pady=(100, 1))

    def handle_filter_button(self):
        self.filter_counter += 1
        if self.filter_counter % 2 == 0:

            self.combobox.destroy()
            self.category_box.destroy()
            self.difficulty_box.destroy()
            self.filtersOn = False

        else:
            self.filtersOn = True
            self.display_filters()

    def display_categories(self, event):
        selected_cuisine = self.combobox.get().strip()

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
        self.category_box.set(f"{'Choose Category':>27}")
        # Set the categories as the values of category_box combobox
        self.category_box.configure(values=categories)

    def back_to_menu(self):
        self.left_frame.destroy()
        self.center_frame.destroy()
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.buttons_frame.grid()
        self.exit_button.grid(row=5, column=2, padx=0, pady=0)
        self.parent.title("Let's Cook-Menu")

    def editing(self):
        selectedRow = self.tree_view.focus()
        if not selectedRow:
            return
        self.center_frame.grid_remove()
        self.parent.title("Let's Cook-Editing")
        self.left_frame.grid_remove()
        self.editing_frame = customtkinter.CTkFrame(self.parent, width=850, corner_radius=20, height=80)
        self.editing_frame.grid(row=0, column=1, columnspan=7, rowspan=5, sticky="nsew", padx=(20, 20), pady=(20, 20))
        self.editing_frame.grid_rowconfigure(4, weight=0)
        self.editing_frame.grid_columnconfigure(4, weight=0)

        self.editing_title = customtkinter.CTkLabel(self.editing_frame, text="Editing Recipe",
                                                    font=('Century Gothic', 24))
        self.editing_title.grid(row=0, column=1, columnspan=4, padx=(80, 1), pady=(10, 1), sticky="n")

        self.save_changes_button = customtkinter.CTkButton(self.editing_frame, text="Save Changes", width=70, height=35,
                                                           corner_radius=15,
                                                           command=self.save_changes)
        self.save_changes_button.grid(row=4, column=4, padx=0, pady=(50, 1), sticky="se")

        self.exit_editing = customtkinter.CTkButton(self.editing_frame, text="       ←  back       ", width=100,
                                                    height=35,
                                                    corner_radius=15,
                                                    command=self.exit)
        self.exit_editing.grid(row=4, column=1, padx=(1, 1560), pady=(50, 1), sticky="se")

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.editing_frame, height=840,
                                                                 scrollbar_button_hover_color="#3786D9",
                                                                 width=1730, corner_radius=12, border_width=5,
                                                                 border_color=("#3673F8", "orange",)
                                                                 )
        self.scrollable_frame.grid(row=0, column=1, padx=(50, 50), columnspan=4, rowspan=5,
                                   pady=(50, 50), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=0)
        self.scrollable_frame.grid_columnconfigure(1, weight=0)
        self.scrollable_frame.grid_columnconfigure(2, weight=0)
        self.scrollable_frame.grid_rowconfigure(3, weight=0)

        self.recipe_title = customtkinter.CTkLabel(self.scrollable_frame, text="Edit Recipe Name:",
                                                   font=('Century Gothic', 30))
        self.recipe_title.grid(row=2, column=0, padx=(350, 1), pady=60, sticky="nw")

        self.search_name = customtkinter.CTkEntry(self.scrollable_frame,
                                                  placeholder_text="                  "
                                                                   "                          "
                                                                   "                          "
                                                                   "                          "
                                                                   "Enter Recipe Name", width=700,
                                                  height=30,
                                                  border_width=1, corner_radius=10)
        self.search_name.grid(row=2, column=0, padx=(550, 1), pady=(150, 1), sticky="s")

        self.time_duration = customtkinter.CTkLabel(self.scrollable_frame, text="Edit Recipe Duration:",
                                                    font=('Century Gothic', 30))
        self.time_duration.grid(row=5, column=0, padx=(350, 1), pady=(50, 40), sticky="nw")

        self.subtract_button = customtkinter.CTkButton(self.scrollable_frame, text="-", width=100 - 6,
                                                       height=32 - 6,
                                                       command=self.step1_subtract)
        self.subtract_button.grid(row=7, column=0, padx=(20, 1), pady=8)

        self.entry = customtkinter.CTkEntry(self.scrollable_frame, width=500, height=26,
                                            border_width=0)
        self.entry.grid(row=7, column=0, padx=(680, 1), pady=8, sticky="w")

        self.add_button = customtkinter.CTkButton(self.scrollable_frame, text="+", width=100 - 6, height=32 - 6,
                                                  command=self.step1_add)
        self.add_button.grid(row=7, column=0, padx=(1058, 1), pady=8)

        self.ingredients_title = customtkinter.CTkLabel(self.scrollable_frame, text="Edit Recipe Ingredients:",
                                                        font=('Century Gothic', 30))
        self.ingredients_title.grid(row=8, column=0, padx=(350, 1), pady=(70, 72), sticky="nw")

        self.ingredients_button = customtkinter.CTkButton(self.scrollable_frame, text="Ingredients", width=280,
                                                          height=33,
                                                          corner_radius=15,
                                                          command=self.ingredients_text_box)
        self.ingredients_button.grid(column=0, row=8, padx=(1, 205), pady=(70, 72), sticky="se")

        self.steps_title = customtkinter.CTkLabel(self.scrollable_frame, text="Edit Recipe Steps:",
                                                  font=('Century Gothic', 30))
        self.steps_title.grid(row=10, column=0, padx=(350, 1), pady=(50, 1), sticky="nw")

        self.steps_button = customtkinter.CTkButton(self.scrollable_frame, text="Steps", width=280,
                                                    height=33,
                                                    corner_radius=15,
                                                    command=self.create_text_boxes)
        self.steps_button.grid(column=0, row=10, padx=(1, 205), pady=(10, 1), sticky="se")

        items = self.tree_view.item(selectedRow)
        self.values = items.get("values")
        sql_query = "SELECT * FROM Recipe WHERE recipeId =?"
        cursor.execute(sql_query, (self.values[0],))
        self.recipe = cursor.fetchall()
        self.search_name.insert(0, self.values[1])
        self.entry.insert(0, f"{' ':>68}" + str(self.recipe[0][5]))

    def create_text_boxes(self):

        if self.steps_visible:
            # Hide the steps
            for textbox in self.tab3_text_boxes:
                textbox.grid_forget()
            for button in self.subtract_button_timers:
                button.grid_forget()
            for button in self.add_button_timers:
                button.grid_forget()
            for message in self.step_message_array:
                message.grid_forget()
            for title_textbox in self.title_textbox_array:
                title_textbox.grid_forget()
            for delete_button in self.delete_buttons:
                delete_button.grid_forget()
            for timer in self.timers:
                timer.grid_forget()
            self.new_step_title.grid_forget()
            self.new_step_button.grid_forget()
            self.steps_visible = False
        else:
            # Show the steps
            for i, textbox in enumerate(self.tab3_text_boxes):
                textbox.grid(row=12 + i, column=0, pady=(150, 100), padx=(550, 1), sticky="w")
            for i, button in enumerate(self.subtract_button_timers):
                button.grid(row=12 + i, column=0, padx=(103, 1), pady=(350, 1))
            for i, button in enumerate(self.add_button_timers):
                button.grid(row=12 + i, column=0, padx=(985, 1), pady=(350, 1))
            for i, message in enumerate(self.step_message_array):
                message.grid(row=12 + i, column=0, padx=(350, 1), pady=(1, 130), sticky="w")
            for i, title_textbox in enumerate(self.title_textbox_array):
                title_textbox.grid(row=12 + i, column=0, pady=(100, 385), padx=(555, 1))
            for i, delete_button in enumerate(self.delete_buttons):
                delete_button.grid(row=12 + i, column=1, padx=(1, 1), pady=(40, 1), sticky="e")
            for i, timer in enumerate(self.timers):
                timer.grid(row=12 + i, column=0, padx=(543, 1), pady=(350, 1))

            self.new_step_title = customtkinter.CTkLabel(self.scrollable_frame, text="Step Addition:",
                                                         font=('Century Gothic', 30))
            self.new_step_title.grid(row=11, column=0, padx=(350, 1), pady=(50, 1), sticky="nw")

            self.new_step_button = customtkinter.CTkButton(self.scrollable_frame, text="Add Step", width=280,
                                                           height=33,
                                                           corner_radius=15,
                                                           command=self.add_new_step)
            self.new_step_button.grid(column=0, row=11, padx=(1, 205), pady=(1, 1), sticky="se")
            self.steps_visible = True
            # Create new textboxes
        if not self.steps_created:
            sql_query = "SELECT COUNT(stepId)FROM Step WHERE recipeId=?;"
            cursor.execute(sql_query, (self.values[0],))
            numberOfSteps = cursor.fetchall()
            for i, _ in enumerate(range(int(numberOfSteps[0][0]))):
                self.stepp_counter += 1
                self.textbox = customtkinter.CTkEntry(self.scrollable_frame, width=670, font=('Arial', 12), height=150)
                self.textbox.grid(row=12 + i, column=0, pady=(150, 100), padx=(550, 1), sticky="w")

                self.title_textbox = customtkinter.CTkEntry(self.scrollable_frame, width=400, font=('Arial', 12),
                                                            height=50,
                                                            corner_radius=18)
                self.title_textbox.grid(row=12 + i, column=0, pady=(100, 385), padx=(555, 1))

                self.step_message = customtkinter.CTkLabel(self.scrollable_frame,
                                                           text=f"Please edit the {i + 1} step:",
                                                           font=('bold', 18))
                self.step_message.grid(row=12 + i, column=0, padx=(350, 1), pady=(1, 130), sticky="w")
                self.subtract_button_third_step = customtkinter.CTkButton(self.scrollable_frame, text="-",
                                                                          width=100 - 6, height=32 - 6,
                                                                          command=lambda
                                                                              index=i: self.subtract_button_callback(
                                                                              index))
                self.subtract_button_third_step.grid(row=12 + i, column=0, padx=(103, 1), pady=(350, 1))

                self.entry_third_step = customtkinter.CTkEntry(self.scrollable_frame, width=350, height=32 - 6,
                                                               border_width=0)

                self.entry_third_step.grid(row=12 + i, column=0, padx=(543, 1), pady=(350, 1))


                self.add_button_third_step = customtkinter.CTkButton(self.scrollable_frame, text="+", width=100 - 6,
                                                                     height=32 - 6,
                                                                     command=lambda index=i: self.add_button_callback(
                                                                         index))
                self.add_button_third_step.grid(row=12 + i, column=0, padx=(985, 1), pady=(350, 1))

                self.delete_step_img = Image.open(r"C:\Users\Admin\Desktop\logo\x.png")
                self.delete_step_img = self.delete_img.resize((24, 24))
                self.delete_step_photo = customtkinter.CTkImage(self.delete_step_img)
                self.delete_button = customtkinter.CTkButton(self.scrollable_frame, text="", width=100 - 6,
                                                             height=32 - 6,
                                                             command=lambda index=i: self.delete_button_callback(index),
                                                             corner_radius=12, image=self.delete_step_photo)
                self.delete_button.grid(row=12 + i, column=1, padx=(1, 1), pady=(40, 1), sticky="e")
                self.delete_buttons.append(self.delete_button)
                # default value

                self.timers.append(self.entry_third_step)
                self.subtract_button_timers.append(self.subtract_button_third_step)
                self.add_button_timers.append(self.add_button_third_step)
                self.tab3_text_boxes.append(self.textbox)
                self.step_message_array.append(self.step_message)
                self.title_textbox_array.append(self.title_textbox)
                self.steps_visible = True
                self.steps_created = True

            selectedRecipe = self.recipe[0]
            sql_query = "SELECT * FROM Step WHERE recipeId =?"
            cursor.execute(sql_query, (selectedRecipe[0],))
            selectedSteps = cursor.fetchall()
            text_boxes_counter = 0
            for step in selectedSteps:
                self.title_textbox_array[text_boxes_counter].insert(tkinter.INSERT, step[1])
                self.tab3_text_boxes[text_boxes_counter].insert(tkinter.INSERT, step[2])
                self.timers[text_boxes_counter].insert(0, f"{' ':>50}" + str(step[3]))
                text_boxes_counter += 1

    def add_new_step(self):
        new_index = self.stepp_counter  # determine index of new step
        self.stepp_counter += 1

        # create new widgets for step
        self.textbox = customtkinter.CTkEntry(self.scrollable_frame, width=670, font=('Arial', 12), height=150)
        self.textbox.grid(row=1 + 12 + new_index, column=0, pady=(150, 100), padx=(550, 1), sticky="w")

        self.title_textbox = customtkinter.CTkEntry(self.scrollable_frame, width=400, font=('Arial', 12), height=50,
                                                    corner_radius=18)
        self.title_textbox.grid(row=1 + 12 + new_index, column=0, pady=(100, 385), padx=(555, 1))

        self.step_message = customtkinter.CTkLabel(self.scrollable_frame, text=f"Please edit the {new_index + 1} step:",
                                                   font=('bold', 18))
        self.step_message.grid(row=1 + 12 + new_index, column=0, padx=(350, 1), pady=(1, 130), sticky="w")

        self.subtract_button_third_step = customtkinter.CTkButton(self.scrollable_frame, text="-", width=100 - 6,
                                                                  height=32 - 6, command=lambda
                index=new_index: self.subtract_button_callback(index))
        self.subtract_button_third_step.grid(row=1 + 12 + new_index, column=0, padx=(103, 1), pady=(350, 1))

        self.entry_third_step = customtkinter.CTkEntry(self.scrollable_frame, width=350, height=32 - 6, border_width=0)
        self.entry_third_step.grid(row=1 + 12 + new_index, column=0, padx=(543, 1), pady=(350, 1))
        self.entry_third_step.insert(0, f"{' ':>50}0:00")

        self.add_button_third_step = customtkinter.CTkButton(self.scrollable_frame, text="+", width=100 - 6,
                                                             height=32 - 6,
                                                             command=lambda index=new_index: self.add_button_callback(
                                                                 index))
        self.add_button_third_step.grid(row=1 + 12 + new_index, column=0, padx=(985, 1), pady=(350, 1))

        self.delete_step_img = Image.open(r"C:\Users\Admin\Desktop\logo\x.png")
        self.delete_step_img = self.delete_img.resize((24, 24))
        self.delete_step_photo = customtkinter.CTkImage(self.delete_step_img)
        self.delete_button = customtkinter.CTkButton(self.scrollable_frame, text="", width=100 - 6, height=32 - 6,
                                                     command=lambda index=new_index: self.delete_button_callback(index),
                                                     corner_radius=12, image=self.delete_step_photo)
        self.delete_button.grid(row=1 + 12 + new_index, column=1, padx=(1, 1), pady=(40, 1), sticky="e")
        self.delete_buttons.append(self.delete_button)

        # add new widgets to appropriate arrays
        self.timers.append(self.entry_third_step)
        self.subtract_button_timers.append(self.subtract_button_third_step)
        self.add_button_timers.append(self.add_button_third_step)
        self.tab3_text_boxes.append(self.textbox)
        self.step_message_array.append(self.step_message)
        self.title_textbox_array.append(self.title_textbox)

    def delete_button_callback(self, index):
        # Remove the step at the given index from the recipe

        print("Index:", index)
        print("Length of timers:", len(self.timers))

        # Remove the widgets for the step from the GUI
        print("Length of subtract_button_timers:", len(self.subtract_button_timers))
        self.subtract_button_timers[index].destroy()
        self.add_button_timers[index].destroy()
        self.tab3_text_boxes[index].destroy()
        self.step_message_array[index].destroy()
        self.title_textbox_array[index].destroy()
        self.delete_buttons[index].destroy()
        self.timers[index].destroy()

        # Remove the widgets from their respective arrays
        del self.subtract_button_timers[index]
        del self.add_button_timers[index]
        del self.tab3_text_boxes[index]
        del self.step_message_array[index]
        del self.title_textbox_array[index]
        del self.timers[index]
        del self.delete_buttons[index]  # remove corresponding delete button from self.delete_buttons

        # Update the indices of the remaining steps
        self.stepp_counter -= 1
        for i in range(index, len(self.step_message_array)):
            self.step_message_array[i].configure(text=f"Please edit the {i + 1} step:")
            self.timers[i].grid(row=12 + i + 1, column=0, padx=(543, 1), pady=(350, 1))
            self.subtract_button_timers[i].grid(row=12 + i + 1, column=0, padx=(103, 1), pady=(350, 1))
            self.add_button_timers[i].grid(row=12 + i + 1, column=0, padx=(985, 1), pady=(350, 1))
            self.tab3_text_boxes[i].grid(row=12 + i + 1, column=0, pady=(150, 100), padx=(550, 1), sticky="w")
            self.step_message_array[i].grid(row=12 + i + 1, column=0, padx=(350, 1), pady=(1, 130), sticky="w")
            self.title_textbox_array[i].grid(row=12 + i + 1, column=0, pady=(100, 385), padx=(555, 1))
            self.delete_buttons[i].grid(row=12 + i + 1, column=1, padx=(1, 1), pady=(40, 1), sticky="e")

        # Update the callbacks for the remaining buttons
        for i, button in enumerate(self.subtract_button_timers):
            button.configure(command=lambda index=i: self.subtract_button_callback(index))
        for i, button in enumerate(self.add_button_timers):
            button.configure(command=lambda index=i: self.add_button_callback(index))
        for i, button in enumerate(self.delete_buttons):
            button.configure(command=lambda index=i: self.delete_button_callback(index))

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
        if entry_third_step.winfo_exists():
            try:
                current_value = entry_third_step.get()
                hours, minutes = map(int, current_value.split(':'))
                current_time = timedelta(hours=hours, minutes=minutes)
                new_time = current_time + timedelta(minutes=increment)

                # Ensure that the time will be equal or higher of 00:00
                if new_time < timedelta():
                    new_time = timedelta()

                hours, minutes = divmod(new_time.seconds // 60, 60)
                formatted_time = f"{hours:51}:{minutes:02}"

                entry_third_step.delete(0, "end")
                entry_third_step.insert(0, formatted_time)
            except ValueError:
                pass

    def ingredients_text_box(self):
        if self.text_box_visible:
            self.ingredients_textbox.grid_forget()  # hide the text box
            self.text_box_visible = False
        else:
            if not self.text_box_created:
                self.ingredients_textbox = customtkinter.CTkTextbox(self.scrollable_frame, width=200, corner_radius=12,
                                                                    height=265, border_width=5, border_spacing=25,
                                                                    border_color=("#3673F8", "orange"),
                                                                    scrollbar_button_color=("#3673F8", "orange"),
                                                                    font=('Arial', 24))
                self.text_box_created = True
            self.ingredients_textbox.grid(row=9, column=0, padx=(525, 1), pady=(1, 1), sticky="nsew")
            self.text_box_visible = True
        selectedRecipe = self.recipe[0]
        if len(self.ingredients_textbox.get("1.0", "end-1c")) == 0:
            self.ingredients_textbox.insert(tkinter.INSERT, selectedRecipe[6])

    def step1_time_changer(self, increment):
        try:
            current_value = self.entry.get()
            hours, minutes = map(int, current_value.split(':'))
            current_time = timedelta(hours=hours, minutes=minutes)
            new_time = current_time + timedelta(minutes=increment)

            # Ensure that the time will be equal or higher of 00:00
            if new_time < timedelta():
                new_time = timedelta()

            hours, minutes = divmod(new_time.seconds // 60, 60)
            formatted_time = f"{hours:69}:{minutes:02}"

            self.entry.delete(0, "end")
            self.entry.insert(0, formatted_time)
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

    def save_changes(self):

        if self.search_name.get() == "":
            # Display message to user that recipe name is empty
            messagebox.showerror("Error", "Recipe name cannot be empty.")
        elif self.entry.get() == f"{' ':>68}0:00":

            # Display message to user that textbox is empty
            messagebox.showerror("Error", "Recipe time cannot be empty.")
            # Special string arguments used to represent the starting and ending positions of a text widget's content.
        elif hasattr(self, "ingredients_textbox") and \
                self.ingredients_textbox is not None and self.ingredients_textbox.get("1.0", "end-1c") == "":
            # Display message to user that ingredients are empty
            messagebox.showerror("Error", "Ingredients cannot be empty.")

        elif not self.step_message_array:

            # Display message to user that textbox is empty
            messagebox.showerror("Error", "Recipe Steps can not be zero.")
        else:
            for textbox in self.tab3_text_boxes:
                if textbox.get() == "":
                    # Display message to user that textbox is empty
                    messagebox.showerror("Error", "Step cannot be empty.")
                    return  # Stop execution if any textbox is empty

            # Check for empty title text boxes
            for title_textbox in self.title_textbox_array:
                if title_textbox.get() == "":
                    # Display message to user that title textbox is empty
                    messagebox.showerror("Error", "Step Title  cannot be empty.")
                    return  # Stop execution if any title textbox is empty

            for timer in self.timers:
                if timer.get() == "" or timer.get() == f"{' ':>50}0:00":
                    # Display message to user that title textbox is empty
                    messagebox.showerror("Error", "Step Timer cannot be zero.")
                    return
            if self.ingredients_textbox is None:
                cursor.execute(
                    "UPDATE Recipe SET name=?,duration=? WHERE recipeId=?",
                    (self.search_name.get(), self.entry.get().strip(), self.values[0]))
                cursor.execute("DELETE FROM STEP WHERE recipeId = ?", (self.values[0],))
                for counter in range(self.stepp_counter):
                    cursor.execute("INSERT INTO STEP(title, instructions, time, recipeId) VALUES(?, ?, ?, ?)", (
                        self.title_textbox_array[counter].get(), self.tab3_text_boxes[counter].get(),
                        self.timers[counter].get().strip(), self.values[0]))
            else:
                cursor.execute(
                    "UPDATE Recipe SET name=?,duration=?,ingredients=? WHERE recipeId=?",
                    (self.search_name.get(), self.entry.get().strip(), self.ingredients_textbox.get("1.0", tkinter.END),
                     self.values[0]))
                cursor.execute("DELETE FROM STEP WHERE recipeId = ?", (self.values[0],))
                for counter in range(self.stepp_counter):
                    cursor.execute("INSERT INTO STEP(title, instructions, time, recipeId) VALUES(?, ?, ?, ?)", (
                        self.title_textbox_array[counter].get(), self.tab3_text_boxes[counter].get(),
                        self.timers[counter].get().strip(), self.values[0]))
            conn.commit()
            self.exit()

    def exit(self):
        self.left_frame.grid()
        self.center_frame.grid()
        self.editing_frame.destroy()
        self.save_changes_button.destroy()

        # Initialize lists here
        self.timers = []
        self.subtract_button_timers = []
        self.add_button_timers = []
        self.tab3_text_boxes = []
        self.step_message_array = []
        self.title_textbox_array = []
        self.delete_buttons = []
        self.steps_created = False
        self.steps_visible = False
        self.text_box_visible = False
        self.text_box_created = False
        self.ingredients_textbox = None
        self.parent.title("Let's Cook-Recipe Search")

    def delete(self):
        selectedRowToDelete = self.tree_view.focus()
        if not selectedRowToDelete:
            return
        items = self.tree_view.item(selectedRowToDelete)
        self.rowValues = items.get("values")
        sql_query = "DELETE FROM Recipe WHERE recipeId =?"
        cursor.execute(sql_query, (self.rowValues[0],))
        sql_query = "DELETE FROM Step WHERE recipeId =?"
        cursor.execute(sql_query, (self.rowValues[0],))
        conn.commit()
        cursor.execute("SELECT * FROM Recipe")
        recipes = cursor.fetchall()
        for row in self.tree_view.get_children():
            self.tree_view.delete(row)
        for recipe in recipes:
            print(recipe[6])
            self.tree_view.insert("", "end", text="Item 1",
                                  values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))

    def search_but(self):
        if self.filtersOn:
            if self.search_name.index("end") == 0:
                query = "SELECT * FROM Recipe WHERE cuisine=? AND category=? AND difficulty=?"
                cuisine = self.combobox.get().strip()
                category = self.category_box.get().strip()
                diff = self.difficulty_box.get().strip()
                cursor.execute(query, (cuisine, category, diff))
                search_recipes = cursor.fetchall()
                for row in self.tree_view.get_children():
                    self.tree_view.delete(row)
                for recipe in search_recipes:
                    self.tree_view.insert("", "end", text="Item 1",
                                          values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))
                return False
            else:
                query = "SELECT * FROM Recipe WHERE name=? AND cuisine=? AND category=? AND difficulty=?"
                cursor.execute(query, (
                self.search_name.get(), self.combobox.get(), self.category_box.get(), self.difficulty_box.get()))
                search_recipes = cursor.fetchall()
                for row in self.tree_view.get_children():
                    self.tree_view.delete(row)
                for recipe in search_recipes:
                    self.tree_view.insert("", "end", text="Item 1",
                                          values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))
                return False
        else:
            if self.search_name.index("end") == 0:
                cursor.execute("SELECT * FROM Recipe")
                recipes = cursor.fetchall()
                for row in self.tree_view.get_children():
                    self.tree_view.delete(row)
                for recipe in recipes:
                    print(recipe[6])
                    self.tree_view.insert("", "end", text="Item 1",
                                          values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))
                return False
            else:
                sql_query = "SELECT * FROM Recipe WHERE NAME=?"
                cursor.execute(sql_query, (self.search_name.get(),))
                search_recipes = cursor.fetchall()
                for row in self.tree_view.get_children():
                    self.tree_view.delete(row)
                for recipe in search_recipes:
                    self.tree_view.insert("", "end", text="Item 1",
                                          values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))

    def show_all_recipes(self):
        if self.search_name.get().compare("end-1c", "==", "1.0"):
            cursor.execute("SELECT * FROM Recipe")
            recipes = cursor.fetchall()
            for recipe in recipes:
                print(recipe[6])
                self.tree_view.insert("", "end", text="Item 1",
                                      values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))

    def lets_cook_window(self):
        selectedRow = self.tree_view.focus()
        if not selectedRow:
            return
        items = self.tree_view.item(selectedRow)
        selectedValues = items.get("values")
        self.center_frame.grid_remove()
        self.left_frame.grid_remove()
        self.parent.title("Let's Cook")
        Lets_Cook(self.parent, self.center_frame, self.left_frame, selectedValues[0])
