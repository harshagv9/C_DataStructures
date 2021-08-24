def foo(x,y,q):
	if (x <= 0) & (y <= 0):
		return q
	if (y <= 0):
		return foo(x-q,y,q)
	if (x <= 0):
		return foo(x,y-q,q)
	return foo(x-q,y,q) + foo(x,y-q,q)

print(foo(15,15,10))












