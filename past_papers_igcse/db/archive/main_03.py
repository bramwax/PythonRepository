# ================================================================================================== >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# Tkinter Class Based Windows: https://youtu.be/RkaekNkIKNY
# =============================================================================================================== <<
from tkinter import *
import sqlite3


def main(): 
    root = Tk()
    app = Application(root, "Past Paper Database (0478 Computer Science)", '600x400')
    return None


class Application:
    n = 0
    def __init__(self, root, title, geometry):
        # ------------------------------------------------------------------ >> create window <<
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        # ------------------------------------------------------------------ >> connect to db <<
        self.conn = sqlite3.connect('0478_past_papers.db')
        # -------------------------------------------------------------- >> declare variables <<
        self.unit_choices = self.get_units(self.conn)
        self.unit_id = 1
        # ---------------------------------------------- >> create widgets & run application  <<
        self.create_widgets()
        self.root.mainloop()
        

    def create_widgets(self):
        # ------------------------------------------------------------- >> units option menu  <<
        variable = StringVar(self.root)
        variable.set(self.unit_choices[1][0])
        unit_menu = OptionMenu(self.root, variable, *self.unit_choices[1], command = self.set_unit)
        unit_menu.pack()
        

    def get_units(self, conn):
        # ----------------------------------- >> fetch data <<
        cur = conn.cursor()
        cur.execute('SELECT * FROM units;')
        records = cur.fetchall()
        # ----------------------- >> place data in 2d array <<
        ids = [row[0] for row in records]
        units = [row[1] for row in records]
        
        return [ids, units]


    def set_unit(self, arg):
        index = self.unit_choices[1].index(arg)
        self.unit_id =self.unit_choices[0][index]
        print(self.unit_id)
        return None


# ================================================================================================== >> main code <<
if __name__ == '__main__':
    main()
