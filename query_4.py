import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

#Знайти середній бал на потоці (по всій таблиці оцінок).
sql = """
SELECT AVG(grades), 
FROM grades g
"""