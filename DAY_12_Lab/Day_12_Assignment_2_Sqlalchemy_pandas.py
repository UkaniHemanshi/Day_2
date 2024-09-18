from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    stud_id = Column(Integer, primary_key=True)
    stud_name = Column(String)
    subj_name = Column(String)
    marks = Column(Integer)

    def __init__(self, id, subj, name, marks):
        self.stud_id=id
        self.stud_name=name
        self.subj_name=subj
        self.marks=marks

    def __repr__(self):
        return f"{self.stud_id}, {self.stud_name}, {self.subj_name}, {self.marks}"

engine = create_engine("sqlite:///mydb_hw.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

s1 = Student(1, 'Daman', 'IP', 89)
s2 = Student(2, 'Will', 'Math', 100)
s3 = Student(3, 'Bob', 'SSt', 44)
s4 = Student(4, 'Eric', 'Science', 77)
s5 = Student(5, 'Nayan', 'Eng', 45)
session.add_all([s1, s2, s3, s4, s5])
session.commit()
res1 = session.query(Student).all()
print("Before update: ")
for s in res1:
    print(res1)


# Query all students before update
res = session.query(Student).all()
print("Before update:")
for student in res:
    print(student)

# update record
studToUpdate = session.query(Student).filter(Student.stud_id==2).first()

if studToUpdate:
    studToUpdate.marks = 98
    session.commit()
    print(f"Update student: {studToUpdate}")
else:
    print("Student with id 2 not found.")


res2 = session.query(Student).all()
print("After update: ")
for stud in res2:
    print(stud)
