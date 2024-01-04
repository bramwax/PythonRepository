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
        
        # ---------- >> initiate creation of gui elements <<
        self.set_styles()
        self.create_tabs()

        # ---------- >> run application  <<
        self.root.mainloop()


    def set_styles(self): # -------------------------------------------------------------------------------------------------------- >> set widget styles <<
          
        style = ttk.Style()
        style.configure('Treeview', font = ('Arial','11'))
        style.configure("Treeview.Heading", font = ('Arial','11'))
        style.configure('TNotebook.Tab', font = ('Arial','11'))
        style.configure('TEntry', padding = '3 3 3 3')
        style.configure('TCombobox', padding = '3 3 3 3')


    def create_tabs(self): # ---------------------------------------------------------------------------------------------------- >> create tabs (frames) <<
        
        # ---------- >> create notebook (tab frames) <<
        self.tab_control = ttk.Notebook(self.root)
        
        self.qry_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.qry_tab, text = '  Query Database  ')
        
        self.ins_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.ins_tab, text = '  Insert Data  ')

        self.tab_control.pack(expand = 1, fill = 'both', padx = 20, pady = 20)

        # ---------- >> add tab elements (widgets) <<
        self.qry_widgets()
        self.ins_widgets()


    def qry_widgets(self): # -------------------------------------------------------------------------------------------- >> populate query tab (widgets) <<

        # ---------- >> units label & combobox  <<
        ttk.Label(self.qry_tab, text = 'Select a unit...').place(x = 16, y = 16, anchor = 'nw')

        self.units_cb = ttk.Combobox(self.qry_tab,
                                     values = self.unit_choices[1],
                                     state  = 'readonly',
                                     width  = 60)
        
        self.units_cb.place(x = 18, y = 46, anchor = 'nw')        
        self.units_cb.bind('<<ComboboxSelected>>', self.set_unit)

        # ---------- >> subunits label & combobox  <<
        tk.Label(self.qry_tab, text = 'Select a subunit...').place(x = 16, y = 82, anchor = 'nw')

        self.subunits_cb = ttk.Combobox(self.qry_tab,
                                        value = [],
                                        state = 'readonly',
                                        width = 60)
        
        self.subunits_cb.place(x = 18, y = 112, anchor = 'nw')
        self.subunits_cb.bind('<<ComboboxSelected>>', self.set_subunit)

        # ---------- >> objectives label & combobox  <<
        tk.Label(self.qry_tab, text = 'Select an objective').place(x = 16, y = 148, anchor = 'nw')

        self.objectives_cb = ttk.Combobox(self.qry_tab,
                                          value = [],
                                          state = 'readonly',
                                          width = 60)
        self.objectives_cb.place(x = 18, y = 178, anchor = 'nw')
        self.objectives_cb.bind('<<ComboboxSelected>>', self.set_objective)

        # ---------- >> separator  <<
        ttk.Separator(self.qry_tab).place(x = 12, y = 226, width = 930)

        # ---------- >> questions label, table & scrollbar  <<
        tk.Label(self.qry_tab, text = 'Questions by objective').place(x = 16, y = 242, anchor = 'nw')
        
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

        # ---------- >> papers heading & separator  <<
        ttk.Label(self.ins_tab, text = 'Add a paper...').place(x = 635, y = 16, anchor = 'nw')
        ttk.Separator(self.ins_tab).place(x = 625, y = 46, width = 320)

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
        self.papers_tv.place(x = 635, y = 65)
        
        self.paper_scrollbar = ttk.Scrollbar(self.ins_tab,
                                             orient="vertical",
                                             command = self.questions_tv.yview)
        self.paper_scrollbar.place(x = 918, y = 65, height = 107)
        self.papers_tv.configure(yscrollcommand = self.paper_scrollbar.set)

        # ---------- >> populate papers <<
        self.set_papers()

        # ---------- >> year label & text entry  <<
        ttk.Label(self.ins_tab, text = 'Year:').place(x = 690, y = 192, anchor = 'ne')

        self.year_et = ttk.Entry(self.ins_tab, width = 5)
        self.year_et.place(x = 710, y = 190, anchor = 'nw')

        # ---------- >> session label & combobox  <<
        ttk.Label(self.ins_tab, text = 'Session:').place(x = 704, y = 239, anchor = 'ne')

        self.session_cb = ttk.Combobox(self.ins_tab,
                                       value = ['spring', 'summer', 'winter'],
                                       state = 'readonly',
                                       width = 8)
        self.session_cb.place(x = 710, y = 237, anchor = 'nw')

        # ----- >> paper label & combobox  <<
        ttk.Label(self.ins_tab, text = 'Paper:').place(x = 704, y = 282, anchor = 'ne')

        self.paper_cb = ttk.Combobox(self.ins_tab,
                                       value = ['01', '02'],
                                       state = 'readonly',
                                       width = 3)
        self.paper_cb.place(x = 710, y = 280, anchor = 'nw')

        # ----- >> insert button  <<
        self.paper_bt = tk.Button(self.ins_tab,
                                  text = 'Insert',
                                  bg = '#f8f8f8',
                                  width = 9, height = 6,
                                  command = self.insert_papers)
        self.paper_bt.place(x = 824, y = 190, anchor = 'nw')

        # ----- >> error message <<


    def set_papers(self): # ---------------------------------------------------------------------------------------------------- >> populate papers table <<

        # ---------- fetch data
        papers = self.get_papers()

        # ---------- >> clear & repopulate papers table <<
        self.papers_tv.delete(*self.papers_tv.get_children())
        for records in papers:
            self.papers_tv.insert("",'end',text="L1",values=records)
        
        return None


