import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
query = "SELECT * FROM directors"
db.execute(query)
rows = db.fetchall()
print(rows)
# => list (rows) of tuples (columns)
