import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error


conn = mysql.connector.connect("cis3368.czszkhju4z7p.us-east-1.rds.amazonaws.com", "admin", "$Koid031", "cis3368db")
cursor = conn.cursor(dictionary=True)
sql = "SELECT * FROM contacts"
cursor.execute(sql)
rows = cursor.fetchall()
for row in rows:
    print(row)
    print(row["fullName"], row["contactDetails"])

