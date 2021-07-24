import mysql.connector
dbconn = mysql.connector.connect(host = "localhost",user = "root",passwd = "")
cursor = dbconn.cursor()
cursor.execute("Create database pythontest")
cursor.execute("use pythontest")
cursor.execute("create table test(name varchar(20) , age int(100) , pointer int(11))")
for i in range(0,3):
	n = input("Enter name")
	a = int(input("Enter age"))
	p = int(input("Enter pointer"))
	cursor.execute("insert into test(name,age,pointer) VALUES('%s',%s,%s)"%(n,a,p))
dbconn.commit()
print("Students with pointer >= 9: ")
cursor.execute("Select name from test where pointer >= 9")
x = cursor.fetchall()
for i in x:
	print(i)
print("Students in pointers of decreasing order")
cursor.execute("Select name,pointer from test order by pointer DESC")
x = cursor.fetchall()
for i in x:
	print(i)
#cursor.execute("Delete where pointer = 6")
cursor.execute("select * from test")
x = cursor.fetchall()
for i in x :
	print(i)