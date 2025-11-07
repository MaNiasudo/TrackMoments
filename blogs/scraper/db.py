import psycopg2

conn=psycopg2.connect(
    dbname='mydatabase',
    user='djangouser',
    password='1',
    host='localhost',
)

cursor=conn.cursor()