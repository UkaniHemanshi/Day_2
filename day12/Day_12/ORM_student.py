from sqlalchemy import create_engine, MetaData, Column, Integer, String, Float, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import inspect

# Create the database engine
engine = create_engine('sqlite:///company_orm2.db')
# Base class for declarative class definitions
Base = declarative_base()


# Define the Employee class
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, Sequence('emp_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    marks = Column(Integer)


# Create all tables in the engine
Base.metadata.create_all(engine)

# Reflect the existing tables into MetaData
metadata = MetaData()
metadata.reflect(bind=engine)

# Inspect the 'employees' table
inspector = inspect(engine)
columns = inspector.get_columns('students')
print('Table students details:')
for column in columns:
    print(f"Column: {column['name']} - Type: {column['type']}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

students_data = [
    Student(name='Sachin', age=30, marks=80),
    Student(name='Hema', age=39, marks=70),
    Student(name='Akash', age=70, marks=60)
]

session.add_all(students_data )
session.commit()

all_students = session.query(Student).all()
for stu in all_students:
    print(f'{stu.id}: {stu.name} - {stu.marks} ')

student_to_update = session.query(Student).filter_by(name='Hema').first()
if student_to_update:
    student_to_update.marks = 75
    session.commit()

# Confirm the update
updated_student = session.query(Student).filter_by(name='Hema').first()
if updated_student:
    print(
        f'Updated Student: {updated_student.id}: {updated_student.name} - {updated_student.marks}')
