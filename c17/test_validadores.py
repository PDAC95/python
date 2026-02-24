from validadores import es_par, es_positivo, es_adulto, es_email_valido


# Tests de es_par
def test_es_par_con_par():
    assert es_par(4) == True


def test_es_par_con_impar():
    assert es_par(7) == False


def test_es_par_con_cero():
    assert es_par(0) == True  # 0 es par


# Tests de es_positivo
def test_es_positivo_positivo():
    assert es_positivo(5) == True


def test_es_positivo_negativo():
    assert es_positivo(-3) == False


def test_es_positivo_cero():
    assert es_positivo(0) == False  # 0 no es positivo


# Tests de es_adulto
def test_es_adulto_mayor():
    assert es_adulto(25) == True


def test_es_adulto_exacto():
    assert es_adulto(18) == True  # Caso edge


def test_es_adulto_menor():
    assert es_adulto(15) == False


def test_es_adulto_limite():
    assert es_adulto(17) == False  # Justo antes


# Tests de es_email_valido
def test_email_valido():
    assert es_email_valido("user@example.com") == True


def test_email_sin_arroba():
    assert es_email_valido("userexample.com") == False


def test_email_sin_punto():
    assert es_email_valido("user@examplecom") == False


def test_email_doble_arroba():
    assert es_email_valido("user@@example.com") == False
