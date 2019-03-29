#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
import mysql.connector

app = Flask(__name__)

def connect_db():
  mydb = mysql.connector.connect(
    host="mydatabase",
    user="mysql",
    passwd="mysql",
    database="microservice"
  )
  mycursor = mydb.cursor()
  print("MySQL connected")
  return (mydb, mycursor)

def disconnect_db(db, cursor):
  if(db.is_connected()):
    cursor.close()
    db.close()
    print("MySQL connection is closed")

@app.route("/put")
def put():
  try:
    mydb, mycursor = connect_db()
    mycursor.execute("INSERT INTO buttonpushed(button_date) VALUES (NOW());")
    mydb.commit()
    message = "1 record inserted, ID:" + str(mycursor.lastrowid)
  except mysql.connector.Error as error :
    mydb.rollback()
    message= "Failed to insert into MySQL table {}".format(error)
    print("MySQL insertion failed")
  finally:
    disconnect_db(mydb, mycursor)
    return message

@app.route("/")
def get():
  try:
    mydb, mycursor = connect_db()
    mycursor.execute("SELECT button_date FROM buttonpushed;")
    myresult = mycursor.fetchall()
    message = '\n'.join(map(str, myresult))
  except mysql.connector.Error as error :
    message= "Failed to select from MySQL table {}".format(error)
    print("MySQL select failed")
  finally:
    disconnect_db(mydb, mycursor)
    return message

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0")
