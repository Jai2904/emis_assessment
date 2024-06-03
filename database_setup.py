import pymysql

connection = pymysql.connect(host="localhost", user="root", password="password", database="patient_db")

cursor = connection.cursor()

with open("ddl_scripts.sql", encoding="utf-8") as f:
    commands = f.read().split(';')

for command in commands:
    if command:
        cursor.execute(command)

connection.close()