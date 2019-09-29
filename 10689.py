def add(a,b):
    return a + b

def minus(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a // b

def divrest(a,b):
    return a % b

a , b = input().split()
a= int(a)
b= int(b)
print(add(a,b))
print(minus(a,b))
print(mul(a,b))
print(div(a,b))
print(divrest(a,b))
