class INTRO(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._resize_image_ids = []
        self.search = customtkinter.StringVar()
        self.title("Let's Cook")
        self.geometry(f"{1400}x{800}")
        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")
        self.image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")
        self.photoImage = ImageTk.PhotoImage(self.image)

        # Create a label and place it in the window
        self.photoLabel = tk.Label(self, image=self.photoImage)
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        # intro layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.img = Image.open(r"C:\Users\Admin\Desktop\logo\chef.png")
        self.img = self.img.resize((24, 24))
        self.photo = customtkinter.CTkImage(self.img)

        # Entry Button
        self.exit_button = customtkinter.CTkButton(self, text="Let's Cook", width=200, height=40, image=self.photo,
                                                   corner_radius=2, text_color='Black', fg_color="#A4A4A4",
                                                   font=('Arial', 20),
                                                   command=self.show_second_window)
        self.exit_button.grid(row=1, column=1, padx=0, pady=0)

        # Periodically resize the image to reduce lag and flashing
        self._resize_image()

    def _resize_image(self):
        # Resize the image to fit the window size
        width = self.winfo_width()
        height = self.winfo_height()

        # Start a new thread to resize the image
        threading.Thread(target=self._resize_image_thread, args=(width, height)).start()

        # Schedule the next image resize
        self._resize_image_ids = self._resize_image_ids[-2:] + [self.after(7, self._resize_image)]
        self.bind('<Destroy>', lambda event: self.after_cancel(self._resize_image_ids[-1]))

    def _resize_image_thread(self, width, height):
        image = self.image.resize((width, height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(image)

        # Update the label with the new image
        self.photoLabel.configure(image=photo_image)
        self.photoLabel.image = photo_image

    def show_second_window(self):
        self.destroy()
        menu = GUI()
        menu.mainloop()