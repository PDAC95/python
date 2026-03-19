"""
Clase 27: Consumir API del clima
Open-Meteo - Sin API key
"""
import requests

CIUDADES = {
    'mexico': ('Ciudad de México', 19.43, -99.13),
    'buenos_aires': ('Buenos Aires', -34.61, -58.38),
    'madrid': ('Madrid', 40.42, -3.70),
    'bogota': ('Bogotá', 4.71, -74.07),
    'lima': ('Lima', -12.04, -77.03),
}

WEATHER_CODES = {
    0: 'Despejado ☀️',
    1: 'Mayormente despejado 🌤️',
    2: 'Parcialmente nublado ⛅',
    3: 'Nublado ☁️',
    45: 'Niebla 🌫️',
    48: 'Niebla con escarcha 🌫️',
    51: 'Llovizna ligera 🌦️',
    53: 'Llovizna moderada 🌦️',
    55: 'Llovizna intensa 🌧️',
    61: 'Lluvia ligera 🌧️',
    63: 'Lluvia moderada 🌧️',
    65: 'Lluvia intensa 🌧️',
    71: 'Nieve ligera ❄️',
    73: 'Nieve moderada ❄️',
    75: 'Nieve intensa ❄️',
    95: 'Tormenta ⛈️',
}


def obtener_clima(ciudad, lat, lon):
    """Obtiene el clima actual de una ubicación"""
    url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': True
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['current_weather']
    except requests.exceptions.RequestException as e:
        print(f"Error obteniendo clima de {ciudad}: {e}")
        return None


if __name__ == '__main__':
    print("🌍 Clima actual en ciudades de habla hispana:\n")

    for key, (nombre, lat, lon) in CIUDADES.items():
        clima = obtener_clima(nombre, lat, lon)
        if clima:
            code = clima['weathercode']
            descripcion = WEATHER_CODES.get(code, f'Código {code}')
            print(f"  {nombre}:")
            print(f"    🌡️  Temperatura: {clima['temperature']}°C")
            print(f"    💨 Viento: {clima['windspeed']} km/h")
            print(f"    {descripcion}")
            print()
