import sqlite3
conn = sqlite3.connect("raycast.db")
cur = conn.cursor()


cur.execute("DROP TABLE IF EXISTS RaycastDB")      
cur.execute('''CREATE TABLE RaycastDB(             
                   key INTEGER NOT NULL PRIMARY KEY,
                   search TEXT,
                   time REAL
                   )''')
