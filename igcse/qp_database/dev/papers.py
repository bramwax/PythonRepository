import tkinter as tk
from tkinter import ttk


class Paper:

    def __init__(self, master): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create & configure window  <<
        self.master = master
        self.master.title('Add Papers')
        self.master.geometry('500x500')
        self.master.option_add( '*font', 'Arial 14' )

        # ---------- >> add widgets <<
        self.create_widgets()

        # ---------- >> run window (application)  <<
        self.master.mainloop()