import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти список студентів у певній групі.
sql = """
SELECT student_name, group_id
FROM students s
INNER JOIN groups g
ON g.student_id = s.student_id
WHERE group_id='15'
"""