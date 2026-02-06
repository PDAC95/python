emails = [

    "JUAN@GMAIL.COM",

    "maria@outlook.com",

    "PEDRO@YAHOO.COM",

    "ana@hotmail.com"

]


emails_lower = [email.lower() for email in emails]

print("Emails normalizados:", emails_lower)

dominios = [email.split('@')[1] for email in emails]

print("Dominios:", dominios)

dominios_lower = [email.split('@')[1].lower() for email in emails]

print("Dominios normalizados:", dominios_lower)

from collections import Counter

dominios = [email.split('@')[1].lower() for email in emails]

conteo = Counter(dominios)

print("Conteo:", dict(conteo))
