import tkinter
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()
print("Screen Resolution: {}x{}".format(width, height))