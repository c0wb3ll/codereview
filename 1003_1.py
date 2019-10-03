c=[]
T = int(input())

def fibonacci(n):
    if n==0:
        return c.append(0)
    elif n==1:
        return c.append(1) 
    else:
        return fibonacci(n-1) , fibonacci(n-2)
        
for i in range(T):
    del c[:]
    n = int(input())
    fibonacci(n)
    print(c.count(0),c.count(1))


