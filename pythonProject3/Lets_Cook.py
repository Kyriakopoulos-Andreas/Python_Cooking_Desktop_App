from imports import *


class Lets_Cook(customtkinter.CTk):
    def __init__(self, parent):
        super().__init__()
        self.parent_class = parent

        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")
        self.title("Let's Cook")

        self.behind_frame = customtkinter.CTkFrame(self.parent_class, width=850, height=150)
        self.behind_frame.grid(row=0, column=1, columnspan=4, rowspan=5, sticky="nsew", padx=(1, 1), pady=(1, 1))
        self.behind_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.behind_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)

        self.center_frame = customtkinter.CTkFrame(self.behind_frame, width=900, corner_radius=20, height=80)
        self.center_frame.grid(row=0, column=1, columnspan=4, rowspan=5, sticky="nsew", padx=(50, 1), pady=(15, 15))
        self.center_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.center_frame.grid_columnconfigure((0, 1, 2, 3), weight=0)

        self.tittle = customtkinter.CTkLabel(self.center_frame, text="Let's Give Soul To The Recipe", font=('Bold', 27))
        self.tittle.grid(row=0, column=1, columnspan=4, padx=(1, 100), pady=(10, 1), sticky="n")

        self.back_editing_button = customtkinter.CTkButton(self.center_frame, text="          ←  back          ",
                                                           width=70, height=30,
                                                           corner_radius=15,
                                                           command=self.back)
        self.back_editing_button.grid(row=4, column=0,  padx=(1, 10), pady=(1, 1), sticky="nse")
        self.right_button = customtkinter.CTkButton(self.center_frame, text="     Next Step    ",
                                                    font=('Arial', 18, 'bold'),
                                                    height=27, width=30, corner_radius=100)
        self.right_button.grid(row=1, column=1, sticky="e", pady=(80, 1))

        self.left_button = customtkinter.CTkButton(self.center_frame, text=" Previous Step ",
                                                   font=('Arial', 18, 'bold'),
                                                   height=27, width=30, corner_radius=100)
        self.left_button.grid(row=1, column=0, sticky="w", pady=(80, 1), padx=(1, 20))

        self.back_editing_button.grid(row=5, column=1, padx=(1, 1500), pady=(1, 1), sticky="s")

        self.information_frame = customtkinter.CTkScrollableFrame(self.center_frame, height=810,
                                                                  scrollbar_button_hover_color="#3786D9",
                                                                  width=10, corner_radius=12, border_width=5,
                                                                  border_color=("#3673F8", "orange",)
                                                                  )
        self.information_frame.grid(row=0, column=0, columnspan=3, rowspan=5, padx=(167, 165), pady=(50, 10),
                                    sticky="nsew")

        self.progressbar = customtkinter.CTkProgressBar(self.center_frame, orientation="horizontal", height=18,
                                                        width=20)
        self.progressbar.grid(row=6, column=1, padx=(350, 500), pady=(1, 15),
                              sticky="nsew")

        self.progress_tittle = customtkinter.CTkLabel(self.center_frame, text="Recipe Progress", font=('Bold', 24))
        self.progress_tittle.grid(row=5, column=1, padx=(160, 267), pady=(1, 5),
                                  sticky="nsew")

    def back(self):
        self.parent_class.left_frame.grid()
        self.parent_class.center_frame.grid()
        self.behind_frame.grid_remove()
        self.center_frame.grid_remove()
