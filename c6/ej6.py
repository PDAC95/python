# vocales
frase = input("Frase: ").lower()

cont_a = cont_e = cont_i = cont_o = cont_u = 0

for letra in frase:
    if letra == 'a': cont_a += 1
    elif letra == 'e': cont_e += 1
    elif letra == 'i': cont_i += 1
    elif letra == 'o': cont_o += 1
    elif letra == 'u': cont_u += 1

print(f"a:{cont_a}, e:{cont_e}, i:{cont_i}")
print(f"o:{cont_o}, u:{cont_u}")
