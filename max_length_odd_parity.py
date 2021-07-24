def sol(s,n):
    li=[]
    for i in s:
        li.append(i)
    se = set(li)
    freq = dict()
    for i in se:
        freq[i]= li.count(i)
    print(freq)
    li=list(freq.values())
    f_n=dict()
    for i in li:
        f_n[i] = li.count(i)
    xx = list(f_n.values())
    print(f_n,max(xx))
    key = 0
    for i in f_n:
        if f_n[i] == max(xx):
            if key<i:
                key=i

    answer = 0
    for i in freq:
        if freq[i] != key:
            answer += abs(freq[i]-key)
    return answer

S = "ceeabcdb"
N = len(S)

print (sol(S, N))