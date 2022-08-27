# ====================================================================================================== >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# https://www.pythontutorial.net/tkinter/
# Tkinter Class Based Windows: https://youtu.be/RkaekNkIKNY
# =================================================================================================================== <<
import tkinter as tk
from tkinter import ttk
import sqlite3


class Application:
    def __init__(self, root):

        self.root = root
        # ------------------------------ >> connect database <<
        self.conn = sqlite3.connect('0478_past_papers.db')
        
        # ------------------------------ >> declare variables <<
        self.unit_choices = self.get_units(self.conn)
        self.unit_id = None
        self.subunit_choices = None
        self.subunit_id = None
        self.objective_choices = None
        self.objective_id = None
        # ------------------------------ >> create widgets & run application  <<
        self.create_widgets()
        self.root.mainloop()


    # ============================================================================================= >> create widgets <<
    def create_widgets(self):

        # ------------------------------ >> units label & dropdown  <<
        self.units_lb = tk.Label(self.root, text = 'Select a unit...')
        self.units_lb.pack(side = tk.TOP, anchor = tk.NW, padx = (20,0), pady = (20,5))
        
        self.units_cb = ttk.Combobox(self.root,
                                     values = self.unit_choices[1],
                                     state  = 'readonly',
                                     width  = 60)
        self.units_cb.pack(side = tk.TOP, anchor = tk.NW, padx = (22,20), pady = (0,0))
        self.units_cb.bind('<<ComboboxSelected>>', self.set_unit)
        
        # ------------------------------ >> subunits label & dropdown  <<
        self.subunits_lb = tk.Label(self.root, text = 'Select a subunit...')
        self.subunits_lb.pack(side = tk.TOP, anchor = tk.NW, padx = (20,0), pady = (5,5))
        
        self.subunits_cb = ttk.Combobox(self.root,
                                        value = [],
                                        state = 'readonly',
                                        width = 60)
        self.subunits_cb.pack(side = tk.TOP, anchor = tk.NW, padx = (22,20), pady = (0,0))
        self.subunits_cb.bind('<<ComboboxSelected>>', self.set_subunit)
        
        # ------------------------------ >> objectives label & dropdown  <<
        self.objectives_lb = tk.Label(self.root, text = 'Select a subunit')
        self.objectives_lb.pack(side = tk.TOP, anchor = tk.NW, padx = (20,0), pady = (5,5))
        
        self.objectives_cb = ttk.Combobox(self.root,
                                          value = [],
                                          state = 'readonly',
                                          width = 60)
        self.objectives_cb.pack(side = tk.TOP, anchor = tk.NW, padx = (22,20), pady = (0,0))
        self.objectives_cb.bind('<<ComboboxSelected>>', self.set_objective)
        
        # ------------------------------ >> questions label, scrollbar, table  <<
        self.objectives_lb = tk.Label(self.root, text = 'Questions by objective')
        self.objectives_lb.pack(side = tk.TOP, anchor = tk.NW, padx = (20,0), pady = (20,5))

        columns = ('#1','#2','#3','#4','#5','#6')
        self.questions_tv = ttk.Treeview(self.root,
                                         selectmode='browse',
                                         columns=columns,
                                         show='headings',
                                         height=16)

        self.scrollbar = ttk.Scrollbar(self.root,
                                       orient="vertical",
                                       command = self.questions_tv.yview)
        self.scrollbar.place(x = 925, y = 217, height = 346)
        self.questions_tv.configure(yscrollcommand = self.scrollbar.set)

        self.questions_tv.heading('#1', anchor='w', text = 'Year')
        self.questions_tv.heading('#2', anchor='w', text = 'Session')
        self.questions_tv.heading('#3', anchor='w', text = 'Paper')
        self.questions_tv.heading('#4', anchor='w', text = 'Question')
        self.questions_tv.heading('#5', anchor='w', text = 'Mark')
        self.questions_tv.heading('#6', anchor = 'w', text = 'Note')
        
        self.questions_tv.column('#1', minwidth = 0, width = 50)
        self.questions_tv.column('#2', minwidth = 0, width = 70)
        self.questions_tv.column('#3', minwidth = 0, width = 50)
        self.questions_tv.column('#4', minwidth = 0, width = 80)
        self.questions_tv.column('#5', minwidth = 0, width = 50)
        self.questions_tv.column('#6', minwidth = 0, width=600)
        self.questions_tv.pack(side = tk.TOP, anchor = tk.NW, padx = (22,20), pady = (0,0))

        '''
        for i in range(16):
            self.questions_tv.insert("",'end',text="L1",values=('col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6'))
        self.questions_tv.insert("",'end',text="L1",values=('col_11', 'col_22', 'col_33', 'col_44', 'col_55', 'col_66'))
        '''

    # ==================================================================================================== >> methods <<
    def get_units(self, conn):
        
        # ------------------------------ >> fetch data <<
        cur = conn.cursor()
        cur.execute('''SELECT *
                       FROM units;''')
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


    def get_objectives(self, conn):
        
        # ------------------------------ >> fetch data <<
        cur = conn.cursor()
        sql = f'''SELECT objectives.objective_id, objectives.objective
                        FROM objectives
                        WHERE objectives.unit_fk = {self.unit_id};'''
        # ------------------------------ >> check if unit has subunits <<        
        if self.subunit_id != None:
            sql = sql[:-1] + f' AND objectives.subunit_fk = {self.subunit_id};'
        cur.execute(sql)
        records = cur.fetchall()
        # ------------------------------ >> place data in 2d array <<
        ids = [row[0] for row in records]
        objectives = [row[1] for row in records]
        return [ids, objectives]

    def get_questions(self, conn):
        return 'Get_questions!'


    # ===================================================================================================== >> events <<
    def set_unit(self, event):
        
        # ------------------------------ >> calculate & update unit_id <<
        index = self.unit_choices[1].index(self.units_cb.get())
        self.unit_id = self.unit_choices[0][index]

        # ------------------------------ >> delete subunit_id, clear & re-populate subunits_cb <<
        self.subunit_id = None
        self.subunits_cb.set([])
        self.subunit_choices = self.get_subunits(self.conn)
        self.subunits_cb.config(value=self.subunit_choices[1])

        # ------------------------------ >> clear objectives_cb <<
        self.objectives_cb.set([])
        
        # ------------------------------ >> check if ther are subunits <<
        if len(self.subunit_choices[0]) == 0:
            self.subunit_id = None
            self.subunits_cb.set('This unit has no subunits...')
            self.objective_choices = self.get_objectives(self.conn)
            self.objectives_cb.config(value=self.objective_choices[1])
        else:
            self.objective_id = None
            self.objectives_cb.config(value=[])

        print(self.unit_id, self.subunit_id, self.objective_id)


    def set_subunit(self, event):
        
        # ------------------------------ >> calculate & update subunit_id <<
        index = self.subunit_choices[1].index(self.subunits_cb.get())
        self.subunit_id = self.subunit_choices[0][index]

        # ------------------------------ >> delete objective_id, clear & re-populate objectives_cb <<
        self.objective_id = None
        self.objectives_cb.set([])
        self.objective_choices = self.get_objectives(self.conn)
        self.objectives_cb.config(value = self.objective_choices[1])

        print(self.unit_id, self.subunit_id, self.objective_id)


    def set_objective(self, event):

        # ------------------------------ >> calculate & update objective_id <<
        index = self.objective_choices[1].index(self.objectives_cb.get())
        self.objective_id = self.objective_choices[0][index]

        print(self.get_questions(self.conn))
        print(self.unit_id, self.subunit_id, self.objective_id)

# ====================================================================================================== >> main code <<
root = tk.Tk()
root.geometry('962x586')
root.resizable(False, False)
root.iconbitmap('favicon.ico')
root.title(' Past paper exam questions database | Cambridge IGCSE Computer Science (0478)')
app = Application(root)
