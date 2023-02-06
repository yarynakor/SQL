from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random
from models import Base, Student, Group, Teacher, Subject, Grade

engine = create_engine('sqlite:///students.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

fake = Faker()

# Generate 3 groups
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)
session.commit()

# Generate 7 subjects
subjects = [Subject(name=fake.word()) for _ in range(7)]
session.add_all(subjects)
session.commit()

# Generate 4 teachers
teachers = [Teacher(name=fake.name(), subject=random.choice(subjects)) for _ in range(4)]
session.add_all(teachers)
session.commit()

# Generate 40 students
students = [Student(name=fake.name(), group=random.choice(groups)) for _ in range(40)]
session.add_all(students)
session.commit()

# Generate up to 20 grades for each student for each subject
for student in students:
    for subject in subjects:
        for _ in range(random.randint(0, 20)):
            session.add(Grade(student=student, subject=subject, grade=random.randint(1, 100)))

session.commit()
