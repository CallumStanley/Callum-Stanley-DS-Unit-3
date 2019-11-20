import sqlite3
with sqlite3.connect("movies.db") as database:
    cursor = database.cursor()
    query = ("""
        SELECT director
        FROM movies
        WHERE director = "US";
        """)
    for row in cursor.fetchall():
     print(row[0]) 