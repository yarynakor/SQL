import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти список курсів, які відвідує студент.
sql = """
SELECT subject_name
FROM subjects s
    LEFT JOIN students st ON s.subject_id = st.subject_id
WHERE student_name='Smith'
"""