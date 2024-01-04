import tkinter as tk
from tkinter import ttk
import query_frame as qry
import paper_frame as pap
import question_frame as que

class Window():

    def __init__(self, master, trigger): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # set window type to query, paper, or question
        self.app_function = trigger

        # ---------- >> create & configure window  <<
        self.master = master

        self.master.focus_force()
        self.master.resizable(False, False)
        self.master.iconbitmap('favicon.ico')
        self.master.title(' Videorials ')
        self.master.configure(bg = '#f5f4ed')
        self.master.option_add( '*font', 'Arial 11' )

        # ---------- >> create & configure corresponding frame  <<
        if self.app_function == 'query':
            self.frame = qry.Query_Frame(self.master)
            self.master.geometry('962x620')
        elif self.app_function == 'paper':
            self.frame = pap.Paper_Frame(self.master)
            self.master.geometry('360x330')
        else:
            self.frame = que.Question_Frame(self.master)
            self.master.geometry('500x300')           

        self.frame.pack(expand = 1,
                        fill = 'both',
                        padx = 20, pady = 20,
                        ipadx = 20, ipady = 20)

        # ---------- >> run window (application)  <<
        self.master.mainloop()