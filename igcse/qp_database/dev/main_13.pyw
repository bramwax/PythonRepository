import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3


class Application:

    def __init__(self, root): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        self.root = root
        
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

        self.ins_unit_choices = self.get_units()
        self.ins_unit_id = None
        
        # ---------- >> initiate creation of gui elements <<
        self.set_styles()
        self.create_tabs()

        # ---------- >> run application  <<
        self.root.mainloop()

    def set_styles(self): # -------------------------------------------------------------------------------------------------------- >> set widget styles <<
          
        style = ttk.Style()
        style.configure('Treeview', font = ('Arial','11'), fieldbackground="#ffc61e")
        style.configure("Treeview.Heading", font = ('Arial','11'))
        style.configure('TNotebook.Tab', font = ('Arial','11'))
        style.configure('TEntry', padding = '3 3 3 3')
        style.configure('TCombobox', padding = '3 3 3 3')

    def create_tabs(self): # ---------------------------------------------------------------------------------------------------- >> create tabs (frames) <<
        
        # ---------- >> create notebook (tab frames) <<
        self.tab_control = ttk.Notebook(self.root)
        
        self.qry_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.qry_tab, text = '  QUERY  ')
        
        self.ins_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.ins_tab, text = '  INSERT  ')

        self.tab_control.pack(expand = 1, fill = 'both', padx = 20, pady = 20)

        # ---------- >> add tab elements (widgets) <<
        self.qry_widgets()
        self.ins_widgets()

    def qry_widgets(self): # -------------------------------------------------------------------------------------------- >> populate query tab (widgets) <<

        # ---------- >> units label & combobox  <<
        ttk.Label(self.qry_tab, text = 'Select Unit...').place(x = 16, y = 20, anchor = 'nw')

        self.qry_units_cb = ttk.Combobox(self.qry_tab,
                                     values = self.unit_choices[1],
                                     state  = 'readonly',
                                     width  = 60)
        
        self.qry_units_cb.place(x = 18, y = 46, anchor = 'nw')        
        #self.qry_units_cb.bind('<<ComboboxSelected>>', self.set_unit)
        self.qry_units_cb.bind('<<ComboboxSelected>>', lambda event: self.set_unit(event, 'qry'))

        # ---------- >> subunits label & combobox  <<
        tk.Label(self.qry_tab, text = 'Select Subunit.').place(x = 16, y = 86, anchor = 'nw')

        self.qry_subunits_cb = ttk.Combobox(self.qry_tab,
                                        value = [],
                                        state = 'readonly',
                                        width = 60)
        
        self.qry_subunits_cb.place(x = 18, y = 112, anchor = 'nw')
        #self.qry_subunits_cb.bind('<<ComboboxSelected>>', self.set_subunit)
        self.qry_subunits_cb.bind('<<ComboboxSelected>>', lambda event: self.set_subunit(event, 'qry'))

        # ---------- >> objectives label & combobox  <<
        tk.Label(self.qry_tab, text = 'Select Objective').place(x = 16, y = 152, anchor = 'nw')

        self.qry_objectives_cb = ttk.Combobox(self.qry_tab,
                                          value = [],
                                          state = 'readonly',
                                          width = 60)
        self.qry_objectives_cb.place(x = 18, y = 178, anchor = 'nw')
        self.qry_objectives_cb.bind('<<ComboboxSelected>>', lambda event: self.set_objective(event, 'qry'))

        # ---------- >> separator  <<
        ttk.Separator(self.qry_tab).place(x = 12, y = 230, width = 930)

        # ---------- >> questions label, table & scrollbar  <<
        tk.Label(self.qry_tab, text = 'Questions by Objective').place(x = 16, y = 246, anchor = 'nw')
        
        columns = ('#1','#2','#3','#4','#5','#6')
        self.questions_tv = ttk.Treeview(self.qry_tab,
                                         selectmode='browse',
                                         columns=columns,
                                         show='headings',
                                         height=12)

        self.questions_tv.heading('#1', anchor='w',   text = 'Year')
        self.questions_tv.heading('#2', anchor='w',   text = 'Session')
        self.questions_tv.heading('#3', anchor='w',   text = 'Paper')
        self.questions_tv.heading('#4', anchor='w',   text = 'Question')
        self.questions_tv.heading('#5', anchor='w',   text = 'Mark')
        self.questions_tv.heading('#6', anchor = 'w', text = 'Note')
        
        self.questions_tv.column( '#1', width = 50)
        self.questions_tv.column( '#2', width = 70)
        self.questions_tv.column( '#3', width = 50)
        self.questions_tv.column( '#4', width = 80)
        self.questions_tv.column( '#5', width = 50)
        self.questions_tv.column( '#6', width=600)
        self.questions_tv.place(x = 20, y = 276)

        self.questions_scrollbar = ttk.Scrollbar(self.qry_tab,
                                       orient="vertical",
                                       command = self.questions_tv.yview)
        self.questions_scrollbar.place(x = 923, y = 275, height = 268)
        self.questions_tv.configure(yscrollcommand = self.questions_scrollbar.set)

    def ins_widgets(self): # ------------------------------------------------------------------------------------------- >> populate insert tab (widgets) <<

        # ---------- >> tab headings & separators  <<
        ttk.Label(self.ins_tab, text = 'QUESTION', font = 'Arial 11 bold').place(x = 26, y = 22, anchor = 'nw')
        ttk.Label(self.ins_tab, text = '(select paper and set options below)').place(x = 110, y = 22, anchor = 'nw')

        ttk.Separator(self.ins_tab, orient='vertical').place(x = 590, y = 16, height = 326)
        ttk.Separator(self.ins_tab, orient='horizontal').place(x = 590, y = 340, width = 340)

        ttk.Label(self.ins_tab, text = 'PAPER', font = 'Arial 11 bold').place(x = 614, y = 22, anchor = 'nw')

        # ---------- >> units label & combobox  <<
        ttk.Label(self.ins_tab, text = 'Unit:').place(x = 96, y = 66, anchor = 'ne')

        self.ins_units_cb = ttk.Combobox(self.ins_tab,
                                         values = self.ins_unit_choices[1],
                                         state  = 'readonly',
                                         width  = 51)
        
        self.ins_units_cb.place(x = 102, y = 63, anchor = 'nw')        
        self.ins_units_cb.bind('<<ComboboxSelected>>', lambda event: self.set_unit(event, 'ins'))

        # ---------- >> subunits label & combobox  <<
        tk.Label(self.ins_tab, text = 'Subunit:').place(x = 96, y = 110, anchor = 'ne')

        self.ins_subunits_cb = ttk.Combobox(self.ins_tab,
                                        value = [],
                                        state = 'readonly',
                                        width = 51)
        
        self.ins_subunits_cb.place(x = 102, y = 107, anchor = 'nw')
        self.ins_subunits_cb.bind('<<ComboboxSelected>>', lambda event: self.set_subunit(event, 'ins'))

        # ---------- >> objectives label & combobox  <<
        tk.Label(self.ins_tab, text = 'Objective:').place(x = 96, y = 157, anchor = 'ne')

        self.ins_objectives_cb = ttk.Combobox(self.ins_tab,
                                          value = [],
                                          state = 'readonly',
                                          width = 51)

        self.ins_objectives_cb.place(x = 102, y = 154, anchor = 'nw')
        self.ins_objectives_cb.bind('<<ComboboxSelected>>', lambda event: self.set_objective(event, 'ins'))

        # ---------- >> question number label & input field  <<
        ttk.Label(self.ins_tab, text = 'Question:').place(x = 96, y = 204, anchor = 'ne')

        self.question_et = ttk.Entry(self.ins_tab, width = 5)
        self.question_et.place(x = 102, y = 202, anchor = 'nw')

        # ---------- >> mark label & input field  <<
        ttk.Label(self.ins_tab, text = 'Mark:').place(x = 176, y = 204, anchor = 'nw')

        self.mark_et = ttk.Entry(self.ins_tab, width = 4)
        self.mark_et.place(x = 218, y = 202, anchor = 'nw')

        # ---------- >> note label & input field  <<
        ttk.Label(self.ins_tab, text = 'Note:').place(x = 96, y = 251, anchor = 'ne')

        self.note_et = ttk.Entry(self.ins_tab, width = 53)
        self.note_et.place(x = 102, y = 249, anchor = 'nw')

        # ---------- >> insert question button  <<
        self.question_bt = tk.Button(self.ins_tab,
                                  text = 'Insert Question',
                                  bg = '#f8f8f8',
                                  width = 47, height = 2,
                                  command = self.check_new_question)
        self.question_bt.place(x = 102, y = 294, anchor = 'nw')

        # ---------- >> questions table & scrollbar <<
        columns = ('#1','#2','#3','#4','#5','#6')
        self.questions_tv = ttk.Treeview(self.ins_tab,
                                         selectmode = 'browse',
                                         columns=columns,
                                         show='headings',
                                         height = 7)

        self.questions_tv.heading('#1', anchor='w', text = 'Question_Id')
        self.questions_tv.heading('#2', anchor='w', text = 'Question_No')
        self.questions_tv.heading('#3', anchor='w', text = 'Mark')
        self.questions_tv.heading('#4', anchor='w', text = 'Note')
        self.questions_tv.heading('#5', anchor='w', text = 'Paper_Id')
        self.questions_tv.heading('#6', anchor='w', text = 'Objective_Id')

        self.questions_tv.column( '#1', width = 94)
        self.questions_tv.column( '#2', width = 100)
        self.questions_tv.column( '#3', width = 50)
        self.questions_tv.column( '#4', width = 455)
        self.questions_tv.column( '#5', width = 76)
        self.questions_tv.column( '#6', width = 94)
        self.questions_tv.place(x = 26, y = 370)
        
        self.questions_scrollbar = ttk.Scrollbar(self.ins_tab,
                                             orient="vertical",
                                             command = self.questions_tv.yview)
        self.questions_scrollbar.place(x = 898, y = 370, height = 167)

        self.questions_tv.configure(yscrollcommand = self.questions_scrollbar.set)

        # ---------- >> populate questions <<
        self.set_questions()

        # =============================================================================================================

        # ---------- >> papers table & scrollbar <<
        columns = ('#1','#2','#3','#4')
        self.papers_tv = ttk.Treeview(self.ins_tab,
                                         selectmode = 'browse',
                                         columns=columns,
                                         show='headings',
                                         height = 4)

        self.papers_tv.heading('#1', anchor='w', text = 'Paper_Id')
        self.papers_tv.heading('#2', anchor='w', text = 'Year')
        self.papers_tv.heading('#3', anchor='w', text = 'Session')
        self.papers_tv.heading('#4', anchor='w', text = 'Paper_No')

        self.papers_tv.column( '#1', width = 80)
        self.papers_tv.column( '#2', width = 50)
        self.papers_tv.column( '#3', width = 70)
        self.papers_tv.column( '#4', width = 80)
        self.papers_tv.place(x = 615, y = 65)
        
        self.papers_scrollbar = ttk.Scrollbar(self.ins_tab,
                                             orient="vertical",
                                             command = self.papers_tv.yview)
        self.papers_scrollbar.place(x = 898, y = 64, height = 107)

        self.papers_tv.configure(yscrollcommand = self.papers_scrollbar.set)
        self.papers_tv.bind('<ButtonRelease-1>', self.set_insert_paper)

        # ---------- >> populate papers <<
        self.set_papers()

        # ---------- >> year label & text entry  <<
        ttk.Label(self.ins_tab, text = 'Year:').place(x = 684, y = 204, anchor = 'ne')

        self.year_et = ttk.Entry(self.ins_tab, width = 5)
        self.year_et.place(x = 690, y = 202, anchor = 'nw')

        # ---------- >> session label & combobox  <<
        ttk.Label(self.ins_tab, text = 'Session:').place(x = 684, y = 252, anchor = 'ne')

        self.session_cb = ttk.Combobox(self.ins_tab,
                                       value = ['spring', 'summer', 'winter'],
                                       state = 'readonly',
                                       width = 8)
        self.session_cb.place(x = 690, y = 249, anchor = 'nw')

        # ---------- >> paper label & combobox  <<
        ttk.Label(self.ins_tab, text = 'Paper:').place(x = 684, y = 286, anchor = 'ne')

        self.paper_cb = ttk.Combobox(self.ins_tab,
                                       value = ['11', '12','13', '21', '22','23', '01', '02'],
                                       state = 'readonly',
                                       width = 3)
        self.paper_cb.place(x = 690, y = 294, anchor = 'nw')

        # ---------- >> insert paper button  <<
        self.paper_bt = tk.Button(self.ins_tab,
                                  text = 'Insert\nPaper',
                                  bg = '#f8f8f8',
                                  width = 9, height = 6,
                                  command = self.check_new_paper)
        self.paper_bt.place(x = 805, y = 202, anchor = 'nw')

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_papers(self): # ---------------------------------------------------------------------------------------------------- >> populate papers table <<

        # ---------- fetch data
        papers = self.get_all_papers()

        # ---------- >> clear & repopulate papers table <<
        self.papers_tv.delete(*self.papers_tv.get_children())
        for records in papers:
            self.papers_tv.insert("", 'end', text = "L1", values = records)
        
        return None

    def set_questions(self):

        # ---------- fetch data
        questions = self.get_all_questions()

        # ---------- >> clear & repopulate questions table <<
        self.questions_tv.delete(*self.questions_tv.get_children())
        for records in questions:
            self.questions_tv.insert("", 'end', text = "L1", values = records)

        return None

    def check_new_paper(self): # -------------------------------------------------------------------- >> check paper parameters & insert or display error <<
        
        # get necessary data from widgets
        year = self.year_et.get()
        session = self.session_cb.get()
        paper = self.paper_cb.get()

        if year != '' and session != '' and paper != '':
            duplicate = self.count_papers(year, session, paper)
            
            if duplicate == 0:
                self.insert_paper(year, session, paper)
                self.set_papers()
                tkinter.messagebox.showinfo('Success!', 'New paper inserted')
            else:
                tkinter.messagebox.showinfo('Error', 'That paper already exists!')

        else:
                tkinter.messagebox.showinfo('Error', 'You must fill in all fields!')

    def check_new_question(self):

        # get necessary data from widgets
        question = self.question_et.get()
        mark = self.mark_et.get()
        note = self.note_et.get()
        paper = self.paper_selected
        objective = self.objective_id

        print(f'Q: {question} | M: {mark} | N: {note} | P: {paper} | O: {objective}')

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_unit(self, event, trigger): # ----------------------------------------------------------------------------------------------- >> unit selected (event) <<
        
        # ---------- >> reset/clear all non-related widgets <<
        if trigger == 'qry':
            self.ins_units_cb.set('')
        else: 
            self.qry_units_cb.set('')

        self.subunit_id = None
        self.qry_subunits_cb.set([])
        self.ins_subunits_cb.set([])

        self.objective_id = None
        self.qry_objectives_cb.set([])
        self.ins_objectives_cb.set([])

        self.questions_tv.delete(*self.questions_tv.get_children())

        # ---------- >> get & set unit_id selected

        index = eval(f'self.unit_choices[1].index(self.{trigger}_units_cb.get())')
        self.unit_id = self.unit_choices[0][index]

        # ---------- >> get & set subunit <<
        subunits = self.get_subunits()

        if len(subunits[0]) == 0:

            # ---------- >> clear subunit_id & display message <<
            self.subunit_id = None
            eval(f"self.{trigger}_subunits_cb.set('This unit has no subunits...')")

            # ---------- >> populate objectives combobox <<
            self.objective_choices = self.get_objectives()
            eval(f'self.{trigger}_objectives_cb.config(value = self.objective_choices[1])')

        else:

            self.subunit_choices = self.get_subunits()
            eval(f'self.{trigger}_subunits_cb.config(value = self.subunit_choices[1])')

    def set_subunit(self, event, trigger): # ----------------------------------------------------------------------------------------- >> subunit selected (event) <<

        # ---------- >> reset/clear all non-related widgets <<
        if trigger == 'qry':
            self.ins_subunits_cb.set('')
        else: 
            self.qry_subunits_cb.set('')

        self.objective_id = None
        self.qry_objectives_cb.set([])
        self.ins_objectives_cb.set([])

        self.questions_tv.delete(*self.questions_tv.get_children())

        # ---------- >> calculate & update subunit_id <<
        index = eval(f'self.subunit_choices[1].index(self.{trigger}_subunits_cb.get())')
        self.subunit_id = self.subunit_choices[0][index]

        # ---------- >> populate objectives combobox <<
        self.objective_choices = self.get_objectives()
        eval(f'self.{trigger}_objectives_cb.config(value = self.objective_choices[1])')

    def set_objective(self, event, trigger): # ------------------------------------------------------------------------------------- >> objective selected (event) <<

        # ---------- >> reset/clear questions table <<
        self.questions_tv.delete(*self.questions_tv.get_children())

        # ---------- >> calculate & update objective_id <<
        index = eval(f'self.objective_choices[1].index(self.{trigger}_objectives_cb.get())')
        self.objective_id = self.objective_choices[0][index]

        # ---------- >> clear & re-populate questions_tv (if qry triggered) <<
        if trigger == 'qry':
            self.questions_tv.delete(*self.questions_tv.get_children())
            questions = self.get_questions()
            for records in questions:
                self.questions_tv.insert("",'end',text = "L1", values = records)

        print(f'Tab: {trigger.upper()} | Unit: {self.unit_id} | Subunit: {self.subunit_id} | Objective: {self.objective_id}')

    def set_insert_paper(self, event): # -------------------------------------------------------------------------------------- >> paper selected (event) <<

        paper_selected = self.papers_tv.focus()
        self.paper_selected = self.papers_tv.item(paper_selected)['values'][0]

        print(f'Paper: {self.paper_selected}')

        return None

    # ------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_units(self): # ------------------------------------------------------------------------------------- >> fetch & process all unit records (sql) <<
        
        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        cur.execute('''SELECT *
                       FROM units;''')
        records = cur.fetchall()
        
        # ---------- >> place data in 2d array <<
        ids = [row[0] for row in records]
        units = [row[1] for row in records]

        return [ids, units]

    def get_subunits(self): # --------------------------------------------------------- >> fetch & process subunit records relating to unit selected (sql) <<
        
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

    def get_objectives(self):  # ---------------------------------------- >> fetch & process objectives records relating to unit or subunit selected (sql) <<
        
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

    def get_questions(self): # ------------------------------------------------------------- >> fetch question records related to objective selected (sql) <<

        # ---------- >> fetch data <<     
        cur = self.conn.cursor()
        cur.execute(f'''SELECT papers.year, papers.session, papers.paper_no,
                        questions.question_number, questions.mark, questions.note
                        FROM questions
                        JOIN papers ON papers.paper_id = questions.paper_fk
                        WHERE questions.objective_fk = {self.objective_id};''')

        return cur.fetchall()

    def get_all_questions(self):

        # ---------- fetch data
        cur = self.conn.cursor()
        cur.execute('''SELECT *
					   FROM questions
					   ORDER BY question_id DESC;''')

        return cur.fetchall()

    def get_all_papers(self): # --------------------------------------------------------------------------------------------- >> fetch all paper records (sql) <<

        # ---------- fetch data
        cur = self.conn.cursor()
        cur.execute('''SELECT *
					   FROM papers
					   ORDER BY paper_id DESC;''')

        return cur.fetchall()

    def count_papers(self, year, session, paper): # --------------------------------------- >> fetch count paper records based on parameters supplied (sql) <<
        
        # ---------- >> fetch data <<
        cur = self.conn.cursor()
        cur.execute(f'''SELECT COUNT(*)
                        FROM papers
                        WHERE year   ={year}
                        AND session  = '{session}'
                        AND paper_no = '{paper}';''')
        
        return cur.fetchall()[0][0]

    def insert_paper(self, year, session, paper): # ----------------------------------------------------------------------------- >> insert new paper (sql) <<

        cur = self.conn.cursor()
        cur.execute(f'''INSERT INTO papers (year, session, paper_no)
					    VALUES ({year},'{session}','{paper}');''')
        
        self.conn.commit()

        return None

    def insert_question(self, question_number, mark, note, paper, objective):

        cur = self.conn.cursor()
        cur.execute(f'''INSERT INTO questions (question_number, mark, note, paper_fk, objective_fk)
					    VALUES ({question_number},'{mark}','{note}','{paper}','{objective}');''')
        
        self.conn.commit()
        
        return None


# ========================================================================================================================================== >> main code <<
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.geometry('1000x630')
root.resizable(False, False)
root.option_add( '*font', 'Arial 11' )
root.iconbitmap('favicon.ico')
root.title(' Past paper exam questions database | Cambridge IGCSE Computer Science (0478)')
app = Application(root)