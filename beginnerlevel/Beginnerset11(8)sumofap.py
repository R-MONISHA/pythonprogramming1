try:
	(a,b,c)=map(int,sys.stdin.readline().split())
	print(int(a+(c-1)*b))
except:
	print('invalid')
