from imports import *
from Menu import Menu


class Intro(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = None
        self.title("Let's Cook-Intro")  # Αλλαγή της επικεφαλίδας του προγράμματος

        # Δημιουργούμε μια λίστα απο αντικείμενα τύπου monitor για την κάθε οθόνη
        # Το primary monitor αντιστοιχίζεται στο πρώτο στοιχείο που είναι η κύρια οθόνη

        primary_monitor = get_monitors()[0]
        width = int(primary_monitor.width)  # Ορίζουμε το πλάτος του παραθύρου ως το πλάτος της οθόνης
        height = int(primary_monitor.height + 10)  # Ορίζουμε το ύψος του παραθύρου ως το ύψος της οθόνης

        # Υπολογισμός των συντεταγμένων του παραθύρου για να βρούμε το κέντρο
        x = int((primary_monitor.width - width) / 2 - 11)
        y = int((primary_monitor.height - height) / 2 - 5)

        # Ορίζουμε τη γεωμετρία του παραθύρου
        self.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))


        self.iconbitmap(r"C:\Users\Admin\Desktop\logo\image.ico")  # Ορίζουμε το desktop icon της εφαρμογής
        self.image = Image.open(r"C:\Users\Admin\Desktop\logo\cook.jpg")   # Φορτώνουμε την εικόνα από το Path
        self.photoImage = ImageTk.PhotoImage(self.image)  # Δημιουργία αντικειμένου photoImage

        # Δημιουργούμε ένα label για την τοποθέτηση της εικόνας
        self.photoLabel = tk.Label(self, image=self.photoImage)
        self.photoLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        #  Διαμορφώνουμε διάταξη στο παράθυρο με γραμμές και στήλες
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.img = Image.open(r"C:\Users\Admin\Desktop\logo\chef.png")  # Φορτώνουμε από τον δίσκο την εικόνα
        self.img = self.img.resize((24, 24))  # Αλλαγή του μεγέθους της εικόνας
        self.photo = customtkinter.CTkImage(self.img)   # Δημιουργούμε ένα αντικείμενο

        # Δημιουργία κουμπιού και τοποθέτηση του αντικειμένου εικόνας για εισαγωγή στο μενού
        self.LetS_Cook_Button = customtkinter.CTkButton(self, text="Let's Cook", width=200, height=40, image=self.photo,
                                                        corner_radius=2, text_color='Black', fg_color="#A4A4A4",
                                                        font=('Arial', 20),
                                                        command=self.on_close)
        self.LetS_Cook_Button.grid(row=1, column=1, padx=0, pady=0)

    def on_close(self):   # Μέθοδος για κλείσιμο του intro παραθύρου και εισαγωγή στο μενού
        for after_id in self.tk.eval('after info').split():
            self.after_cancel(after_id)
        self.photoLabel.destroy()  # Καταστροφή της εικόνας
        self.LetS_Cook_Button.grid_remove() # Remove στο κουμπί του intro
        # Hide the Intro window
        # Create the Menu window
        self.title("Let's Cook-Menu")  # Αλλαγή της επικεφαλίδας
        self.menu = Menu(self)  # Περνάμε ως όρισμα το self για να δημιουργήσουμε το άλλο παράθυρο πάνω στη γονική κλάση
