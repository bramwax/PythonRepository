import tkinter as tk
from tkinter import ttk


class Question:

    def __init__(self, master): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create & configure window  <<
        self.master = master
        self.master.title('Add Questions')
        self.master.geometry('800x800')
        self.master.option_add( '*font', 'Arial 14' )

        # ---------- >> add widgets <<
        self.create_widgets()

        # ---------- >> run window (application)  <<
        self.master.mainloop()