from imports import *


class Word_cuisine(customtkinter.CTk):
    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)

        self.current_file_index = 0  # αρχικοποίηση δείκτη
        # Πίνακας με όλα τα paths
        self.file_paths = ['C:/Users/Admin/PycharmProjects/pythonProject3/mediterranean.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/mexican.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/arabic.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/chinese.txt',
                           'C:/Users/Admin/PycharmProjects/pythonProject3/Thai.txt']

        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")   # Βάζουμε το desktop icon της εφαρμογής
        self.title("Let's Cook-Word Cuisine")   # Ορίζουμε την επικεφαλίδα του αυτόνομου παραθύρου
        self.resizable(False, False)   # Ορίζουμε το resize του παραθύρου σε false

        # Παίρνουμε και χρησιμοποιούμε τις συντεταγμένες του παραθύρου για να εμφανίζεται στο κέντρο
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - 900) / 2)
        y = int((screen_height - 500) / 2)
        self.geometry(f"900x500+{x}+{y}")

        # Ορίζουμε το διάγραμμα του παραθύρου με τα κουμπιά και το frame του

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.out_frame = customtkinter.CTkFrame(self, width=200, corner_radius=7)
        self.out_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(15, 15), pady=(15, 15), sticky="nsew")
        self.out_frame.grid_columnconfigure(0, weight=1)
        self.out_frame.grid_rowconfigure(0, weight=1)
        # Κουμπί εξόδου
        self.exit_button = customtkinter.CTkButton(self.out_frame, text="   exit    ", font=('Arial', 13, 'bold'),
                                                   height=27, width=150, corner_radius=7, command=self.exit_window)
        self.exit_button.grid(row=1, column=3, sticky="nw", pady=(1, 7))
        # Δεξί κουμπί πλοήγησης
        self.right_button = customtkinter.CTkButton(self.out_frame, text=" → ", font=('Arial', 34, 'bold'),
                                                    height=27, width=30, corner_radius=100, command=self.load_next_file)
        self.right_button.grid(row=0, column=3, sticky="e", pady=(1, 1))

        # Αριστερό κουμπί πλοήγησης
        self.left_button = customtkinter.CTkButton(self.out_frame, text=" ← ", font=('Arial', 34, 'bold'),
                                                   height=27, width=30, corner_radius=100,
                                                   command=self.load_previous_file)
        self.left_button.grid(row=0, column=0, sticky="w", pady=(1, 1))

        # Frame πάνω στο οποίο θα εμφανίζονται οι συνταγές
        self.information_frame = customtkinter.CTkScrollableFrame(self.out_frame, height=360,
                                                                  scrollbar_button_hover_color="#3786D9",
                                                                  width=670, corner_radius=12, border_width=5,
                                                                  border_color=("#3673F8", "orange",)
                                                                  )
        self.information_frame.grid(row=0, column=0, columnspan=7, rowspan=7, padx=(70, 70), pady=(50, 50),
                                    sticky="nsew")
        # Δημιουργία label για τις οδηγίες παραθύρου
        self.content_label = customtkinter.CTkLabel(self.information_frame,
                                                    text="                         Use the left and right button to "
                                                         "taste Word's Cuisines",
                                                    font=('Arial', 18),
                                                    wraplength=600, justify="left", width=60)
        self.content_label.grid(row=0, column=0)

        self.information_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.information_frame.grid_columnconfigure((0, 1, 2, 4, 5), weight=1)
        # Τίτλος παραθύρου
        self.information_logo = customtkinter.CTkLabel(self.out_frame, text="Word Cuisines",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.information_logo.grid(row=0, column=0, padx=(150, 1), sticky="n")

    def load_file(self):

        file_path = self.file_paths[self.current_file_index]

        # άνοιγμα του αρχείου για διάβασμα
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Για να μην εμφανίζει λάθος πράγματα κατά την αλλαγή κουζινών
        self.content_label.configure(text=" ")


        # Αποτροπή display errors  καθυστερούμε την εμφάνιση κατά 50 milliseconds
        self.content_label.after(50, lambda: self.content_label.configure(text=content))

    def load_next_file(self):
        # αυξάνουμε τον δείκτη αρχείου για να δείξουμε στο επόμενο
        self.current_file_index += 1
        if self.current_file_index >= len(self.file_paths): # Έλεγχος για να μην ξεφύγουμε εκτός ορίων
            self.current_file_index = 0
        self.load_file()  # Ανοίγουμε το επόμενο αρχείο

    def load_previous_file(self):
        # Μειώνουμε τον δείκτη και δείχνουμε στο προηγούμενο αρχείο
        self.current_file_index -= 1
        if self.current_file_index < 0:
            self.current_file_index = len(self.file_paths) - 1
        self.load_file()

    def exit_window(self):
        self.destroy()    # έξοδος από το παράθυρο



