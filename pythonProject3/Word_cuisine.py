from imports import *


class Word_cuisine(customtkinter.CTk):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.current_file_index = 0  # Initialize the current file index to 0
        self.file_paths = ['C:/Users/Admin/PycharmProjects/pythonProject3/mediterranean.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/mexican.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/arabic.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/chinese.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/Thai.txt']

        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")
        self.title("Let's Cook-Word Cuisine")
        self.resizable(False, False)
        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 900) / 2)
        y = int((screen_height - 500) / 2)
        self.geometry(f"900x500+{x}+{y}")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.out_frame = customtkinter.CTkFrame(self, width=200, corner_radius=7)
        self.out_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15), sticky="nsew")
        self.out_frame.grid_columnconfigure(0, weight=1)
        self.out_frame.grid_rowconfigure(0, weight=1)

        self.exit_button = customtkinter.CTkButton(self.out_frame, text="   exit    ", font=('Arial', 13, 'bold'),
                                                   height=27, width=150, corner_radius=7, command=self.exit_window)
        self.exit_button.grid(row=1, column=3, sticky="nw", pady=(1, 7))

        self.right_button = customtkinter.CTkButton(self.out_frame, text=" → ", font=('Arial', 34, 'bold'),
                                                    height=27, width=30, corner_radius=100)
        self.right_button.grid(row=0, column=3, sticky="e", pady=(1, 1))
        self.right_button.bind('<Button-1>', lambda event: self.load_next_file())

        self.left_button = customtkinter.CTkButton(self.out_frame, text=" ← ", font=('Arial', 34, 'bold'),
                                                   height=27, width=30, corner_radius=100)
        self.left_button.grid(row=0, column=0, sticky="w", pady=(1, 1))
        self.left_button.bind('<Button-1>', lambda event: self.load_previous_file())

        self.information_frame = customtkinter.CTkScrollableFrame(self.out_frame, height=360,
                                                                  scrollbar_button_hover_color="#3786D9",
                                                                  width=670, corner_radius=12, border_width=5,
                                                                  border_color=("#3673F8", "orange",)
                                                                  )
        self.information_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(70, 70), pady=(50, 50),
                                    sticky="nsew")
        self.content_label = customtkinter.CTkLabel(self.information_frame,
                                                    text="                         Use the left and right button to "
                                                         "taste Word's Cuisines",
                                                    font=('Arial', 18),
                                                    wraplength=600, justify="left", width=60)
        self.content_label.grid(row=0, column=0)

        self.information_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.information_frame.grid_columnconfigure((0, 1, 2, 4, 5), weight=1)

        self.information_logo = customtkinter.CTkLabel(self.out_frame, text="Word Cuisines",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.information_logo.grid(row=0, column=0, padx=(150, 1), sticky="n")

    def load_file(self):
        # Get the file path based on current file index
        file_path = self.file_paths[self.current_file_index]

        # Read file content
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Update display with a space to avoid fault displaying
        self.content_label.configure(text=" ")


        # Avoid the display error problem
        # Delay the displaying 30 milliseconds
        self.content_label.after(50, lambda: self.content_label.configure(text=content))

    def load_next_file(self):
        # Increment current file index and load the next file
        self.current_file_index += 1
        if self.current_file_index >= len(self.file_paths):
            self.current_file_index = 0  # Wrap around to the first file
        self.load_file()

    def load_previous_file(self):
        # Decrement current file index and load the previous file
        self.current_file_index -= 1
        if self.current_file_index < 0:
            self.current_file_index = len(self.file_paths) - 1  # Wrap around to the last file
        self.load_file()

    def exit_window(self):
        self.destroy()



if __name__ == "__main__":
    app = Word_cuisine()
    app.mainloop()
