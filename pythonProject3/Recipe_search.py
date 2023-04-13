from imports import *
from Registration import RegistrationDef



class Recipe_search(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set window size to full screen
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
        self.title("Registration")
        self.filter_counter = 0

        self.overrideredirect(False)
        width = int(self.winfo_screenwidth() * 1.039)
        height = int(self.winfo_screenheight() * 0.941)
        x = int(self.winfo_screenwidth() / 2 - width / 2 + 25)
        y = int(self.winfo_screenheight() / 2 - height / 2 - 40)
        self.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))
        self.resizable(True, True)

        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")
        self.title("Let's Cook-Recipe Search")

        self.grid_columnconfigure((1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 4), weight=1)

        # left frame
        self.left_frame = customtkinter.CTkFrame(self, width=400, corner_radius=20)
        self.left_frame.grid(row=0, column=0, rowspan=5, columnspan=1, sticky="nsew", padx=(20, 1), pady=(20, 20))
        self.left_frame.grid_rowconfigure(4, weight=1)

        self.center_frame = customtkinter.CTkFrame(self, width=850, corner_radius=20, height=80)
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

        self.Recipe_name = customtkinter.CTkEntry(self.left_inside_frame,
                                                  placeholder_text="                     "
                                                                   "                     "
                                                                   "Enter Recipe Name", width=400,
                                                  height=25,
                                                  border_width=1, corner_radius=10)
        self.Recipe_name.grid(row=0, column=0, padx=(20, 20), pady=(100, 150), sticky="n")

        self.recipe_search_tittle = customtkinter.CTkLabel(self.left_inside_frame, text="Use filters to find a recipe",
                                                           font=customtkinter.CTkFont(size=20, weight="bold"))
        self.recipe_search_tittle.grid(row=0, column=0, padx=(80, 80), pady=(50, 1), sticky="ew")

        self.filter_button = customtkinter.CTkButton(self.left_inside_frame, text="Filters",
                                                     width=130, height=40, command=self.handle_filter_button)
        self.filter_button.grid(row=0, column=0, padx=0, pady=(150, 1), )

        self.back_button = customtkinter.CTkButton(self.left_inside_frame, text="←  back   ",
                                                   width=60, height=30, corner_radius=15, command=self.back_to_menu)
        self.back_button.grid(row=90, column=0, padx=0, pady=(50, 1), sticky="w")

        self.edit_img = Image.open(r"C:\Users\Admin\Desktop\logo\spoon.png")
        self.edit_img = self.edit_img.resize((24, 24))
        self.edit_photo = customtkinter.CTkImage(self.edit_img)

        self.editing_button = customtkinter.CTkButton(self.bottom_frame, text="Edit Recipe",image=self.edit_photo,
                                                      width=130, height=40, corner_radius=15,
                                                      )
        self.editing_button.grid(row=0, column=0, padx=(1, 10), pady=(30, 30), sticky="e")

        self.delete_img = Image.open(r"C:\Users\Admin\Desktop\logo\x.png")
        self.delete_img = self.delete_img.resize((24, 24))
        self.delete_photo = customtkinter.CTkImage(self.delete_img)


        self.delete_button = customtkinter.CTkButton(self.bottom_frame, text="Delete Recipe", image=self.delete_photo,
                                                      width=130, height=40, corner_radius=15,
                                                      )
        self.delete_button.grid(row=0, column=4, padx=(1, 10), pady=(30, 30), sticky="w")

        self.img = Image.open(r"C:\Users\Admin\Desktop\logo\chef.png")
        self.img = self.img.resize((24, 24))
        self.photo = customtkinter.CTkImage(self.img)

        self.cook_button = customtkinter.CTkButton(self.bottom_frame, text="Let's Cook", image=self.photo,
                                                      width=130, height=40, corner_radius=15,
                                                      )
        self.cook_button.grid(row=0, column=2, padx=(1, 1), pady=(30, 30), sticky="nsew")

        self.search_img = Image.open(r"C:\Users\Admin\Desktop\logo\search.png")
        self.search_img = self.search_img.resize((24, 24))
        self.search_photo = customtkinter.CTkImage(self.search_img)



        self.search_button = customtkinter.CTkButton(self.left_inside_frame, text="Search", image=self.search_photo,
                                                     width=240, height=40)
        self.search_button.grid(row=3, column=0, padx=0, pady=(10, 1), )




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

        else:
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
        self.destroy()
        from Menu import Menu
        self.back = Menu()

        self.back.mainloop()


if __name__ == "__main__":
    window = Recipe_search()
    window.mainloop()
