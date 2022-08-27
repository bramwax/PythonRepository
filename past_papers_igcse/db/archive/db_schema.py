# ================================================================================ >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# ============================================================================================= <<
import sqlite3
import csv


def create_db(conn):
    cur = conn.cursor()
    cur.execute(create_papers_table)
    cur.execute(create_units_table)
    cur.execute(create_subunits_table)
    cur.execute(create_objectives_table)
    cur.execute(create_questions_table)
    conn.commit()
    cur.close()


def prime_db(conn):
    cur = conn.cursor()
    # ---------------------------------------------------------------------------------------- >> units <<
    data_stream = open('units.csv', newline='')
    unit_data = csv.reader(data_stream, delimiter='|')
    next(unit_data)
    for row in unit_data:
        cur.execute("INSERT INTO units (unit_id,unit) VALUES(?,?)", row)
    # ------------------------------------------------------------------------------------- >> subunits <<
    data_stream = open('subunits.csv', newline='')
    subunit_data = csv.reader(data_stream, delimiter='|')
    next(subunit_data)
    for row in subunit_data:
        cur.execute("INSERT INTO subunits (subunit_id,subunit) VALUES(?,?)", row)
    # ----------------------------------------------------------------------------------- >> objectives <<
    data_stream = open('objectives.csv', newline='')
    objective_data = csv.reader(data_stream, delimiter='|')
    next(objective_data)
    for row in objective_data:
        cur.execute("INSERT INTO objectives (objective_id,objective,unit_fk,subunit_fk) VALUES(?,?,?,?)",row)
    conn.commit()
    cur.close()


create_papers_table = """CREATE TABLE IF NOT EXISTS papers (
                         paper_id integer PRIMARY KEY AUTOINCREMENT,
                         year integer NOT NULL,
                         session text NOT NULL,
                         paper_no text NOT NULL); """


create_units_table = """CREATE TABLE IF NOT EXISTS units (
                        unit_id integer PRIMARY KEY,
                        unit text NOT NULL); """


create_subunits_table = """CREATE TABLE IF NOT EXISTS subunits (
                           subunit_id real PRIMARY KEY,
                           subunit text NOT NULL); """


create_objectives_table = """CREATE TABLE IF NOT EXISTS objectives (
                             objective_id integer PRIMARY KEY,
                             objective text NOT NULL,
                             unit_fk integer NOT NULL,
                             subunit_fk real,
                             FOREIGN KEY (unit_fk) REFERENCES units (unit_id),
                             FOREIGN KEY (subunit_fk) REFERENCES subunits (subunit_id));"""

create_questions_table = """CREATE TABLE IF NOT EXISTS questions (
                            question_id integer PRIMARY KEY,
                            question_number text NOT NULL,
                            mark integer NOT NULL,
                            note text,
                            paper_fk integer NOT NULL,
                            objective_fk integer NOT NULL,
                            FOREIGN KEY (paper_fk) REFERENCES papers (paper_fk),
                            FOREIGN KEY (objective_fk) REFERENCES objectives (objective_fk));"""


# ================================================================================ >> main code <<
conn = sqlite3.connect(r"0478_past_papers.db")
create_db(conn)
prime_db(conn)
conn.close()