# ------------------------------------------------------------------------------------------------------------------------------------------------------------


    def set_unit(self, event): # ----------------------------------------------------------------------------------------------- >> unit selected (event) <<
        
        # ----- >> calculate & update unit_id <<
        index = self.unit_choices[1].index(self.units_cb.get())
        self.unit_id = self.unit_choices[0][index]

        # ----- >> delete subunit_id, clear & re-populate subunits_cb <<
        self.subunit_id = None
        self.subunits_cb.set([])
        self.subunit_choices = self.get_subunits()
        self.subunits_cb.config(value=self.subunit_choices[1])

        # ----- >> clear objectives_cb <<
        self.objectives_cb.set([])

        # ------------------------------ >> clear questions_tv <<
        self.questions_tv.delete(*self.questions_tv.get_children())
        
        # ----- >> check if ther are subunits <<
        if len(self.subunit_choices[0]) == 0:
            self.subunit_id = None
            self.subunits_cb.set('This unit has no subunits...')
            self.objective_choices = self.get_objectives()
            self.objectives_cb.config(value=self.objective_choices[1])
        else:
            self.objective_id = None
            self.objectives_cb.config(value=[])


    def set_subunit(self, event): # ----------------------------------------------------------------------------------------- >> subunit selected (event) <<
        
        # ---------- >> calculate & update subunit_id <<
        index = self.subunit_choices[1].index(self.subunits_cb.get())
        self.subunit_id = self.subunit_choices[0][index]

        # ---------- >> delete objective_id, clear & re-populate objectives_cb <<
        self.objective_id = None
        self.objectives_cb.set([])
        self.objective_choices = self.get_objectives()
        self.objectives_cb.config(value = self.objective_choices[1])

        # ---------- >> clear questions_tv <<
        self.questions_tv.delete(*self.questions_tv.get_children())


    def set_objective(self, event): # ------------------------------------------------------------------------------------- >> objective selected (event) <<

        # ---------- >> calculate & update objective_id <<
        index = self.objective_choices[1].index(self.objectives_cb.get())
        self.objective_id = self.objective_choices[0][index]

        # ---------- >> clear & re-populate questions_tv <<
        self.questions_tv.delete(*self.questions_tv.get_children())
        questions = self.get_questions()
        for records in questions:
            self.questions_tv.insert("",'end',text="L1",values=records)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------


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


    def get_papers(self): # --------------------------------------------------------------------------------------------- >> fetch all paper records (sql) <<

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


    def insert_papers(self): # ---------------------------------------- >> check and insert new paper (sql) <<

        # get necessary data from widgets
        year = self.year_et.get()
        session = self.session_cb.get()
        paper = self.paper_cb.get()

        if year != '' and session != '' and paper != '':
            duplicate = self.count_papers(year, session, paper)
            
            if duplicate == 0:
                print('Insert is possible')
            else:
                tkinter.messagebox.showinfo('Error', 'That paper already exists!')

        else:
                tkinter.messagebox.showinfo('Error', 'You must fill in all fields!')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
# ========================================================================================================================================== >> main code <<
# ----------------------------------------------------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.geometry('1000x630')
root.resizable(False, False)
root.option_add( '*font', 'Arial 11' )
root.iconbitmap('favicon.ico')
root.title(' Past paper exam questions database | Cambridge IGCSE Computer Science (0478)')
app = Application(root)