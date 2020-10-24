import sqlite3

class DataBase:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS user(
            username TEXT,
            password TEXT
        )''')
        self.conn.commit()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS all_data(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            middle_name TEXT,
            phone_num TEXT,
            computer_name TEXT,
            computer_serial TEXT,
            person_pic TEXT,
            computer_pic TEXT
        )''')
        self.conn.commit()

    def addData(self, fname, lname, pnum, cname, cserial, ppic, cpic):
        self.cur.execute('''INSERT INTO all_data VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)''', (fname, lname, pnum, cname, cserial, ppic, cpic))
        self.conn.commit()

    def searchData(self, val):
        self.cur.execute('''SELECT * FROM all_data WHERE first_name=?''', (val,))
        data = self.cur.fetchall()
        return data

    def deleteData(self, id):
        self.cur.execute('''DELETE FROM all_data WHERE id=?''', (id,))
        self.conn.commit()

    def fetchAll(self):
        self.cur.execute('''SELECT * FROM all_data''')
        data = self.cur.fetchall()
        return data

db = DataBase('db.db')