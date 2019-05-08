import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

print(sqlalchemy.__version__)

## engine object
engine = create_engine('sqlite:///college.db', echo=False)
print(type(engine))

meta = MetaData()

## define table object (students)
students = Table('students', meta,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('lastname', String))

## define table object (users)
users = Table('users', meta,
              Column('user_id', Integer, primary_key=True),
              Column('user_name', String(16), nullable=True),
              Column('email_address', String(60)),
              Column('nickname', String(50), nullable=False))

print(meta.tables)

for t in meta.sorted_tables:
    print(t.name)

## create tables
meta.create_all(engine)
# users.drop(engine, checkfirst=True)
# users.create(engine, checkfirst=True)
# students.drop(engine, checkfirst=True)
# students.create(engine, checkfirst=True)

## define sql expression
ins = students.insert().values(name='Karen')
print(str(ins))
print(ins.compile().params)

## execute sql
conn = engine.connect()
ins = students.insert().values(name='Karen', lastname='Kapoor')
result = conn.execute(ins)

print(result.inserted_primary_key)

conn.execute(students.insert(), [
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])

