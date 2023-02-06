from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship("Subject", back_populates="teachers")

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teachers = relationship("Teacher", back_populates="subject")
    grades = relationship("Grade", back_populates="subjects")


class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    grade = Column(Integer)
    date = Column(DateTime, default=datetime.now())

    student = relationship("Student", back_populates="grades")
    subjects = relationship("Subject", back_populates="grades")


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="students")

engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)
