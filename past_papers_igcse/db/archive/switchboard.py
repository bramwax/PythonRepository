import tkinter as tk
from tkinter import ttk
import query_frame as qry
import paper_frame as pap
import question_frame as que

class Switchboard:

    def __init__(self): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create & configure window  <<
        
        #self.master = master
        self.master = tk.Tk()
        self.master.geometry('614x210')
        self.master.iconbitmap('favicon.ico')
        self.master.title(' Videorials ')
        self.master.resizable(False, False)
        
        # ---------- >> set styles & create widgets <<
        self.set_styles()
        self.widgets()

        # ---------- >> run window (application)  <<
        self.master.mainloop()

    def set_styles(self):

        self.master.configure(bg = '#f5f4ed') # beige background
        self.master.option_add('*font', 'Arial 13') # increase button text size

        self.master.style = ttk.Style()
        self.master.style.configure('TEntry', padding = '3 3 3 3')
        self.master.style.configure('TCombobox', padding = '3 3 3 3')

        self.master.style.configure("Treeview",
                                    font = ('Arial', 12))
        self.master.style.configure("Treeview.Heading",
                                    font=('Arial', 12,'bold'),
                                    background='black', foreground='black')

    def widgets(self):

        # ---------- >> tab headings & separators  <<
        ttk.Label(self.master,
                  text = 'Past paper exam questions database',
                  font = 'calibri 20 bold').place(x = 26, y = 20, anchor = 'nw')

        ttk.Label(self.master,
                  text = 'Cambridge IGCSE Computer Science (0478)',
                  font = 'calibri 14 bold').place(x = 26, y = 60, anchor = 'nw')

        ttk.Separator(self.master, orient='horizontal').place(x = 10, y = 100, width = 590)

        # ---------- >> query button  <<
        self.query_bt = tk.Button(self.master,
                                  text = 'Query by Objective',
                                  bg = '#f0e6e6', width = 18, height = 3,
                                  command = lambda: self.new_window('query'))
        self.query_bt.place(x = 20, y = 120, anchor = 'nw')

        # ---------- >> paper button  <<
        self.paper_bt = tk.Button(self.master,
                                  text = 'Insert Paper(s)',
                                  bg = '#e6e8f0', width = 18, height = 3,
                                  command = lambda: self.new_window('paper'))
        self.paper_bt.place(x = 220, y = 120, anchor = 'nw')

        # ---------- >> question button  <<
        self.paper_bt = tk.Button(self.master,
                                  text = 'Insert Question(s)',
                                  bg = '#e7f0e6', width = 18, height = 3,
                                  command = lambda: self.new_window('question'))
        self.paper_bt.place(x = 420, y = 120, anchor = 'nw')

    def new_window(self, trigger):

        # ---------- >> create new window <<
        self.master = tk.Toplevel() #tk.Tk()

        # ---------- >> create & configure corresponding frame  <<
        if trigger == 'query':
            self.frame = qry.Query_Frame(self.master)
            self.master.geometry('962x620')
        elif trigger == 'paper':
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


        #win.Window(self.master, trigger)