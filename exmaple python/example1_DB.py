import mysql.connector

class connectionDB:
    def __init__(self):
        self.conn = mysql.connector.connect(host="localhost", user="root", password="")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE DATABASE IF NOT EXISTS listcitizen")
        self.conn.commit()

        self.conn = mysql.connector.connect(host="localhost", user="root", password="", database="vaccinedb")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS listcitizen (
                            icnumber  VARCHAR(20) NOT NULL,
                            name VARCHAR(50) NOT NULL,
                            age INT NOT NULL,
                            citizen VARCHAR(10) NOT NULL,
                            Diabetes VARCHAR(10) NOT NULL,
                            Hyper VARCHAR(10) NOT NULL,
                            Heart VARCHAR(10) NOT NULL,
                            ageStatus VARCHAR(20) NOT NULL,
                            vacStatus VARCHAR(20) NOT NULL
                            )""")
        self.conn.commit()