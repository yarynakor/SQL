import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти які курси читає певний викладач.
sql = """
SELECT teacher_name, subject_name
FROM teachers t
INNER JOIN subjects s
ON t.subject_id = subjects.subject_id
WHERE teacher='Smith'
"""