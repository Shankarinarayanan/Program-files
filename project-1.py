import mysql.connector

c=mysql.connector.connect(host='localhost',database='Employee',user='root',password='Shank09@')

if c.is_connected():
    print("connected to MySQL")
cursor=c.cursor()
cursor.execute("use Employee")
quest = (input("Enter text-"))
cursor.execute("select answers from lists where questions = "+"'"+quest+"'")
for row in iter(cursor.fetchone, None):
    print (row)
cursor.close()
c.close()
