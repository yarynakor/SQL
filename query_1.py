import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql = """
SELECT TOP 5 (AVG(grades)), s.student_name
FROM grades as g
    LEFT JOIN students s ON g.student_id = s.id
"""