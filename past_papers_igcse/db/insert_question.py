import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class Question_Frame(ttk.Frame):

    def __init__(self, parent): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        ttk.LabelFrame.__init__(self, parent, text = "  Insert Question  ")
        self.parent = parent

        # ---------- >> connect to database <<
        self.conn = sqlite3.connect('0478_past_papers.db')

        # ---------- >> declare & assign variables <<
        self.unit_choices = self.get_units()
        self.unit_id = None
        self.subunit_choices = None
        self.subunit_id = None
        self.objective_choices = None
        self.objective_id = None
        self.paper_selected = None

        # ---------- >> initiate creation & style of gui elements <<
        self.widgets()

    def widgets(self):

        # ---------- >> units label & combobox  <<
        ttk.Label(self, text = 'Unit:').place(x = 96, y = 31, anchor = 'ne')

        self.units_cb = ttk.Combobox(self,
                                         values = self.unit_choices[1],
                                         state  = 'readonly',
                                         width  = 51)
        
        self.units_cb.place(x = 102, y = 28, anchor = 'nw')        
        self.units_cb.bind('<<ComboboxSelected>>', lambda event: self.set_unit(event))

        # ---------- >> subunits label & combobox  <<
        tk.Label(self, text = 'Subunit:').place(x = 96, y = 82, anchor = 'ne')

        self.subunits_cb = ttk.Combobox(self,
                                        value = [],
                                        state = 'readonly',
                                        width = 51)
        
        self.subunits_cb.place(x = 102, y = 79, anchor = 'nw')
        self.subunits_cb.bind('<<ComboboxSelected>>', lambda event: self.set_subunit(event))


        # ---------- >> objectives label & combobox  <<
        tk.Label(self, text = 'Objective:').place(x = 96, y = 133, anchor = 'ne')

        self.objectives_cb = ttk.Combobox(self,
                                          value = [],
                                          state = 'readonly',
                                          width = 51)

        self.objectives_cb.place(x = 102, y = 130, anchor = 'nw')
        self.objectives_cb.bind('<<ComboboxSelected>>', lambda event: self.set_objective(event))

        # ---------- >> question number label & input field  <<
        ttk.Label(self, text = 'Question:').place(x = 96, y = 184, anchor = 'ne')

        self.question_et = ttk.Entry(self, width = 5)
        self.question_et.place(x = 102, y = 181, anchor = 'nw')

        # ---------- >> mark label & input field  <<
        ttk.Label(self, text = 'Mark:').place(x = 176, y = 184, anchor = 'nw')

        self.mark_et = ttk.Entry(self, width = 4)
        self.mark_et.place(x = 226, y = 181, anchor = 'nw')

        # ---------- >> note label & input field  <<
        ttk.Label(self, text = 'Note:').place(x = 96, y = 235, anchor = 'ne')

        self.note_et = ttk.Entry(self, width = 53)
        self.note_et.place(x = 102, y = 232, anchor = 'nw')

        # ---------- >> papers table & scrollbar <<
        columns = ('#1','#2','#3','#4')
        self.papers_tv = ttk.Treeview(self,
                                         selectmode = 'browse',
                                         columns=columns,
                                         show='headings',
                                         height = 14)

        self.papers_tv.heading('#1', anchor='w', text = 'Pap_Id')
        self.papers_tv.heading('#2', anchor='w', text = 'Year')
        self.papers_tv.heading('#3', anchor='w', text = 'Session')
        self.papers_tv.heading('#4', anchor='w', text = 'Pap_No')

        self.papers_tv.column( '#1', width = 60)
        self.papers_tv.column( '#2', width = 44)
        self.papers_tv.column( '#3', width = 70)
        self.papers_tv.column( '#4', width = 66)
        self.papers_tv.place(x = 615, y = 28)
        
        self.papers_scrollbar = ttk.Scrollbar(self,
                                             orient="vertical",
                                             command = self.papers_tv.yview)
        self.papers_scrollbar.place(x = 858, y = 28, height = 307)

        self.papers_tv.configure(yscrollcommand = self.papers_scrollbar.set)
        self.papers_tv.bind('<ButtonRelease-1>', self.set_paper)

        # ---------- >> populate papers <<
        self.set_papers()

        # ---------- >> insert question button  <<
        self.question_bt = tk.Button(self,
                                  text = 'Insert Question',
                                  bg = '#f8f8f8',
                                  width = 53, height = 2,
                                  command = self.check_new_question)
        self.question_bt.place(x = 102, y = 284, anchor = 'nw')

        
        # ---------- >> questions table & scrollbar <<
        columns = ('#1','#2','#3','#4','#5','#6')
        self.questions_tv = ttk.Treeview(self,
                                         selectmode = 'browse',
                                         columns=columns,
                                         show='headings',
                                         height = 8)

        self.questions_tv.heading('#1', anchor='w', text = 'Que_Id')
        self.questions_tv.heading('#2', anchor='w', text = 'Que_No')
        self.questions_tv.heading('#3', anchor='w', text = 'Mark')
        self.questions_tv.heading('#4', anchor='w', text = 'Note')
        self.questions_tv.heading('#5', anchor='w', text = 'Pap_Id')
        self.questions_tv.heading('#6', anchor='w', text = 'Obj_Id')

        self.questions_tv.column( '#1', width = 60)
        self.questions_tv.column( '#2', width = 70)
        self.questions_tv.column( '#3', width = 50)
        self.questions_tv.column( '#4', width = 519)
        self.questions_tv.column( '#5', width = 60)
        self.questions_tv.column( '#6', width = 60)
        self.questions_tv.place(x = 36, y = 370)
        
        self.questions_scrollbar = ttk.Scrollbar(self,
                                             orient="vertical",
                                             command = self.questions_tv.yview)
        self.questions_scrollbar.place(x = 858, y = 370, height = 187)

        self.questions_tv.configure(yscrollcommand = self.questions_scrollbar.set)

        # ---------- >> populate questions <<
        self.set_questions()

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_papers(self): # ---------------------------------------------------------------------------------------------------- >> populate papers table <<

        # ---------- fetch data
        papers = self.get_all_papers()

        # ---------- >> clear & repopulate papers table <<
        self.papers_tv.delete(*self.papers_tv.get_children())
        for records in papers:
            self.papers_tv.insert("", 'end', text = "L1", values = records)

    def set_questions(self):

        # ---------- fetch data
        questions = self.get_all_questions()

        # ---------- >> clear & repopulate questions table <<
        self.questions_tv.delete(*self.questions_tv.get_children())
        for records in questions:
            self.questions_tv.insert("", 'end', text = "L1", values = records)

    def check_new_question(self):

        # get necessary data from widgets
        question = self.question_et.get()
        mark = self.mark_et.get()
        note = self.note_et.get()
        paper = self.paper_selected
        objective = self.objective_id

        if question != '' and mark != '' and note != '' and paper != '' and objective != '':
            duplicate = self.count_questions(question, paper)

            if duplicate == 0:
                self.insert_question(question, mark, note, paper, objective)
                self.set_questions()
                tkinter.messagebox.showinfo('Success!', 'New question inserted', parent = self)
            else:
                tkinter.messagebox.showinfo('Error', 'That question already exists!', parent = self)

        else:
            tkinter.messagebox.showinfo('Error', 'You must fill in all fields!', parent = self)

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_unit(self, event): # ----------------------------------------------------------------------------------------------- >> unit selected (event) <<
        
        # ---------- >> reset/clear all non-related variables & widgets <<
        self.subunit_id = None
        self.objective_id = None

        self.subunits_cb.set([])
        self.objectives_cb.set([])

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

        # ---------- >> calculate & update subunit_id <<
        index = self.subunit_choices[1].index(self.subunits_cb.get())
        self.subunit_id = self.subunit_choices[0][index]

        # ---------- >> populate objectives combobox <<
        self.objective_choices = self.get_objectives()
        self.objectives_cb.config(value = self.objective_choices[1])

    def set_objective(self, event): # ------------------------------------------------------------------------------------- >> objective selected (event) <<

        # ---------- >> calculate & update objective_id <<
        index = self.objective_choices[1].index(self.objectives_cb.get())
        self.objective_id = self.objective_choices[0][index]

    def set_paper(self, event): # --------------------------------------------------------------------------------------- >> paper selected (event) <<

        paper_selected = self.papers_tv.focus()
        self.paper_selected = self.papers_tv.item(paper_selected)['values'][0]

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

    def get_all_questions(self): # ---------------------------------------------------------------------------------- >> fetch all question records (sql) <<

        # ---------- fetch data
        cur = self.conn.cursor()
        cur.execute('''SELECT *
					   FROM questions
					   ORDER BY question_id DESC;''')

        return cur.fetchall()

    def get_all_papers(self): # ---------------------------------------------------------------------------------------- >> fetch all paper records (sql) <<

        # ---------- fetch data
        cur = self.conn.cursor()
        cur.execute('''SELECT *
					   FROM papers
					   ORDER BY paper_id DESC;''')

        return cur.fetchall()

    def count_questions(self, question, paper): # --------------------------------------- >> fetch count paper records based on parameters supplied (sql) <<
        
        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        cur.execute(f'''SELECT COUNT(*)
                        FROM questions
                        WHERE question_number = '{question}'
                        AND paper_fk = '{paper}';''')
        
        return cur.fetchall()[0][0]

    def insert_question(self, question_number, mark, note, paper, objective):

        cur = self.conn.cursor()
        cur.execute(f'''INSERT INTO questions (question_number, mark, note, paper_fk, objective_fk)
					    VALUES ('{question_number}','{mark}','{note}','{paper}','{objective}');''')
        
        self.conn.commit()
