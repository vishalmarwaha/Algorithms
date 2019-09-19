
nlist = [7, 1, 2, 3, 4, 5, 6]
size = len(nlist)
for n in range(0,size):
	for m in range(n+1,size):
		if nlist[n]>nlist[m]:
			temp = nlist[n]
			nlist[n] = nlist[m]
			nlist[m] = temp
			
olist = []
i = 0
for n in range(size-1,size/2-1,-1):
	olist.insert(i,nlist[n])
	i +=2
	
j = 1
for n in range(0,size/2):
	olist.insert(j,nlist[n])
	j +=2


print olist
