import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import sqlite3

class Paper_Frame(ttk.Frame):

    def __init__(self, parent): # --------------------------------------------------------------------------------------------------- >> constructor method <<

        # ---------- >> create frame <<
        ttk.LabelFrame.__init__(self, parent, text = "  Insert Paper  ")

        # ---------- >> connect to database <<
        self.conn = sqlite3.connect('0478_past_papers.db')

        # ---------- >> create widgets <<
        self.widgets()

    def widgets(self):

        # ---------- >> papers table & scrollbar <<
        columns = ('#1','#2','#3','#4')
        self.papers_tv = ttk.Treeview(self,
                                         selectmode = 'browse',
                                         columns=columns,
                                         show='headings',
                                         height = 4)

        self.papers_tv.heading('#1', anchor='w', text = 'Paper_Id')
        self.papers_tv.heading('#2', anchor='w', text = 'Year')
        self.papers_tv.heading('#3', anchor='w', text = 'Session')
        self.papers_tv.heading('#4', anchor='w', text = 'Paper_No')

        self.papers_tv.column( '#1', width = 80)
        self.papers_tv.column( '#2', width = 44)
        self.papers_tv.column( '#3', width = 70)
        self.papers_tv.column( '#4', width = 90)
        self.papers_tv.place(x = 30, y = 28)
        
        self.papers_scrollbar = ttk.Scrollbar(self,
                                             orient="vertical",
                                             command = self.papers_tv.yview)
        self.papers_scrollbar.place(x = 317, y = 28, height = 107)

        self.papers_tv.configure(yscrollcommand = self.papers_scrollbar.set)
        self.papers_tv.bind('<ButtonRelease-1>', self.set_insert_paper)

        # ---------- >> populate papers <<
        self.set_papers()

        # ---------- >> year label & text entry  <<
        ttk.Label(self, text = 'Year:').place(x = 100, y = 164, anchor = 'ne')

        self.year_et = ttk.Entry(self, width = 5)
        self.year_et.place(x = 106, y = 162, anchor = 'nw')


        # ---------- >> session label & combobox  <<
        ttk.Label(self, text = 'Session:').place(x = 100, y = 215, anchor = 'ne')

        self.session_cb = ttk.Combobox(self,
                                       value = ['spring', 'summer', 'winter'],
                                       state = 'readonly',
                                       width = 8)
        self.session_cb.place(x = 106, y = 213, anchor = 'nw')

        # ---------- >> paper label & combobox  <<
        ttk.Label(self, text = 'Paper:').place(x = 100, y = 265, anchor = 'ne')

        self.paper_cb = ttk.Combobox(self,
                                       value = ['11', '12','13', '21', '22','23', '01', '02'],
                                       state = 'readonly',
                                       width = 3)
        self.paper_cb.place(x = 106, y = 263, anchor = 'nw')

        # ---------- >> insert paper button  <<
        self.paper_bt = tk.Button(self,
                                  text = 'Insert',
                                  bg = '#f8f8f8',
                                  width = 9, height = 6,
                                  command = self.check_new_paper)
        self.paper_bt.place(x = 242, y = 162, anchor = 'nw')

    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_papers(self): # ----------------------------------------------------------------------------------------------------- >> populate papers table <<

        # ---------- fetch data
        papers = self.get_all_papers()

        # ---------- >> clear & repopulate papers table <<
        self.papers_tv.delete(*self.papers_tv.get_children())
        for records in papers:
            self.papers_tv.insert("", 'end', text = "L1", values = records)

    def check_new_paper(self): # --------------------------------------------------------------------- >> check paper parameters & insert or display error <<
        
        # get necessary data from widgets
        year = self.year_et.get()
        session = self.session_cb.get()
        paper = self.paper_cb.get()

        if year != '' and session != '' and paper != '':
            duplicate = self.count_papers(year, session, paper)
            
            if duplicate == 0:
                self.insert_paper(year, session, paper)
                self.set_papers()
                tkinter.messagebox.showinfo('Success!', 'New paper inserted', parent = self)
            else:
                tkinter.messagebox.showinfo('Error', 'That paper already exists!', parent = self)

        else:
            tkinter.messagebox.showinfo('Error', 'You must fill in all fields!', parent = self)

    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    def set_insert_paper(self, event): # --------------------------------------------------------------------------------------- >> paper selected (event) <<

        paper_selected = self.papers_tv.focus()
        self.paper_selected = self.papers_tv.item(paper_selected)['values'][0]

    # -------------------------------------------------------------------------------------------------------------------------------------------------------

    def get_all_papers(self): # ----------------------------------------------------------------------------------------- >> fetch all paper records (sql) <<

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
