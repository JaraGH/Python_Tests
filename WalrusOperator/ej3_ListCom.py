def f(v):
    return 2*v
datos = [2,4,10,24,19,1,13]

resultado = [(x, y, x/y) for x in datos if (y := f(x)) > 0]
print (resultado)