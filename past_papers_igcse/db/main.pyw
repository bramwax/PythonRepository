import tkinter as tk
from tkinter import ttk

import query_questions as qry_que
import insert_paper as ins_pap
import insert_question as ins_que

class Switchboard:

    def __init__(self): # --------------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> declare & assign variables <<
        self.bgcolor = '#f5f4ed' # beige

        # ---------- >> create & configure switchboard window  <<
        self.master = tk.Tk()
        self.master.geometry('614x210')
        self.master.iconbitmap('favicon.ico')
        self.master.title(' Videorials ')
        self.master.resizable(False, False)
        self.master.configure(bg = self.bgcolor)
        
        # ---------- >> set styles & create widgets <<
        self.set_styles()
        self.widgets()

        # ---------- >> run window (application)  <<
        self.master.mainloop()

    def set_styles(self):  # ----------------------------------------------------------------------------------------------------- >> apply widget styles <<

        # ---------- >> adjust button text size <<
        self.master.option_add('*font', 'Arial 13') # increase button text size

        self.style = ttk.Style()

        # ---------- >> backgrounds <<
        self.style.configure('TLabel', background = self.bgcolor)
        self.style.configure('TFrame', background = self.bgcolor)
        self.style.configure('TLabelframe', background = self.bgcolor)

         # ---------- >> label text size <<
        self.style.configure('TLabelframe.Label', font=('Arial 14'))

         # ---------- >> combobox & input widget internal padding <<
        self.style.configure('TEntry', padding = '3 3 3 3')
        self.style.configure('TCombobox', padding = '3 3 3 3')

         # ---------- >> treeview table <<
        self.style.configure("Treeview.Heading", font=('Arial', 11,'bold'))
        self.style.configure("Treeview", font = ('Arial', 11))

    def widgets(self): # ----------------------------------------------------------------------------------------------------- >> add switchboard widgets <<

        # ---------- >> title & subtitle <<
        ttk.Label(self.master,
                  text = 'Past paper exam questions database',
                  font = 'calibri 20 bold').place(x = 26, y = 20, anchor = 'nw')
        ttk.Label(self.master,
                  text = 'Cambridge IGCSE Computer Science (0478)',
                  font = 'calibri 14 bold').place(x = 26, y = 60, anchor = 'nw')

        # ---------- >> separators  <<
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

    def new_window(self, trigger): # ----------------------------------------------------------------------------------------------- >> create sub-window <<

        # ---------- >> create new (toplevel) window <<
        self.master = tk.Toplevel()

        # ---------- >> create & configure corresponding frame  <<
        if trigger == 'query':
            self.frame = qry_que.Query_Frame(self.master)
            self.master.geometry('1002x680')

        elif trigger == 'paper':
            self.frame = ins_pap.Paper_Frame(self.master)
            self.master.geometry('408x376')
        else:
            self.frame = ins_que.Question_Frame(self.master)
            self.master.geometry('952x660')      

        self.master.iconbitmap('favicon.ico')
        self.master.resizable(False, False)
        self.master.configure(bg = self.bgcolor)


        self.frame.pack(expand = 1,
                        fill = 'both',
                        padx = 20, pady = 20)

        # ---------- >> run window (application)  <<
        self.master.mainloop()

# ========================================================================================================================================== >> main code <<
# ----------------------------------------------------------------------------------------------------------------------------------------------------------
def main():
    Switchboard()

if __name__ == '__main__':
    main()