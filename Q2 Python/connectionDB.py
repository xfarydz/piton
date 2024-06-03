import mysql.connector

class loanDB:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE DATABASE IF NOT EXISTS loan")
        self.conn.commit()

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="loan")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS listloan (
                            icnumber VARCHAR(20),
                            name VARCHAR(255),
                            salary VARCHAR(20),
                            amount VARCHAR(20),
                            loanStatus VARCHAR(50),
                            PRIMARY KEY (icnumber)
                            )""")
        self.conn.commit()
        print("...Successful connection to database...")
