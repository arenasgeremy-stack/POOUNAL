'''Se requiere un programa que modele el concepto de una persona. Una persona posee nombre, apellido, número de documento de identidad y año de
nacimiento. La clase debe tener un constructor que inicialice los valores de sus
respectivos atributos.
La clase debe incluir los siguientes métodos:
u Definir un método que imprima en pantalla los valores de los atributos del objeto.
u En un método main se deben crear dos personas y mostrar los valores de sus atributos en pantalla.
'''
from enum import Enum
class Genero(Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"
    PERUANO = "Peruano"#esto era el otro, solo que el ide me sugirio peruano y me causo gracia
class Persona:
    #esto es como el constructor del texto
    def __init__(self, nombre, apellido, edad, genero, cedula, pais_de_nacimiento):
        self.nombre = str(nombre).lower().capitalize()
        self.apellido = str(apellido).lower().capitalize()
        self.edad = int(edad)
        self.genero = genero
        self.cedula = int(cedula)
        self.pais_de_nacimiento = ((str(pais_de_nacimiento)).lower()).capitalize()

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad} años")
        print(f"Genero: {self.genero.value}")
        print(f"Cedula: {self.cedula}")
        print(f"Pais de nacimiento: {self.pais_de_nacimiento}\n")
#esta es mi prueba (seria un objeto)
persona1 = Persona("Geremy", "Arenas", 17, Genero.MASCULINO, 1015, "Colombia")
#aun no estoy seguro si esa persona2 deberia ir aqui o donde esta, persona2 con sus inputs seria el segundo objeto
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese la edad: ")
gen_input = input("Ingrese el genero (masculino/femenino): ").strip().upper()


try:
    gen_seleccionado = Genero[gen_input] 
except KeyError:
    print("Género no válido, asignando por defecto...")
    gen_seleccionado = Genero.PERUANO
cedula = input("Ingrese el numero de cedula: ").strip()
pais_input = input("Ingrese el pais de nacimiento: ").strip()
persona2 = Persona(nombre, apellido, edad, gen_seleccionado, cedula, pais_input)

print("Datos Persona 1:")
persona1.mostrar_datos()
print("Datos Persona 2:")
persona2.mostrar_datos()