import sqlite3

conn = sqlite3.connect('./db/initial_db.db')
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS 'PICTURE';""")
c.execute("""DROP TABLE IF EXISTS 'PICTURE_APP';""")
c.execute("""
CREATE TABLE 'PICTURE' (
    'Pic_ID' INTEGER PRIMARY KEY AUTOINCREMENT,
    'Pic_Name' TEXT NOT NULL,
    'Pic_Path' TEXT NOT NULL);
""")
c.execute("""
CREATE TABLE 'PICTURE_APP' (
    'Pic_ID' INTEGER PRIMARY KEY FOREIGN KEY REFERENCES PICTURE(Pic_ID),
    'App_ID' INTEGER NOT NULL);
    """)
conn.commit()