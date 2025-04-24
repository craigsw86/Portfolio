import sqlite3
import pandas
import mysql.connector
import schedule
import time
from datetime import datetime, timedelta

connection = sqlite3.connect("gfg.db")

crsr = connection.cursor()

sql_command = """CREATE TABLE emp (
patient_number INTEGER PRIMARY KEY,
fname VARCHAR(30),
lname VARCHAR(30),
lastvisit DATE);"""

pk = [2, 3, 4]

fname = ["John", "Joe", "Anna"]

lname = ["Smith", "Jones", "Roberts"]

lastvisit = ["2020-01-01", "1991-12-31", "2024-01-01"]

for i in range(3):
    crsr.execute(
        'INSERT INTO emp VALUES ({pk[i]}, "{f_name[i]}", "{l_name[i]}", "{date[i]}")'
    )

connection.commit()

connection.close()

while True:
    schedule.run_pending()
    time.sleep(60)
