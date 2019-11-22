import sqlite3
with sqlite3.connect("movies.db") as database:
    cursor = database.cursor()
    query = ("""
                SELECT memname
                FROM members
                WHERE owes IS NOT NULL;
                """)
    for row in cursor.fetchall():
        print(row) 