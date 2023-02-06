from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade

# create an engine and a session
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()
#1. Find 5 students with the highest average grade from all subjects
top_5_students = session.query(Student, func.avg(Grade.grade).label('average_grade'))\
    .join(Grade)\
    .group_by(Student.id)\
    .order_by(func.avg(Grade.grade).desc())\
    .limit(5)\
    .all()


#2. Find a student with the highest average grade in mathematics:
highest_math_student = session.query(Student, func.avg(Grade.grade).label('average_grade'))\
    .join(Grade)\
    .join(Subject)\
    .filter(Subject.name == 'Mathematics')\
    .group_by(Student.id)\
    .order_by(func.avg(Grade.grade).desc())\
    .first()

print(highest_math_student.name, highest_math_student.average_grade)

#3 Find average math grade in groups:
avg_math_grades_by_group = session.query(Group.name, func.avg(Grade.grade).label('average_grade'))\
    .join(Student)\
    .join(Grade)\
    .join(Subject)\
    .filter(Subject.name == 'Mathematics')\
    .group_by(Group.id)\
    .all()


#4 Find overall average grade:
for group_name, avg_grade in avg_math_grades_by_group:
    print(group_name, avg_grade)

overall_average_grade = session.query(func.avg(Grade.grade).label('average_grade')).scalar()

print(overall_average_grade)

#5 Find which subjects are led by teacher Smith:
teacher_smith_subjects = session.query(Subject.name)\
    .join(Subject)\
    .join(Teacher)\
    .filter(Teacher.name == 'Smith')\
    .all()

for subject_name in teacher_smith_subjects:
    print(subject_name)


#6 Find the number of students in group 1:
num_students_in_group_1 = session.query(func.count(Student.id))\
    .join(Group)\
    .filter(Group.name == '1')\
    .scalar()

print(num_students_in_group_1)

#7 Find grades of students in group 2 in math:
grades_group_2_math = session.query(Student.name, Grade.grade)\
    .join(Group)\
    .join(Grade)\
    .join(Subject)\
    .filter(Group.name == '2', Subject)


#8 Number of students in group 1
num_of_students_g1 = session.query(func.count(Student.id)).filter(Student.group_id == 1).scalar()
print("Number of students in group 1: ", num_of_students_g1)

#9 Grades of students in group 2 in math
grades_group2= session.query(Student.name, Student.math_grade).filter(Student.group_id == 2).all()
print("Grades of students in group 2 in math:")
for name, grade in grades_group2:
    print("{}: {}".format(name, grade))


#10 Average grade given by teacher Smith
ave_grade_smith = session.query(func.avg(Student.grade)).filter(Student.teacher_name == "Smith").scalar()
print("Average grade given by teacher Smith: ", ave_grade_smith)


session.close()