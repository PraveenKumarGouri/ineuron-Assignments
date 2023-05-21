import mysql.connector as conn
mydb= conn.connect(host="localhost",user="root",passwd="Login123$")
print(mydb)