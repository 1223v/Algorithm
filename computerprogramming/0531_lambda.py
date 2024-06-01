result= (lambda x : x*x)(5)
print(result)

Dae = lambda s: s.upper()
result = Dae('test')
print(result)

Min = lambda a,b : b if a>b else a
result = Min(4,7)
print(result)

def filterfunc(x):
    if x %2 == 0 :
        return True
    else:
        return False

l = [3,4,5,6,7,8,1,2,3,4]

result = filter(filterfunc, l)
print(list(result))


