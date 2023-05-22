n=int(input())

def matriz_quadrada(t):
	m=[[0 for x in range (t)] for x in range(t)]
	for j in range(t):
			for k in range(j,t-j):
					m[j][k]=j+1
					m[k][j] =j+1
					m[t-j-1][k]=j+1
					m[k][t-j-1]=j+1
	for elem in m:
		print(elem)
while(n>0):
	matriz_quadrada(n)
	n=int(input())
	