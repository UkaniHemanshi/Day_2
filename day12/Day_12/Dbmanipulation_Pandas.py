import pandas as pd
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Float, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import inspect


engine = create_engine('sqlite:///company_orm3.db')
# Base class for declarative class definitions
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    position = Column(String,nullable=False)
    salary = Column(Float,nullable=False)

def create_table():
    Base.metadata.create_all(engine)
    print("Table 'employees' created successfully")

def insert_sample_data():
    Session = sessionmaker(bind=engine)
    session = Session()

    employees_data = [
        Employee(name='Sachin', position='Engineer', salary=70000),
        Employee(name='Hema', position='Manager', salary=7000),
        Employee(name='Akash',position='Analyst', salary=60000)
    ]

    session.add_all(employees_data)
    session.commit()
    session.close()
    print('Sample data added successfully')

def read_data():
    df = pd.read_sql('employees', con=engine)
    return df

def update_salary(df, employee_id,new_salary):
    df.loc[df['employee_id'] == employee_id, 'salary']= new_salary
    return df

def write_data(df):
    df.to_sql('employees',con=engine, if_exists='replace', index=False)
    print('updated data written back to Database')

def main():
    create_table()
    insert_sample_data()
    df= read_data()
    print('original DataFrame:')
    print(df)

    df = update_salary(df,employee_id=2,new_salary=50000)
    print('\nupdated DataFrame:')
    print(df)
    write_data(df)
    print('\nData updated in db')
    df= read_data()
    print("updated Dataframe:")
    print(df)

if __name__ == "__main__":
    main()