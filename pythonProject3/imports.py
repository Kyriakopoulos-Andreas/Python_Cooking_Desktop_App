import customtkinter
import tkinter as tk
import customtkinter as ctk             # Δήλωση Βιβλιοθήκης
from PIL import ImageTk, Image
from tkinter import messagebox
from datetime import timedelta
from screeninfo import get_monitors
from Registration import Registration
from Word_cuisine import Word_cuisine
from Recipe_search import Recipe_search
from Lets_Cook import Lets_Cook
from intro import Intro
from Menu import Menu


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
__all__ = ['tk',  'messagebox', 'ImageTk', 'Image', 'ctk', 'customtkinter','timedelta', 'get_monitors', 'Registration',
           'Word_cuisine', 'Recipe_search', 'Intro', 'Menu', 'Lets_Cook']