from random import randrange
import sqlite3

conn = sqlite3.connect("baza_content.db")
cur = conn.cursor()


def insert(cur, data):
  cur.execute(f'INSERT INTO allusers (name,sphere) VALUES( ?, ?);', data)

def select(cur, table):
  cur.execute(f'SELECT * FROM {table};')
  return cur.fetchall()

data=('bro', 'bax',)
data2=('brox', 'bax',)
data3=('new', 'newsphere')

insert(cur, data)
insert(cur, data2)
insert(cur, data3)
conn.commit()
result = select(cur,'allusers')

for res in result:
  print(res)

