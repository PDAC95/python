def dividir(a,b):
    if b ==0:
        raise ValueError("nose puede dividir entre cero")
    return a/b

print (dividir(10,2)) #5.0
print (dividir(10,0))