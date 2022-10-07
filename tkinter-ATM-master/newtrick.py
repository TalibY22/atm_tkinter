import sqlite3 as sql

conn = sql.connect('Oshwal.db')

cursor = conn.cursor()

#cursor.execute("""CREATE TABLE CUSTOMERS2 (
    #accid interger(10) primary key,
    ##name varchar(30),
    ##current_balance char(30)

#) """)

#cursor.execute("INSERT INTO CUSTOMERS2 VALUES(133,'TALIB',1234,'1111')")
conn.commit()

#testing
cursor.execute('select * from CUSTOMERS2')
values=cursor.fetchall()

b=[]
for i in values:
      b.append(i[0])


print(b)     