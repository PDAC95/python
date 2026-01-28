# Datos de configuración que vienen de un archivo JSON

config_servidor = {

    "host": "api.ejemplo.com",

    "puerto": 443,

    "timeout": 30,

    "ssl": True

}


def conectar(host, puerto, timeout=10, ssl=False):

    print(f"Conectando a {host}:{puerto}")

    print(f"Timeout: {timeout}, SSL: {ssl}")


# Pasamos toda la config de una vez

conectar(**config_servidor)