# ================================================================================================== >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# =============================================================================================================== <<
import sqlite3
import csv

conn = sqlite3.connect(r'0478_past_papers.db')
cur = conn.cursor()

# ============================================================================================== >> create tables <<

cur.execute(''' CREATE TABLE IF NOT EXISTS papers (
                paper_id integer PRIMARY KEY AUTOINCREMENT,
                year integer NOT NULL,
                session text NOT NULL,
                paper_no text NOT NULL); ''')

cur.execute(''' CREATE TABLE IF NOT EXISTS units(
                unit_id integer PRIMARY KEY,
                unit text NOT NULL); ''')

cur.execute(''' CREATE TABLE IF NOT EXISTS subunits (
                subunit_id real PRIMARY KEY,
                subunit text NOT NULL); ''')

cur.execute(''' CREATE TABLE IF NOT EXISTS objectives (
                objective_id integer PRIMARY KEY AUTOINCREMENT,
                objective text NOT NULL,
                unit_fk integer NOT NULL,
                subunit_fk real,
                FOREIGN KEY (unit_fk) REFERENCES units (unit_id),
                FOREIGN KEY (subunit_fk) REFERENCES subunits (subunit_id)); ''')

cur.execute(''' CREATE TABLE IF NOT EXISTS questions (
                question_id integer PRIMARY KEY AUTOINCREMENT,
                question_number text NOT NULL,
                mark integer NOT NULL,
                note text,
                paper_fk integer NOT NULL,
                objective_fk integer NOT NULL,
                FOREIGN KEY (paper_fk) REFERENCES papers (paper_fk),
                FOREIGN KEY (objective_fk) REFERENCES objectives (objective_fk)); ''')

# ================================================================================================ >> import data <<

data_stream = open('units.csv', newline='')
unit_data = csv.reader(data_stream, delimiter='|')
next(unit_data)
for row in unit_data:
    cur.execute(''' INSERT INTO units (unit_id,unit)
                    VALUES(?,?); ''', row)

data_stream = open('subunits.csv', newline='')
subunit_data = csv.reader(data_stream, delimiter='|')
next(subunit_data)
for row in subunit_data:
    cur.execute(''' INSERT INTO subunits (subunit_id,subunit)
                    VALUES(?,?); ''', row)

data_stream = open('objectives.csv', newline='')
objective_data = csv.reader(data_stream, delimiter='|')
next(objective_data)
for row in objective_data:
    cur.execute(''' INSERT INTO objectives (objective,unit_fk,subunit_fk)
                    VALUES(?,?,?); ''',row)

data_stream = open('papers.csv', newline='')
paper_data = csv.reader(data_stream, delimiter='|')
next(paper_data)
for row in paper_data:
    cur.execute(''' INSERT INTO papers (year,session,paper_no)
                    VALUES(?,?,?); ''', row)

data_stream = open('questions.csv', newline='')
question_data = csv.reader(data_stream, delimiter='|')
next(question_data)
for row in question_data:
    cur.execute(''' INSERT INTO questions (question_number,mark,note,paper_fk,objective_fk)
                    VALUES(?,?,?,?,?); ''', row)
conn.commit()

# =============================================================================================================== <<

cur.close()
conn.close()

