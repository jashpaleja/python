import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="manishpaleja"
                               ,database="jash")
# print(mydb)
mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE user (name VARCHAR(255), age INT)")
# mycursor.execute("SHOW  TABLES")
#
# for x in mycursor:
#   print(x)
# sql = "INSERT INTO user (name, age) VALUES (%s, %s)"
# val = ("Jash", "19")
# mycursor.execute(sql, val)
#
# mydb.commit()


# ## For adding many data at the same time ##
# sqlFormula = "INSERT INTO user (name,age) VALUES(%s,%s)"
# students = [("ZEEL",10),
#              ("VEDANT",20),
#              ("VIRAJ",19),
#              ("ABHISHEK",39)]
# mycursor.executemany(sqlFormula,students)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid)
# """to print the whole db"""
# mycursor.execute("SELECT * FROM user")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)


# """how to search in db """
# NAME
# mycursor.execute("SELECT * FROM user WHERE name ='ZEEL'")
# # result = mycursor.fetchall()

# AGE
# mycursor.execute("SELECT * FROM user WHERE age =20")

# mycursor.execute("SELECT * FROM user WHERE name LIKE '%as%'")
# result = mycursor.fetchall()
# for z in result:
#     print(z)
# ANOTHER METHOD
# sql = ("SELECT * FROM user WHERE name = %s")
# mycursor.execute(sql, ("zeel",))
# mycursor.execute("SELECT * FROM user ORDER BY name")
# mycursor.execute("SELECT * FROM user ORDER BY age DESC")
#
# result = mycursor.fetchall()
# for z in result:
#     print(z)

# HOW TO UPDATE DB
# sql = "UPDATE user SET age = 25 WHERE name ='zeel'"
# mycursor.execute(sql)
# mydb.commit()



# TO SET A LIMIT

# mycursor.execute("SELECT * FROM user LIMIT 3 OFFSET 1")
# result = mycursor.fetchall()
# for j in result:
#     print(j)


# ORDER THE DB BY NAME OR AGE
# sql = "SELECT * FROM students ORDER BY name"
# sql = "SELECT * FROM students ORDER BY age DESC"
#       # "DESC" is decending
# mycursor.execute(sql)
# results = mycursor.fetchall()
# for i in results:
#     print(i)

# HOW TO DELETE FROM DB
# sql = "DELETE FROM user WHERE name = 'ABHISHEK'"

# DELETING THE WHOLE TABLE

mycursor.execute("DROP TABLE user")
mydb.commit()