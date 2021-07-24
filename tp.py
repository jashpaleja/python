# import datetime
# begin_time = datetime.datetime.now()

def app(x,c):
        if x in li:
            pass
        else:
            li.append(x)

def op(m,n):
    for x in range(1,m+1):
        for y in range(1,n+1):
            num=(x*y)+x+y
            numstr=str(x)+str(y)
            if(str(num)==numstr):
                counter=counter+1
                app(x,c)
            else:
                pass

    # print(li)
arr=[]
t=int(input())
for i in range(0,t):
    arr.append(list(map(int, input().split())))
for l in arr:
    c=0
    li=[0]
    counter=0
    m=l[0]
    n=l[1]

    print(f"{counter} {len(li)-1}")
    print(li)
# print(datetime.datetime.now() - begin_time)
