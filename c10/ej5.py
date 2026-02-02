from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9,10]
total_encadenado = reduce(
    lambda a,b: a + b,
    map(
        lambda x: x **2,
        filter(lambda x: x % 2 == 0, numeros)
    )
)