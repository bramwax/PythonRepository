# ================================================================================================== >> reference <<
# https://www.sqlitetutorial.net/sqlite-python/
# https://sqlitebrowser.org/
# =============================================================================================================== <<
import sqlite3

def get_units(conn):
    cur = conn.cursor()
    cur.execute('SELECT unit FROM units;')
    records = cur.fetchall()
    # ---------------------------------------------------------
    return [row[0] for row in records]

def insert(conn, table, data):
    cur = conn.cursor()
    if table == paper:
        cur.execute(''' INSERT INTO papers (year,session,paper_no)
                        VALUES(?,?,?); ''', data)
    else:
        cur.execute(''' INSERT INTO questions (question_number,mark,note,paper_fk,objective_fk)
                        VALUES(?,?,?,?,?); ''', data)  
    conn.commit()

'''
def qry_table(conn, tableName):
    cur = conn.cursor()
    sql = "SELECT * FROM " + tableName + ";"
    cur.execute(sql)
    records = cur.fetchall()
    for row in records:
        print(row)
'''

# ================================================================================================== >> main code <<
print('SQLite Version', sqlite3.sqlite_version)
# ------------------------------------------------------------------------------- >> connect db <<
conn = sqlite3.connect(r"0478_past_papers.db")
# ------------------------------------------------------------------------ >> create & prime db <<
unit_choices = get_units(conn)

print(unit_choices)
