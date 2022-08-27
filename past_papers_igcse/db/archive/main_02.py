# ================================================================================================== >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# Tkinter Class Based Windows: https://youtu.be/RkaekNkIKNY
# =============================================================================================================== <<
from tkinter import *
import sqlite3

def main(): 
    root = Tk()
    app = Application(root, "Past Paper Database (0478 Computer Science)", '400x500')
    return None

class Application:
    n = 0
    def __init__(self, root, title, geometry):
        # ------------------------------------------------------------------ >> create window <<
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

        self.conn = sqlite3.connect('0478_past_papers.db')
        self.unit_choices = self.get_units(self.conn)
        self.unit_selected = ''
        # ------------------------------------------------- >> add widgets & run application  <<
        self.create_widgets()
        self.root.mainloop()
        

    def create_widgets(self):
        # ------------------------------------------------------------- >> units option menu  <<
        variable = StringVar(self.root)
        variable.set(self.unit_choices[0])
        unit_menu = OptionMenu(self.root, variable, *self.unit_choices, command = self.set_unit)
        unit_menu.pack()
        

    def get_units(self, conn):
        cur = conn.cursor()
        cur.execute('SELECT unit FROM units;')
        records = cur.fetchall()
        return [row[0] for row in records]


    def set_unit(self, arg):
        self.unit_selected = arg
        print(self.unit_selected)
        return None

# ================================================================================================== >> main code <<
if __name__ == '__main__':
    main()
