import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Create the database engine
engine = create_engine('sqlite:///student_data.db')

# Base class for declarative class definitions
Base = declarative_base()


# Define the Student class
class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    marks = Column(Float, nullable=False)


def create_table():
    Base.metadata.create_all(engine)
    print("Table 'students' created successfully")


def insert_sample_data():
    Session = sessionmaker(bind=engine)
    session = Session()

    students_data = [
        Student(name='Sachin', age=20, department='HR', marks=85.5),
        Student(name='Hema', age=22, department='IT', marks=91.0),
        Student(name='Akash', age=21, department='Finance', marks=78.5)
    ]

    session.add_all(students_data)
    session.commit()
    session.close()
    print('Sample data added successfully')


def read_data():
    df = pd.read_sql('students', con=engine)
    return df


def update_marks(df, student_id, new_marks):
    # Correct syntax for updating marks in the DataFrame
    df.loc[df['student_id'] == student_id, 'marks'] = new_marks
    return df


def write_data(df):
    # Write the DataFrame back to the database
    df.to_sql('students', con=engine, if_exists='replace', index=False)
    print('Updated data written back to database')


def main():
    create_table()
    insert_sample_data()
    df = read_data()
    print('Original DataFrame:')
    print(df)

    # Update marks for a specific student
    df = update_marks(df, student_id=2, new_marks=95.0)
    print('\nUpdated DataFrame:')
    print(df)

    write_data(df)
    print('\nData updated in database')

    df = read_data()
    print("Updated DataFrame:")
    print(df)


if __name__ == "__main__":
    main()
