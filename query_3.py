import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти середній бал у групах з певного предмета.
sql = """
SELECT AVG(grades), subject_id, subject_name
FROM grades g
INNER JOIN subjects s
ON g.subject_id = subjects.subject_id
WHERE subject='math'
"""