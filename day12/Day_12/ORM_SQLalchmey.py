from sqlalchemy import create_engine, MetaData, Column, Integer, String, Float, Sequence
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import inspect

# Create the database engine
engine = create_engine('sqlite:///company_orm1.db')
# Base class for declarative class definitions
Base = declarative_base()


# Define the Employee class
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, Sequence('emp_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    department = Column(String(50))
    salary = Column(Float)


# Create all tables in the engine
Base.metadata.create_all(engine)

# Reflect the existing tables into MetaData
metadata = MetaData()
metadata.reflect(bind=engine)

# Inspect the 'employees' table
inspector = inspect(engine)
columns = inspector.get_columns('employees')  # Use 'employees' (lowercase) to match the table name

print('Table employees details:')
for column in columns:
    print(f"Column: {column['name']} - Type: {column['type']}")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create and add new employee records
employees_data = [
    Employee(name='Sachin', age=30, department='HR', salary=70000),
    Employee(name='Hema', age=39, department='IT', salary=7000),
    Employee(name='Akash', age=70, department='Finance', salary=60000)
]

session.add_all(employees_data)  # Use session.add_all() to add multiple records at once
session.commit()

# Query and print all employees
all_employees = session.query(Employee).all()
for emp in all_employees:
    print(f'{emp.id}: {emp.name} - {emp.department} - ${emp.salary}')

# Update salary for a specific employee
employee_to_update = session.query(Employee).filter_by(name='Hema').first()
if employee_to_update:
    employee_to_update.salary = 75000
    session.commit()

# Confirm the update
updated_employee = session.query(Employee).filter_by(name='Hema').first()
if updated_employee:
    print(
        f'Updated Employee: {updated_employee.id}: {updated_employee.name} - {updated_employee.department} - ${updated_employee.salary}')
