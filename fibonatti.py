n=int(input("digite um numero: "))
def fibonatti(n):
	if n <= 1:
		return n
	else:
		return fibonatti(n-1)+fibonatti(n-2)
for i in range(n):
	print(fibonatti(i))