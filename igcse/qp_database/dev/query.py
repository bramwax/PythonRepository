import tkinter as tk
from tkinter import ttk


class Query:

    def __init__(self, master): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create & configure window  <<
        self.master = master
        #self.master.title('Query by Objective')
        self.master.geometry('300x300')
        #self.master.option_add( '*font', 'Arial 14' )

        # ---------- >> add widgets <<
        self.create_widgets()

        # ---------- >> run window (application)  <<
        self.master.mainloop()