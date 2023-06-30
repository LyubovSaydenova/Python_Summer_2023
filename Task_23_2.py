import psycopg2
con = psycopg2.connect(
    database="postgres",
    user="postgres",
    password=
    host="127.0.0.1",
    port="5433"
)

cur = con.cursor()
cur.execute("SELECT * FROM book where author = 2")

rows = cur.fetchall()
for row in rows:
    print(row)
con.close()