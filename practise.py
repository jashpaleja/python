# # # print("""use for long
# # # paragraphs
# # # u can typeanything
# # #
# # #
# # #
# # # """)
# # # print("*" * 10)
# # # c="formated strings"
# a="very good"
# # b="boy"
# # msg = f"jash is a {a} [{b}]"
# # print(msg)
# print(a.upper())
# # inbuild function in string for converting every element to upper case
# print(a.lower())
# # inbuild function in string for converting every element to lower case
# print(a.find('g'))
# # gives the position of the given string element
# print(a.replace("good","bad"))
# # inbuild function to replace a string
# print(len(a))
# #gives the length of the string in the output
# print("very" in a)
# # used to check if the given part is inside the string or not,gives a boolean output.
# string='abcdefghi'
# print(string[2 : ])   #  o/p => cdefgh
# print(string[ : 5])    # o/p:- abcde
# print(string[ 1:3])  # o/p:- bc
# print(string[ : : ]) # o/p:- abcdefhgi
# print(string[ : : 2 ])  #o/p:- acegi
# print(string[ : : -1]) # o/p:-ihgfedcba
# print(string[ 1: 5 : 2 ]) # o/p:- bd
# print(string[ : : -3]) # o/p:-ifc

# name="Ramesh"
# name[0]='P'
# o/p:- Erro
# mystring= "Hello World"
# #          012345678910
# print(mystring[0])
# print(mystring[8])
# print(mystring[-1])
# # # ##https://docs.python.org/3/library/math.html
# # # #math module functions inbuild list#
# # a=list(map(int, input().split()))
# # b=list(map(int, input().split()))
# # c=[0,0]
#
# # for i in range(0,3):
# #     print(i)
#     # if a[i]>b[i]:
#     #      c[0]=c[0]+1
#     # elif a[i]<b[i]:
#     #      c[1]=c[1]+1
#     # else:
#         # pass
#
# # print(f"{c[0]} {c[1]}")
# # i = 0
# # while (i < 3):
# #    print(i)
# #     i += 1   # this has to be done by the user to increment in while
# # a=[[1,2,3],[4,5,6],[7,8,9]]
# r=int(input('enter rows'))
# c=int(input('enter columns'))
# matrix=[]
# for row in range(0,r):
#     a = []
#     for col in range(0,c):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)


# print(list[0])
# print(list[1:3])
# print(list[0:2])
# list.append(53)
# a=[]
# tuple1 = ('jash', 'vedant', 19)
# tuple2=('jash', 3908, 53)
# print(tuple1+tuple2)
# print(list)
# x= 8j
# print(int(x))
# dict = {'Name': 'Jash', 'Age': 19, 'Class': 'SE'}
# del dict["Name"]
# print(dict)
#
# def pre(name):
#     print(f'hello {name}')
#
# pre('jash')
# # pre('vedant')
# def fucn(name,age):
# 	print(f"I am {name} and my age is {age}")
#
# fucn("jash",19)
# fucn("dhairya",13)
# def fucn(*sub):
# 	print(f"My subjects is {sub[0]}")
# fucn("math","physics","chemistry")
# def fun(a):
# 	for x in a:
# 		print(x)
# a=[1,"jash",53,"hi"]
# fun(a)
# def fucn(sub1,sub2,sub3):
# 	print("My subjects are")
# 	print(sub1)
# 	print(sub2)
# 	print(sub3)
#
# fucn(sub3 = "math",sub1 = "physics",sub2 = "chemistry")
# def tableof5(num):
# 	return 5*num
#
# print(tableof5(3))
# print(tableof5(10))
# print(tableof5(13))
# print(tableof5(2))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("enter a number: "))
# print(factorial(n))

x = int(input())
arr= list(map(int,input().split()))
res = []
u=0
[res.append(x) for x in arr if x not in res]
arr2=[]
for x in res:
    y=arr.count(x)
    arr2.append(y)
max=max(arr2)
u=sum(arr2)-max
print(u)

