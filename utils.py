def factorial(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res
def simple(x):
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    return True




