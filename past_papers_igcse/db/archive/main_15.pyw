import tkinter as tk
from tkinter import ttk


class Switchboard:

    def __init__(self, root): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create & configure window  <<
        self.root = root
        self.root.geometry('708x122')
        self.root.option_add( '*font', 'Arial 14' )

        # ---------- >> add widgets <<
        self.create_widgets()

        # ---------- >> run window (application)  <<
        self.root.mainloop()

    def create_widgets(self):
        
        # ---------- >> query button  <<
        self.query_bt = tk.Button(self.root,
                                  text = 'Query by Objective',
                                  bg = '#f0e6e6', width = 18, height = 3,
                                  command = lambda: self.new_window('query'))
        self.query_bt.place(x = 20, y = 20, anchor = 'nw')

        # ---------- >> paper button  <<
        self.paper_bt = tk.Button(self.root,
                                  text = 'Insert new Papers',
                                  bg = '#e6e8f0', width = 18, height = 3,
                                  command = lambda: self.new_window('paper'))
        self.paper_bt.place(x = 248, y = 20, anchor = 'nw')

        # ---------- >> question button  <<
        self.paper_bt = tk.Button(self.root,
                                  text = 'Insert new Questions',
                                  bg = '#e7f0e6', width = 18, height = 3,
                                  command = lambda: self.new_window('questions'))
        self.paper_bt.place(x = 476, y = 20, anchor = 'nw')

    def new_window(self, trigger):
        print(f'Open {trigger} window')


root = tk.Tk()
root.resizable(False, False)
root.option_add( '*font', 'Arial 11' )
root.iconbitmap('favicon.ico')
root.title(' Past paper exam questions database | Cambridge IGCSE Computer Science (0478)')
root.configure(bg = '#f5f4ed')

app = Switchboard(root)