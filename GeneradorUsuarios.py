import random
from datetime import datetime, timedelta

# Función para generar un nombre ficticio
def generar_nombre():
    nombres = ["Ana", "Carlos", "Juan", "Maria", "Pedro", "Laura", "Luis", "Raquel", "Sofia", "David", "Marta", "Fernando", "Paula", "Eduardo", "Javier"]
    apellidos = ["Gonzalez", "Lopez", "Martinez", "Rodriguez", "Perez", "Sanchez", "Ramirez", "Torres", "Diaz", "Hernandez", "Garcia", "Fernandez"]
    return f"{random.choice(nombres)} {random.choice(apellidos)}"

# Función para generar un DNI ficticio
def generar_dni():
    return str(random.randint(10000000, 99999999))

# Función para generar una dirección ficticia
def generar_direccion():
    calles = ["Calle Falsa", "Avenida Principal", "Calle 5", "Calle San Juan", "Avenida de la Paz", "Calle Libertad"]
    numeros = random.randint(1, 100)
    return f"{random.choice(calles)} {numeros}, Ciudad Imaginaria"

# Función para generar un teléfono ficticio
def generar_telefono():
    return f"+57 {random.randint(600000000, 699999999)}"

# Función para generar un correo ficticio
def generar_correo(nombre):
    correos = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    return f"{nombre.replace(' ', '.').lower()}@{random.choice(correos)}"

# Función para generar un código QR ficticio
def generar_codigo_qr():
    return f"QR-{random.randint(100000, 999999)}"

# Función para generar una fecha de registro aleatoria
def generar_fecha_registro():
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 12, 31)
    delta_days = (end_date - start_date).days
    random_date = start_date + timedelta(days=random.randint(0, delta_days))
    return random_date.strftime("%Y-%m-%d")

# Función para generar el estado
def generar_estado():
    return random.choice(["activo", "inactivo"])

# Generar los 40 usuarios o la cantidad que quieras.
usuarios = []
for _ in range(40):
    nombre = generar_nombre()
    dni = generar_dni()
    direccion = generar_direccion()
    telefono = generar_telefono()
    correo = generar_correo(nombre)
    codigo_qr = generar_codigo_qr()
    fecha_registro = generar_fecha_registro()
    estado = generar_estado()
    usuarios.append((nombre, dni, direccion, telefono, correo, codigo_qr, fecha_registro, estado))

# Crear las instrucciones SQL para insertar los datos
sql_inserts = "INSERT INTO usuarios (nombre, dni, direccion, telefono, correo, codigo_qr, fecha_registro, estado) VALUES\n"
sql_inserts += ",\n".join([f"('{usuario[0]}', '{usuario[1]}', '{usuario[2]}', '{usuario[3]}', '{usuario[4]}', '{usuario[5]}', '{usuario[6]}', '{usuario[7]}')" for usuario in usuarios])
sql_inserts += ";"

print(sql_inserts)
