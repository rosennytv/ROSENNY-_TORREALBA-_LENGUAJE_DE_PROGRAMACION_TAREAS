# ==============================================================================
# Instituto Superior Tecnológico Rumiñahui - ISTER
# Carrera de Infraestructura de Redes y Ciberseguridad
# Asignatura: Lenguaje de Programación Python
# Tarea práctica - Semana 3
# Estudiante: Rosenny Andreina Torrealba Vera
# Docente: Ing. Héctor Llerena, MSc
# ==============================================================================

# ------------------------------------------------------------------------------
# Ejercicio 1. ¿Es el protocolo seguro? (condicionales)
# ------------------------------------------------------------------------------
print("--- Ejercicio 1 ---")
protocolos_a_probar = ["HTTPS", "Telnet", "FTP", "SSH", "Desconocido"]

for protocolo in protocolos_a_probar:
    # Verificación usando condicionales y operadores lógicos (or)
    if protocolo == "HTTPS" or protocolo == "SSH" or protocolo == "SFTP":
        print(f"El protocolo {protocolo} es SEGURO")
    elif protocolo == "HTTP" or protocolo == "Telnet" or protocolo == "FTP":
        print(f"El protocolo {protocolo} es INSEGURO")
    else:
        print(f"El protocolo '{protocolo}' es: Desconocido")
print()

# ------------------------------------------------------------------------------
# Ejercicio 2. Identificar el servicio según el puerto (if / elif / else)
# ------------------------------------------------------------------------------
print("--- Ejercicio 2 ---")
puertos_a_probar = [443, 8080, 22, 3306]

for puerto in puertos_a_probar:
    # Cadena de if-elif-else para asignar el servicio correspondiente
    if puerto == 22:
        servicio = "SSH"
    elif puerto == 80:
        servicio = "HTTP"
    elif puerto == 443:
        servicio = "HTTPS"
    elif puerto == 3306:
        servicio = "MySQL"
    elif puerto == 3389:
        servicio = "RDP"
    else:
        servicio = "Servicio desconocido"

    print(f"Puerto {puerto}: {servicio}")
print()

# ------------------------------------------------------------------------------
# Ejercicio 3. Listar IPs de una subred (bucle for con range)
# ------------------------------------------------------------------------------
print("--- Ejercicio 3 ---")
# range(8) genera números del 0 al 7 inclusive
for i in range(8):
    # Construcción de la IP usando f-strings
    print(f"192.168.1.{i}")
print()

# ------------------------------------------------------------------------------
# Ejercicio 4. Inventario numerado de dispositivos (for con enumerate)
# ------------------------------------------------------------------------------
print("--- Ejercicio 4 ---")
dispositivos = ["Router Cisco", "Switch HP", "Firewall Fortinet", "Servidor Dell"]

# Se utiliza start=1 para que la numeración visible empiece desde 1
for posicion, valor in enumerate(dispositivos, start=1):
    print(f"{posicion}. {valor}")
print()

# ------------------------------------------------------------------------------
# Ejercicio 5. Cuenta regresiva de apagado (bucle while)
# ------------------------------------------------------------------------------
print("--- Ejercicio 5 ---")
contador = 5

# Bucle condicional que se ejecuta mientras el contador sea mayor o igual a 1
while contador >= 1:
    print(f"Apagado en: {contador}")
    contador -= 1  # Actualización de la variable de control para evitar bucle infinito

print("Apagando servidor...")
print()

# ------------------------------------------------------------------------------
# Ejercicio 6. Reintento de conexión (while con condición compuesta)
# ------------------------------------------------------------------------------
print("--- Ejercicio 6 ---")
intento = 1
conectado = False

# Condición compuesta: se ejecuta mientras no exceda los 5 intentos y no esté conectado
while intento <= 5 and not conectado:
    if intento == 3:
        conectado = True
        print(f"Intento {intento}:")
        print("CONECTADO")
    else:
        print(f"Intento {intento}: sin respuesta")

    intento += 1
print()

# ------------------------------------------------------------------------------
# Ejercicio 7. Primer puerto cerrado (uso de break)
# ------------------------------------------------------------------------------
print("--- Ejercicio 7 ---")
puertos = [21, 22, 23, 25, 80]
estados = ["abierto", "abierto", "abierto", "cerrado", "abierto"]

# zip() permite recorrer ambas listas de forma paralela en el mismo ciclo
for puerto, estado in zip(puertos, estados):
    if estado == "cerrado":
        print(f"Primer puerto cerrado: {puerto}")
        break  # Interrumpe el bucle de manera inmediata
    print(f"Puerto {puerto}: {estado}")
print()

# ------------------------------------------------------------------------------
# Ejercicio 8. Filtrar IPs de la lista negra (uso de continue)
# ------------------------------------------------------------------------------
print("--- Ejercicio 8 ---")
ips_log = ["10.0.0.5", "200.0.0.1", "10.0.0.8", "45.33.32.156", "10.0.0.10"]
blacklist = ["200.0.0.1", "45.33.32.156"]
total_procesadas = 0

for ip in ips_log:
    if ip in blacklist:
        continue  # Salta el resto del código de esta iteración y va a la siguiente IP

    print(f"Procesando: {ip}")
    total_procesadas += 1

print(f"Total procesadas: {total_procesadas}")
print()

# ------------------------------------------------------------------------------
# Ejercicio 9. Buscar dispositivo en inventario (else en bucle)
# ------------------------------------------------------------------------------
print("--- Ejercicio 9 ---")
inventario = ["Router-01", "Switch-A", "Firewall-FW1", "Servidor-Web"]

# Caso de prueba 1: "Firewall-FW1" (Sí está)
buscar_1 = "Firewall-FW1"
print(f"Buscando: '{buscar_1}'")
for d in inventario:
    if d == buscar_1:
        print("Encontrado")
        break
else:
    # Este bloque solo se ejecuta si el bucle termina normalmente (sin romperlo con break)
    print("No encontrado en el inventario")

# Caso de prueba 2: "Switch-Z" (No está)
buscar_2 = "Switch-Z"
print(f"Buscando: '{buscar_2}'")
for d in inventario:
    if d == buscar_2:
        print("Encontrado")
        break
else:
    print("No encontrado en el inventario")
print()

# ------------------------------------------------------------------------------
# Ejercicio 10. Validador de dirección IPv4 (integrador)
# ------------------------------------------------------------------------------
print("--- Ejercicio 10 ---")
ips_test = ["192.168.1.1", "10.0.0.255", "256.1.1.1", "192.168.1", "192.168.a.l"]

for ip in ips_test:
    partes = ip.split(".")
    valida = True
    motivo = ""

    # Validación 1: Verificar que tenga exactamente 4 octetos
    if len(partes) != 4:
        valida = False
        motivo = "faltan octetos o excede la cantidad"
    else:
        # Validación 2: Evaluar cada octeto de manera individual
        for octeto in partes:
            # Comprobar si el contenido es completamente numérico
            if not octeto.isdigit():
                valida = False
                motivo = "no numerico"
                break

            # Comprobar si el valor entero está dentro del rango permitido (0-255)
            num = int(octeto)
            if num < 0 or num > 255:
                valida = False
                motivo = "octeto fuera de rango"
                break

    # Imprimir los resultados según los hallazgos correspondientes
    if valida:
        print(f"{ip} -> Valida")
    else:
        print(f"{ip} -> Invalida ({motivo})")
