# Diccionario adaptado con los datos de Rosenny Torrealba
datos_rosenny = {
    "nombre": "Rosenny Andreina Torrealba Vera",
    "profesión": "TECNOLÓGA UNIVERSITARIA EN INFRAESTRUCTURA DE REDES Y CYBERSEGURIDAD",
    "institución": "Instituto Superior Tecnológico Rumiñahui",
    "estudiante": "INFRAESTRUCTURA DE REDES Y CYBERSEGURIDAD",
    "país": "Ecuador"
}

# Recorremos el diccionario usando .items()
for clave, valor in datos_rosenny.items():
    # Usamos .replace("_", " ").capitalize() para que las claves compuestas se vean impecables
    etiqueta = clave.replace("_", " ").capitalize()
    print(f"{etiqueta}: {valor}")