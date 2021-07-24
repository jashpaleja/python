def minCntCharDeletionsfrequency(str, N):
    mp = {}
    pq = []
    cntChar = 0
    for i in range(N):
		mp[str[i]] = mp.get(str[i], 0)+1
	for it in mp:
		pq.append(mp[it])
	pq = sorted(pq)
	while (len(pq) > 0):
		frequent = pq[-1]
		del pq[-1]
		if (len(pq) == 0):
			return cntChar
		if (frequent == pq[-1]):
			if (frequent > 1):
				pq.append(frequent - 1)
				
			cntChar += 1
			
		pq = sorted(pq)
		
	return cntChar

if _name_ == '_main_':
	
	str = "ceabaacb"

	N = len(str)
	
	print(minCntCharDeletionsfrequency(str, N))