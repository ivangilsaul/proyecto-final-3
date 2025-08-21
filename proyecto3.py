import json
import os

# Ruta del archivo donde se guardan los usuarios
ARCHIVO_USUARIOS = "usuarios.json"

# Cargar usuarios desde archivo (si existe)
def cargar_usuarios():
    if os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "r") as archivo:
            return json.load(archivo)
    else:
        return {}

# Guardar usuarios en archivo
def guardar_usuarios(usuarios):
    with open(ARCHIVO_USUARIOS, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

# Función para registrar usuario
def registrar_usuario(usuarios):
    nombre = input("Nombre: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    if email in usuarios:
        print("Este email ya está registrado.")
    else:
        usuarios[email] = {
            "nombre": nombre,
            "contraseña": contraseña
        }
        guardar_usuarios(usuarios)
        print("Usuario registrado con éxito.")

# Función para login
def login(usuarios):
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    if email in usuarios:
        if usuarios[email]["contraseña"] == contraseña:
            print(f"Bienvenido/a, {usuarios[email]['nombre']}!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

# Función para mostrar todos los usuarios
def mostrar_usuarios(usuarios):
    print("\nLista de usuarios registrados:")
    for email, datos in usuarios.items():
        print(f" - {datos['nombre']} ({email})")
    print()

# Buscar un usuario por email
def buscar_usuario(usuarios):
    email = input("Ingresa el email a buscar: ")
    if email in usuarios:
        print(f"Encontrado: {usuarios[email]['nombre']} ({email})")
    else:
        print("Usuario no encontrado.")

# Eliminar un usuario
def eliminar_usuario(usuarios):
    email = input("Ingresa el email del usuario a eliminar: ")
    if email in usuarios:
        confirmacion = input(f"¿Seguro que deseas eliminar a {usuarios[email]['nombre']}? (s/n): ")
        if confirmacion.lower() == "s":
            usuarios.pop(email)
            guardar_usuarios(usuarios)
            print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

# Cambiar contraseña
def cambiar_contraseña(usuarios):
    email = input("Ingresa tu email: ")
    if email in usuarios:
        contraseña_actual = input("Ingresa tu contraseña actual: ")
        if usuarios[email]["contraseña"] == contraseña_actual:
            nueva = input("Ingresa tu nueva contraseña: ")
            usuarios[email]["contraseña"] = nueva
            guardar_usuarios(usuarios)
            print("Contraseña actualizada.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")

# Menú principal
def menu():
    usuarios = cargar_usuarios()
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver todos los usuarios")
        print("4. Buscar usuario por email")
        print("5. Eliminar usuario")
        print("6. Cambiar contraseña")
        print("7. Salir")

        opcion = input("Elige una opción (1-7): ")

        if opcion == "1":
            registrar_usuario(usuarios)
        elif opcion == "2":
            login(usuarios)
        elif opcion == "3":
            mostrar_usuarios(usuarios)
        elif opcion == "4":
            buscar_usuario(usuarios)
        elif opcion == "5":
            eliminar_usuario(usuarios)
        elif opcion == "6":
            cambiar_contraseña(usuarios)
        elif opcion == "7":
            print("Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar programa
menu()