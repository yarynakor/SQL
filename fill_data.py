import faker
from random import randint, choice
import sqlite3

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 40
NUMBER_SUBJECTS = 7
NUMBER_TEACHERS = 5
NUMBER_GRADES = 15


def generate_fake_data(number_groups, number_students, number_subjects, number_teachers, number_grades) -> tuple():
    fake_groups = []
    fake_students = []
    fake_subjects = []
    fake_teachers = []
    fake_grades = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.random_number())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_grades):
        fake_grades.append(fake_data.random_number())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.random_number())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    return fake_groups, fake_students, fake_subjects, fake_grades, fake_teachers


def prepare_data(students, grades, teachers, subjects, groups) -> tuple():
    for_students = []
    # підготовляємо список кортежів студентів
    for student in students:
        for_students.append((student, randint(1, NUMBER_GROUPS)))

    for_teachers = []  # для таблиці teachers
    for tch in teachers:
        for_teachers.append((tch, ))

    for_grades = []
    for grade in range(NUMBER_SUBJECTS):
        for_grades.append((randint(1, NUMBER_GRADES), choice(subjects), choice(students)))

    for_groups = []
    for group_name in range(NUMBER_GROUPS):
        for_groups.append((randint(1, NUMBER_GROUPS) ))

    for_subjects = []
    for subject in subjects:
        for_subjects.append((randint(1, NUMBER_SUBJECTS), randint(1, NUMBER_TEACHERS)))

    return for_subjects, for_students, for_groups, for_grades, for_teachers



def insert_data_to_db(students, teachers, grades, groups, subjects) -> None:
    # Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними

    with sqlite3.connect('school.db') as con:

        cur = con.cursor()
        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_grades = """INSERT INTO grades(student_id, grade, subject_id, date_of)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_grades, grades)

        sql_to_groups = """INSERT INTO groups(group_name)
                                      VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                                      VALUES (?, ?)"""
        cur.execute(sql_to_subjects, subjects)

        # Фіксуємо наші зміни в БД

        con.commit()


if __name__ == "__main__":
    students, subjects, teachers, grades, groups = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_SUBJECTS, NUMBER_GRADES, NUMBER_GROUPS, NUMBER_TEACHERS))
    insert_data_to_db(students, subjects, teachers, groups, grades)