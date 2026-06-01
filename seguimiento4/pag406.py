'''Se requiere implementar una clase vendedor que posee los siguientes atributos: nombre (tipo String), 
apellidos (tipo String) y edad (tipo int).
La clase contiene un constructor que inicialice los atributos de la clase. Además, la clase posee los 
siguientes métodos: Imprimir: muestra por pantalla los valores de sus atributos.
Verificar edad: este método recibe como parámetro un valor entero que representa la edad del vendedor. 
Para que un vendedor
pueda desempeñar sus labores se requiere que sea mayor de edad
(mayor de 18 años). Si esta condición no se cumple, se lanza una
excepción de tipo IllegalArgumentException con el mensaje “El vendedor debe ser mayor de 18 años”. 
Además, se evalúa si la edad
se encuentra en el rango de 0 a 120, si no se cumple, se genera
una excepción de tipo IllegalArgumentException con el mensaje “La
edad no puede ser negativa ni mayor a 120”. Si la edad cumple
estos requerimientos se pueden instanciar el objeto vendedor.
Además, se requiere que los datos del vendedor se ingresen por
teclado.
'''

''' EJERCICIOS PROPUESTOS
Escribir un programa con un constructor que lanza una excepción
a un controlador de excepciones. El programa debe intentar crear
un objeto y detectar la excepción que se genera desde el constructor.
Implementar una clase con la tabla ASCII, cada símbolo tiene asociado un valor numérico. La clase tiene dos métodos:
○ int get(String símbolo): dado un símbolo recupera el número
asociado.
○ void set(String símbolo, int número): asocia el número con el
símbolo.
Se deben definir excepciones apropiadas, de tal manera que los métodos funcionen correctamente. Por ejemplo, cuando se requiere recuperar
un símbolo inexistente o que el parámetro pasado sea un valor nulo '''
class Vendedor:
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.verificar_edad()

    def imprimir(self):
        print(f"Nombre: {self.nombre} {self.apellidos}, Edad: {self.edad}")

    def verificar_edad(self):
        if self.edad < 0 or self.edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120")
        if self.edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años")

try:
    vendedorX = Vendedor(input("Ingrese Nombre: "), input("Ingrese apellido: "), int(input("Ingrese edad: ")))
    vendedorX.imprimir()
except ValueError as errores:
    print(f'Error: {errores}')

class ASCIITable:
    def __init__(self):
        self.table = {}

    def set(self, simbolo, numero):
        if simbolo is None or numero is None:
            raise ValueError("El símbolo y el número no pueden ser nulos")
        self.table[simbolo] = numero

    def get(self, simbolo):
        if simbolo not in self.table:
            raise KeyError("Símbolo inexistente")
        return self.table[simbolo]
tabla = ASCIITable()
tabla.set(input("Inserte Caracter: "), int(input("Inserte Valor: ")))
print(tabla.get(input("Inserte Caracter a recuperar: ")))
