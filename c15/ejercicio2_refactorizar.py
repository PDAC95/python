# ============================================
# EJERCICIO 2: Refactorizar codigo feo
# ============================================
# Mejora este codigo aplicando PEP 8:
# - Nombres descriptivos para funciones y variables
# - Espaciado correcto
# - Docstrings
# - Codigo legible

# CODIGO A REFACTORIZAR:
def p(d,k):
    if k in d:
        return d[k]
    else:
        return None

def a(l,v):
    l.append(v)
    return l

def c(l):
    n=[]
    for i in l:
        if i not in n:n.append(i)
    return n


# TODO: Reescribe las funciones aqui abajo con nombres claros y PEP 8
