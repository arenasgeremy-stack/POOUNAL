'''Se requiere definir una clase denominada CálculosNúmericos que realice
las siguientes operaciones: Calcular el logaritmo neperiano recibiendo un valor double como
parámetro. Este método debe ser estático. Si el valor no es positivo
se genera una excepción aritmética. Calcular la raíz cuadrada recibiendo un valor double como parámetro. Este método debe ser estático. 
Si el valor no es positivo se
genera una excepci  ón aritmética.
Se debe crear un método main que utilice dichos métodos ingresando
un valor por teclado.'''

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ValueError("El valor debe ser positivo para calcular el logaritmo neperiano.")#jajaja, ese nombre
        import math
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ValueError("El valor no puede ser negativo para calcular la raíz cuadrada.")
        import math
        return math.sqrt(valor)
try:
    logaritmo_neperiano = CalculosNumericos.calcular_logaritmo_neperiano(float(input("logaritmo neperiano: ")))
    print(f"Logaritmo neperiano: {logaritmo_neperiano}")
except ValueError as errores:
    print(f"Error: {errores}")
try:
    raiz_cuadrada = CalculosNumericos.calcular_raiz_cuadrada(float(input("raíz cuadrada: ")))
    print(f"Raíz cuadrada: {raiz_cuadrada}")
except ValueError as errores:
    print(f"Error: {errores}")
'''Ejercicios propuestos
u Agregar al ejercicio anterior los métodos que realicen las siguientes
operaciones matemáticas:
○ Calcular la pendiente de una recta.
○ Calcular el punto medio de una recta.
○ Calcular las raíces de una ecuación cuadrática.
○ Convertir un número en base 10 a un número en base b.
Y agregar los manejadores de excepciones correspondientes.'''
class CalculosMatematicos:
    @staticmethod
    def calcular_pendiente(x1, y1, x2, y2):
        if x1 == x2:
            raise ValueError("No es funcion porque los puntos tienen la misma coordenada x.")
        else:
            return (y2 - y1) / (x2 - x1)

    @staticmethod
    def calcular_punto_medio(x1, y1, x2, y2):
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    @staticmethod
    def calcular_raices_ecuacion_cuadratica(a, b, c):
        import math
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            raise ValueError("La ecuación no tiene raíces reales.")
        raiz_discriminante = math.sqrt(discriminante)
        raiz1 = (-b + raiz_discriminante) / (2*a)
        raiz2 = (-b - raiz_discriminante) / (2*a)
        return raiz1, raiz2

    @staticmethod
    def convertir_base10_a_base_b(numero, base):
        if base < 2:
            raise ValueError("La base debe ser al menos 2.")
        if numero < 0:
            raise ValueError("El número debe ser no negativo.")
        digitos = []
        while numero > 0:
            digitos.append(str(numero % base))
            numero //= base
        return ''.join(reversed(digitos)) or '0'

x1 = int(input("Ingrese x1 "))
y1 = int(input("Ingrese y1 "))
x2 = int(input("Ingrese x2 "))
y2 = int(input("Ingrese y2 "))
try:
    pendiente = CalculosMatematicos.calcular_pendiente(x1, y1, x2, y2)
    print(f"Pendiente: {pendiente}")
except ValueError as errores:
    print(f"Error: {errores}")
try:
    punto_medio = CalculosMatematicos.calcular_punto_medio(x1, y1, x2, y2)
    print(f"Punto medio: {punto_medio}")
except ValueError as errores:
    print(f"Error: {errores}")
try:
    raices = CalculosMatematicos.calcular_raices_ecuacion_cuadratica(float(input("Ingrese coeficiente a: ")), float(input("Ingrese coeficiente b: ")), float(input("Ingrese coeficiente c: ")))
    print(f"Raíces de la ecuación cuadrática: {raices}")
except ValueError as errores:
    print(f"Error: {errores}")
try:
    numero_base2 = CalculosMatematicos.convertir_base10_a_base_b(10, int(input("Ingrese la base a la que desea convertir el número 10: ")))
    print(f"Número 10 en base 2: {numero_base2}")
except ValueError as errores:
    print(f"Error: {errores}")
