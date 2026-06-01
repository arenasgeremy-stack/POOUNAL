'''Un equipo de programadores desea participar en una maratón de programación. El equipo tiene los siguientes atributos:
Nombre del equipo (tipo String).
Universidad que está representando el equipo (tipo String).
Lenguaje de programación que va a utilizar el equipo en la competencia (tipo String).
Tamaño del equipo (tipo int).
Se requiere un constructor que inicialice los atributos del equipo. El
equipo está conformado por varios programadores, mínimo dos y máximo
418 Cada programador posee nombre y apellidos (de tipo String). Se requieren además los siguientes métodos:
Un método para determinar si el equipo está completo.
Un método para añadir programadores al equipo. Si el equipo está
lleno se debe imprimir la excepción correspondiente.
Un método para validar los atributos nombre y apellidos de un
programador para que reciban datos que sean solo texto. Si se reciben datos numéricos se debe generar la excepción correspondiente. 
Además, no se permiten que los campos String tengan una
longitud igual o superior a 20 caracteres.
En un método main se debe crear un equipo solicitando sus datos por
teclado y se validan los nombres y apellidos de los programadores.'''

class Equipo:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion, tamano_equipo):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.tamano_equipo = int(tamano_equipo)
        self.programadores = []

    def esta_completo(self):
        if len(self.programadores) <= 418:
            return True
        else:
            return False

    def añadir_programador(self, nombre, apellidos):
        if self.esta_completo():
            raise Exception("El equipo está lleno")
        if not nombre.isalpha() or not apellidos.isalpha():
            raise ValueError("Los nombres y apellidos deben ser solo texto")
        if len(nombre) >= 20 or len(apellidos) >= 20:
            raise ValueError("Los campos String no pueden tener una longitud igual o superior a 20 caracteres")
        self.programadores.append((nombre, apellidos))

Queso = Equipo(input("Ingrese el nombre del equipo: "), input("Ingrese la universidad que representa el equipo: "), 
input("Ingrese el lenguaje de programación que va a utilizar el equipo: "), input("Ingrese el tamaño del equipo: "))

'''Ejercicios propuestos
u Se requiere desarrollar una contraseña válida. Los requisitos de la
contraseña son los siguientes:
○ Mínimo 8 caracteres.
○ No debe tener espacios en blanco.
○ Debe tener por lo menos un carácter, un carácter en mayúscula,
un número y un carácter especial.
○ La contraseña se debe ingresar dos veces para su confirmación.
Se lanzarán excepciones si no se cumplen dichos requerimientos y si
las dos contraseñas no son iguales.'''
class password():
    def __init__(self, password1, password2):
        self.password1 = password1
        self.password2 = password2

    def validate_password(self):
        if len(self.password1) < 8:
            raise Exception("La contraseña debe tener al menos 8 caracteres.")
        if " " in self.password1:
            raise Exception("La contraseña no debe contener espacios en blanco.")
        if not any(char.isupper() for char in self.password1):
            raise Exception("La contraseña debe contener al menos una letra mayúscula.")
        if not any(char.isdigit() for char in self.password1):
            raise Exception("La contraseña debe contener al menos un número.")
        if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in self.password1):
            raise Exception("La contraseña debe contener al menos un carácter especial.")
        if self.password1 != self.password2:
            raise Exception("Las contraseñas no coinciden.")
        return "Contraseña válida."

while True:
    try:
        password1 = input("Ingrese la contraseña: ")
        password2 = input("Confirme la contraseña: ")
        pwd = password(password1, password2)
        print(pwd.validate_password())
        break
    except Exception as e:
        print("Error:", e)
        print("Intente nuevamente.\n")
    