import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти оцінки студентів у окремій групі з певного предмета
sql = """
SELECT grades, subject_name, group_id
FROM grades g
    INNER JOIN subjects s ON g.subject_id = subjects.subject_id
    INNER JOIN students st ON g.student_id = st.student_id
WHERE subject='math'
"""