import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти студента із найвищим середнім балом з певного предмета.
sql = """
SELECT MAX(AVG(grade)), student_name, subject_name
FROM grades g
    LEFT JOIN students s ON g.student_id = s.id
    LEFT JOIN subject ON g.subject_id = subjects.subject_id

"""