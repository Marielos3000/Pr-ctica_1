from enum import Enum

# Clase enumerada para los roles
class Rol(Enum):
    ADMIN = "Administrador"
    USUARIO = "Usuario"

# Clase Lugar
class Lugar:
    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Lugar: {self.nombre}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

# Clase Foto
class Foto:
    def __init__(self, ubicacion_archivo: str, tipo_archivo: str, tamano: float):
        self.ubicacion_archivo = ubicacion_archivo
        self.tipo_archivo = tipo_archivo
        self.tamano = tamano

    def __str__(self):
        return f"Foto - Ubicación: {self.ubicacion_archivo}, Tipo: {self.tipo_archivo}, Tamaño: {self.tamano}MB"

# Clase Persona
class Persona:
    def __init__(self, nombre: str, apellido: str, rol: Rol, foto: Foto):
        self.nombre = nombre
        self.apellido = apellido
        self.roles = [rol]              # Lista de roles
        self.lugares_frecuentes = []    # Lista de lugares frecuentes
        self.foto = foto

    def agregar_lugar_frecuente(self, lugar: Lugar):
        self.lugares_frecuentes.append(lugar)

    def set_rol(self, rol: Rol):
        if rol not in self.roles:
            self.roles.append(rol)
    
    def __str__(self):
        lugares_str = "\n".join(str(lugar) for lugar in self.lugares_frecuentes)
        roles_str = ", ".join([rol.name for rol in self.roles])
        return (f"Persona: {self.nombre} {self.apellido}, Roles: {roles_str}\n"
                f"Foto: {self.foto}\n"
                f"Lugares Frecuentes:\n{lugares_str}")

# Clase Main para ejecutar el programa
def main():
    # Crear lugares
    lugar1 = Lugar("Universidad", "Zona 12", "5717-4298")
    lugar2 = Lugar("Biblioteca", "Zona 12", "3333-4444")
    lugar3 = Lugar("Jardín", "Zona 4", "8888-5555")
    lugar4 = Lugar("Cafetería", "Zona 10", "1111-7777")
    
    # Crear fotos
    foto1 = Foto("/imagenes/jose.jpg", "jpg", 1.5)
    foto2 = Foto("/imagenes/marielos.png", "jpg", 6.9)
    
    # Crear personas con roles diferentes
    persona1 = Persona("", "López", Rol.ADMIN, foto1)
    persona2 = Persona("Marielos", "Alegria", Rol.USUARIO, foto2)
    
    # Agregar lugares a las personas
    persona1.agregar_lugar_frecuente(lugar1)
    persona1.agregar_lugar_frecuente(lugar2)
    
    persona2.agregar_lugar_frecuente(lugar3)
    persona2.agregar_lugar_frecuente(lugar4)
    
    # Mostrar información
    print(persona1)
    print("""
         ✦———————✿———————✦—✿—✦———————✿———————✦
    """)
    print(persona2)

if __name__ == "__main__":
    main()
