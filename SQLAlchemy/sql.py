# [1]
import sqlalchemy

print(sqlalchemy.__version__)

# [2]
## engine object
from sqlalchemy import create_engine

engine = create_engine('sqlite:///college.db', echo=False)
print(type(engine))

# [3]
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

## meta object
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

# [4]
for t in meta.sorted_tables:
    print(t.name)

# [5]
## create tables
meta.create_all(engine)

# [6]
users.drop(engine, checkfirst=True)
students.drop(engine, checkfirst=True)

# [7]
users.create(engine, checkfirst=True)
students.create(engine, checkfirst=True)

# [8]
## define sql expression
ins = students.insert().values(name='Karen')

# [9]
print(str(ins))

# [10]
print(ins.compile().params)

# [11]
## execute sql
conn = engine.connect()
ins = students.insert().values(name='Karen', lastname='Kapoor')
result = conn.execute(ins)

# [12]
print(result.inserted_primary_key)

# [13]
conn.execute(students.insert(), [
    {'name': 'Rajiv', 'lastname': 'Khanna'},
    {'name': 'Komal', 'lastname': 'Bhandari'},
    {'name': 'Abdul', 'lastname': 'Sattar'},
    {'name': 'Priya', 'lastname': 'Rajhans'},
])

# [14]
s = students.select()
print(str(s))

# [15]
result = conn.execute(s)

row = result.fetchone()
print(row)
print(row['name'], row['lastname'])

# [16]
for row in result:
    print(row)

# [17]
s = students.select().where(students.c.id > 2)  # .c 表示欄位 column
result = conn.execute(s)

for row in result:
    print(row)

# [18]
from sqlalchemy.sql import select

s = select([students])
result = conn.execute(s)
for row in result:
    print(row)

# [19]
from sqlalchemy import text

t = text("SELECT * FROM students")
print(str(t))
result = conn.execute(t)
for row in result:
    print(row)

# [20]
from sqlalchemy import text

t = text("SELECT students.name, students.lastname FROM students where students.name between :x and :y")
print(str(t))

result = conn.execute(t, x='A', y='L').fetchall()
print(type(result))
for row in result:
    print(row['name'], row['lastname'])

# [21]
from sqlalchemy import bindparam

stmt = text("SELECT * FROM students WHERE students.name BETWEEN :x AND :y")
stmt = stmt.bindparams(bindparam("x", type_=String), bindparam("y", type_=String))

result = conn.execute(stmt, {"x": "A", "y": "L"})
print(result)

for row in result:
    print(row['name'], row['lastname'])

# [22]
s = select([text("students.name, students.lastname from students")]).where(text("students.name between :x AND :y"))
print(str(s))

result = conn.execute(s, {"x": "A", "y": "L"}).fetchall()
print(result)

for row in result:
    print(row)

# [23]
from sqlalchemy import and_
from sqlalchemy.sql import select

s = select([text("* from students")]).where(
    and_(
        text("students.name BETWEEN :x AND :y"),
        text("students.id > 2")
    ))

print(str(s))

result = conn.execute(s, {"x": "A", "y": "L"}).fetchall()
for row in result:
    print(row)

# [24]
from sqlalchemy import or_
from sqlalchemy.sql import select

s = select([text("* from students")]).where(
    or_(
        text("students.name BETWEEN :x AND :y"),
        text("students.id > 2")
    ))

print(str(s))

result = conn.execute(s, {"x":"A", "y":"L"}).fetchall()
for row in result:
    print(row)