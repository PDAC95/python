def test_lista_completa():
   resultado = obtener_numeros()
   assert resultado == [1, 2, 3, 4, 5]

   def test_elemnto_en_lista():
       resultado = obtener_numeros()
       assert 3 in resultado

assert 5 not in resultado
assert len(resultado) ==3
assert resultado == []
assert len(resultado) == 0


assert 'admin' in resultado
assert 'user' not in resultado

assert all (x > 0 for x in resultado)
assert all(isinstance(x, int) for x in resultado)