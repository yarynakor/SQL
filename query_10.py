import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Список курсів, які певному студенту читає певний викладач.
sql = """
SELECT subject_name, student_name, teacher_name
FROM subjects s
    INNER JOIN students st ON st.subject_id = s.subject_id
    INNER JOIN teachers t ON t.subject_id = s.subject_id
WHERE student_name='Smith' AND teacher_name='John'
"""