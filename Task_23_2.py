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

import functools
def get_biggest (numbers):
    def compare(x, y):
        return (-1 if str(x) + str(y) > str(y) + str(x) else 1)
nu = sorted(numbers, key = functools.cmp_to_key(compare))
return int(''.join([str(i) for i in nu]))