d1={"Name":"Abhishek" , "Age":"19" , "Dept":"Computer"}
print(d1)
print("After changing:")
d1["Age"] = 20
d1["Nickname"] = "Abhi"
print(d1)
d2 = sorted(d1.keys())
print(d2)
if "Age" in d1.keys():
	print (d1["Age"])
if "Computer" in d1.values():
	print ("Key found !")
l1=["Name","Age","Gender"]
l2=["Abhishek","19","Male"]
dic={}
for i in range(len(l1)):
	dic[l1[i]]=l2[i]
print(dic)
