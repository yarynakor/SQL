import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти оцінки студентів у окремій групі з певного предмета
sql = """
SELECT AVE(grade), teacher_name 
FROM grades g
    INNER JOIN subjects s ON s.subject_id = g.subject_id
    INNER JOIN teachers t ON t.subject_id = s.subject_id
WHERE subject='math'
"""