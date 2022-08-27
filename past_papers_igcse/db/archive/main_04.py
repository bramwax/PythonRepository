# ================================================================================================== >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# https://www.pythontutorial.net/tkinter/
# Tkinter Class Based Windows: https://youtu.be/RkaekNkIKNY
# =============================================================================================================== <<
import tkinter as tk
from tkinter import ttk
import sqlite3


def main(): 
    root = tk.Tk()
    root.geometry('600x499')
    root.resizable(False, False)
    root.title('Computer Science (0478) Past Papers')
    app = Application(root)


class Application:
    def __init__(self, root):
        # --------------------------------------------------------- >> initialise application <<
        self.root = root
        # ------------------------------ >> connect database <<
        self.conn = sqlite3.connect('0478_past_papers.db')
        # ------------------------------ >> variables <<
        self.unit_choices = self.get_units(self.conn)
        self.unit_id = None
        self.subunit_choices = [[],['Test']]
        self.subunit_id = None
        self.objective_choices = []
        self.objective_id = None
        # ------------------------------ >> create widgets & run application  <<
        self.create_widgets()
        self.root.mainloop()
        

    def create_widgets(self):
        # ------------------------------------------------------------- >> units option menu  <<
        self.units_cb = ttk.Combobox(self.root,
                                     values=self.unit_choices[1],
                                     state='readonly',
                                     width=38)
        self.units_cb.pack(side=tk.TOP, anchor=tk.NW, padx=20, pady=20)
        self.units_cb.bind('<<ComboboxSelected>>', self.set_unit)
        # ---------------------------------------------------------- >> subunits option menu  <<
        self.subunits_cb = ttk.Combobox(self.root,
                                        value=[],
                                        state='readonly',
                                        width=38)
        self.subunits_cb.pack(side=tk.TOP, anchor=tk.NW, padx=20, pady=20)
        self.subunits_cb.bind('<<ComboboxSelected>>', self.set_subunit)
        

    def get_units(self, conn):
        # ------------------------------ >> fetch data <<
        cur = conn.cursor()
        cur.execute('SELECT * FROM units;')
        records = cur.fetchall()
        # ------------------------------ >> place data in 2d array <<
        ids = [row[0] for row in records]
        units = [row[1] for row in records]
        return [ids, units]


    def get_subunits(self, conn):
        # ------------------------------ >> fetch data <<
        cur = conn.cursor()
        cur.execute(f'''SELECT DISTINCT(subunits.subunit_id), subunits.subunit
                        FROM subunits
                        JOIN objectives ON subunits.subunit_id = objectives.subunit_fk
                        WHERE objectives.unit_fk = {self.unit_id};''')
        records = cur.fetchall()
        # ------------------------------ >> place data in 2d array <<
        ids = [row[0] for row in records]
        subunits = [row[1] for row in records]
        return [ids, subunits]


    def set_unit(self, event):
        print('Unit changed!')
        # Update subunits for unit selected
        index = self.unit_choices[1].index(self.units_cb.get())
        self.unit_id = self.unit_choices[0][index]
        self.subunit_choices = self.get_subunits(self.conn)
        # Clear combobox and reset values
        self.subunits_cb.set([])
        self.subunits_cb.config(value=self.subunit_choices[1])


    def set_subunit(self, event):
        print('Subunit changed!')


# ================================================================================================== >> main code <<
if __name__ == '__main__':
    main()
