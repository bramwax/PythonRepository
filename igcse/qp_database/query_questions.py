import tkinter as tk
from tkinter import ttk
import sqlite3

class Query_Frame(ttk.Frame):

    def __init__(self, parent): # ------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create frame <<
        ttk.LabelFrame.__init__(self, parent, text = "  Query by Objective  ")

        # ---------- >> connect to database <<
        self.conn = sqlite3.connect('0478_past_papers.db')

        # ---------- >> declare & assign variables <<
        self.unit_choices = self.get_units()
        self.unit_id = None
        self.subunit_choices = None
        self.subunit_id = None
        self.objective_choices = None
        self.objective_id = None

        # ---------- >> create widgets <<
        self.widgets()

    def widgets(self):

        # ---------- >> units label & combobox  <<
        ttk.Label(self, text = 'Select Unit',
                  font = 'Arial 12').place(x = 27, y = 20, anchor = 'nw')

        self.units_cb = ttk.Combobox(self,
                                     values = self.unit_choices[1],
                                     state  = 'readonly',
                                     width  = 60)
        self.units_cb.place(x = 28, y = 48, anchor = 'nw')
        self.units_cb.bind('<<ComboboxSelected>>', self.set_unit)

        # ---------- >> subunits label & combobox  <<
        tk.Label(self, text = 'Select Subunit',
                  font = 'Arial 12').place(x = 27, y = 86, anchor = 'nw')

        self.subunits_cb = ttk.Combobox(self,
                                        value = [],
                                        state = 'readonly',
                                        width = 60)
        self.subunits_cb.place(x = 28, y = 116, anchor = 'nw')
        self.subunits_cb.bind('<<ComboboxSelected>>', self.set_subunit)

        # ---------- >> objectives label & combobox  <<
        tk.Label(self, text = 'Select Objective',
                  font = 'Arial 12').place(x = 27, y = 152, anchor = 'nw')

        self.objectives_cb = ttk.Combobox(self,
                                          value = [],
                                          state = 'readonly',
                                          width = 60)
        self.objectives_cb.place(x = 28, y = 182, anchor = 'nw')
        self.objectives_cb.bind('<<ComboboxSelected>>', self.set_objective)

        # ---------- >> questions label, table & scrollbar  <<
        tk.Label(self, text = 'RESULTS (questions by objective)',
                  font = 'Arial 12').place(x = 27, y = 248, anchor = 'nw')
        
        columns = ('#1','#2','#3','#4','#5','#6')
        self.questions_tv = ttk.Treeview(self,
                                         selectmode = 'browse',
                                         columns = columns,
                                         show='headings',
                                         height = 14)

        self.questions_tv.heading('#1', anchor='w',   text = 'Year')
        self.questions_tv.heading('#2', anchor='w',   text = 'Session')
        self.questions_tv.heading('#3', anchor='w',   text = 'Paper')
        self.questions_tv.heading('#4', anchor='w',   text = 'Question')
        self.questions_tv.heading('#5', anchor='w',   text = 'Mark')
        self.questions_tv.heading('#6', anchor = 'w', text = 'Note')
        
        self.questions_tv.column( '#1', width = 44)
        self.questions_tv.column( '#2', width = 70)
        self.questions_tv.column( '#3', width = 54)
        self.questions_tv.column( '#4', width = 74)
        self.questions_tv.column( '#5', width = 46)
        self.questions_tv.column( '#6', width=590)
        self.questions_tv.place(x = 30, y = 280)

        self.questions_scrollbar = ttk.Scrollbar(self,
                                       orient="vertical",
                                       command = self.questions_tv.yview)
        self.questions_scrollbar.place(x = 911, y = 276, height = 306)
        self.questions_tv.configure(yscrollcommand = self.questions_scrollbar.set)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_unit(self, event): # ----------------------------------------------------------------------------------------------- >> unit selected (event) <<
        
        # ---------- >> reset/clear all non-related variables & widgets <<
        self.subunit_id = None
        self.objective_id = None

        self.subunits_cb.set([])
        self.objectives_cb.set([])
        self.questions_tv.delete(*self.questions_tv.get_children())

        # ---------- >> get & set unit_id selected
        index = self.unit_choices[1].index(self.units_cb.get())
        self.unit_id = self.unit_choices[0][index]

        # ---------- >> get & set subunit <<
        subunits = self.get_subunits()

        if len(subunits[0]) == 0:

            # ---------- >> clear subunit_id & display message <<
            self.subunit_id = None
            self.subunits_cb.set('This unit has no subunits...')

            # ---------- >> populate objectives combobox <<
            self.objective_choices = self.get_objectives()
            self.objectives_cb.config(value = self.objective_choices[1])
            
        else:
            self.subunit_choices = self.get_subunits()
            self.subunits_cb.config(value = self.subunit_choices[1])

    def set_subunit(self, event): # ----------------------------------------------------------------------------------------- >> subunit selected (event) <<

        # ---------- >> reset/clear all non-related widgets <<
        self.objective_id = None
        self.objectives_cb.set([])

        self.questions_tv.delete(*self.questions_tv.get_children())

        # ---------- >> calculate & update subunit_id <<
        index = self.subunit_choices[1].index(self.subunits_cb.get())
        self.subunit_id = self.subunit_choices[0][index]

        # ---------- >> populate objectives combobox <<
        self.objective_choices = self.get_objectives()
        self.objectives_cb.config(value = self.objective_choices[1])

    def set_objective(self, event): # ------------------------------------------------------------------------------------- >> objective selected (event) <<

        # ---------- >> reset/clear questions table <<
        self.questions_tv.delete(*self.questions_tv.get_children())

        # ---------- >> calculate & update objective_id <<
        index = self.objective_choices[1].index(self.objectives_cb.get())
        self.objective_id = self.objective_choices[0][index]

        # ---------- >> clear & re-populate questions_tv (if qry triggered) <<
        self.questions_tv.delete(*self.questions_tv.get_children())
        questions = self.get_questions()
        for records in questions:
            self.questions_tv.insert("",'end',text = "L1", values = records)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_units(self): # ------------------------------------------------------------------------------------ >> fetch & process all unit records (sql) <<
        
        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        cur.execute('''SELECT *
                       FROM units;''')
        records = cur.fetchall()

        # ---------- >> place data in 2d array <<
        ids = [row[0] for row in records]
        units = [row[1] for row in records]

        return [ids, units]

    def get_subunits(self): # -------------------------------------------------------- >> fetch & process subunit records relating to unit selected (sql) <<
        
        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        cur.execute(f'''SELECT DISTINCT(subunits.subunit_id), subunits.subunit
                        FROM subunits
                        JOIN objectives ON subunits.subunit_id = objectives.subunit_fk
                        WHERE objectives.unit_fk = {self.unit_id};''')
        records = cur.fetchall()

        # ---------- >> place data in 2d array <<
        ids = [row[0] for row in records]
        subunits = [row[1] for row in records]

        return [ids, subunits]

    def get_objectives(self):  # --------------------------------------- >> fetch & process objectives records relating to unit or subunit selected (sql) <<
        
        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        sql = f'''SELECT objectives.objective_id, objectives.objective
                  FROM objectives
                  WHERE objectives.unit_fk = {self.unit_id};'''

        # ---------- >> check if unit has subunits <<
        if self.subunit_id != None:
            sql = sql[:-1] + f' AND objectives.subunit_fk = {self.subunit_id};'
        cur.execute(sql)
        records = cur.fetchall()

        # ---------- >> place data in 2d array <<
        ids = [row[0] for row in records]
        objectives = [row[1] for row in records]

        return [ids, objectives]

    def get_questions(self): # ------------------------------------------------------------ >> fetch question records related to objective selected (sql) <<

        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        cur.execute(f'''SELECT papers.year, papers.session, papers.paper_no,
                        questions.question_number, questions.mark, questions.note
                        FROM questions
                        JOIN papers ON papers.paper_id = questions.paper_fk
                        WHERE questions.objective_fk = {self.objective_id};''')

        return cur.fetchall()
