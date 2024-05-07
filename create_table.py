# general layout of python file to create a table if required
# this can be altered as required 

# author: Rachel King

import mysql.connector

import dbconfig as cfg

mydb = mysql.connector.connect(
 host= cfg.mysql['host'],
 user= cfg.mysql['user'],
 password= cfg.mysql['password'],
 database= cfg.mysql['database']
)

mycursor = mydb.connect.cursor()
sql="CREATE TABLE player (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, nationality VARCHAR(255), club VARCHAR(255))"

mycursor.execute(sql)

mycursor.close()