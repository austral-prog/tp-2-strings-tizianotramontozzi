def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)

    nombre = input("Ingrese su nombre completo:")
    email = input("Ingrese su email completo:")
    nota1 = input("Ingrese nota 1:")
    nota2 = input("Ingrese nota 2:")
    nota3 = input("Ingrese nota 3:")

    nombre_limpio = nombre.strip().title()

    email_minusculas = email.lower()

    largo_nombre = len(nombre_limpio)

    espacio = nombre_limpio.find(" ")
    iniciales = nombre_limpio[0] + nombre_limpio[espacio + 1]

    nombre_partes = nombre_limpio.split()
    usuario = nombre_partes[1].lower() + "." + nombre_partes[0].lower()

    tiene_arroba = "@" in email_minusculas

    pos_arroba = email_minusculas.find("@")
    dominio = email_minusculas[pos_arroba + 1:]

    nombre_guion = nombre_limpio.replace(" ", "_")

    cantidad_a = nombre_limpio.lower().count("a")

    codigo_secreto = nombre_limpio[::-1].upper()

    n1 = int(nota1)
    n2 = int(nota2)
    n3 = int(nota3)

    suma = n1 + n2 + n3
    promedio = suma / 3
    promedio_entero = suma // 3

    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")
    print(f"Nombre: {nombre_limpio}")
    print(f"Email: {email_minusculas}")
    print(f"Caracteres en nombre: {largo_nombre}")
    print(f"Iniciales: {iniciales}")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {tiene_arroba}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: {nombre_guion}")
    print(f"Cantidad de a: {cantidad_a}")
    print(f"Codigo secreto: {codigo_secreto}")
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")
    print("=" * 24)

ficha()


