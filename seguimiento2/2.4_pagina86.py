'''2.4 pag 86Se requiere un programa que modele varias figuras geométricas: el círculo,
el rectángulo, el cuadrado y el triángulo rectángulo.
u El círculo tiene como atributo su radio en centímetros.
u El rectángulo, su base y altura en centímetros.
u El cuadrado, la longitud de sus lados en centímetros.
u El triángulo, su base y altura en centímetros.
Se requieren métodos para determinar el área y el perímetro de cada
figura geométrica. Además, para el triángulo rectángulo se requiere:
u Un método que calcule la hipotenusa del rectángulo.
u Un método para determinar qué tipo de triángulo es:
Equilátero: todos sus lados son iguales.
Isósceles: tiene dos lados iguales.
Escaleno: todos sus lados son diferentes.
Se debe desarrollar una clase de prueba con un método main para
crear las cuatro figuras y probar los métodos respectivos. Agregar una nueva clase denominada Rombo. Definir los métodos
para calcular el área y el perímetro de esta nueva figura geométrica.
Agregar una nueva clase denominada Trapecio. Definir los métodos para calcular el área y el perímetro de esta nueva figura geométrica.'''
from math import pi,pow,sqrt
class Circulo:
    def __init__(self, radio):
        self.radio = float(radio)
    
    def calc_area(self):
        return pi * pow(self.radio,2)    
    def calc_perimetro(self):
        return 2 * pi * self.radio
    
    def mostrar(self):
        print("Circulo:")
        print("Radio: ", self.radio)
        print("Area: ", self.calc_area())
        print("Perimetro: ", self.calc_perimetro(),"\n")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
    
    def calc_area(self):
        return self.base * self.altura

    def calc_perimetro(self):
        return 2 * (self.base + self.altura)

    def mostrar(self):
        print("Rectangulo:")
        print("Base: ", self.base)
        print("Altura: ", self.altura)
        print("Area: ", self.calc_area())
        print("Perimetro: ", self.calc_perimetro(),"\n")

class Cuadrado:
    def __init__(self, lado):
        self.lado = float(lado)
    
    def calc_area(self):
        return pow(self.lado,2)

    def calc_perimetro(self):
        return 4 * self.lado

    def mostrar(self):
        print("Cuadrado:")
        print("Lado: ", self.lado)
        print("Area: ", self.calc_area())
        print("Perimetro: ", self.calc_perimetro(),"\n")

class Triangulorectangulo:
    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)
    
    def calc_hipotenusa(self):
        return sqrt(pow(self.base,2) + pow(self.altura,2))
    
    def calc_area(self):
        return (self.base * self.altura) / 2
    
    def calc_perimetro(self):
        return self.base + self.altura + self.calc_hipotenusa()
    
    def mostrar(self):
        print("Triangulo:")
        print("Base: ", self.base)
        print("Altura: ", self.altura)
        print("Area: ", self.calc_area())
        print("Perimetro: ", self.calc_perimetro())
        print(self.determinarTipoTriángulo(),"\n")
    def determinarTipoTriángulo(self):
        if ((self.base == self.altura) and (self.base == self.calc_hipotenusa()) and (self.altura == self.calc_hipotenusa())):
            return "Es un triángulo equilátero"
        elif ((self.base != self.altura) and (self.base != self.calc_hipotenusa()) and (self.altura != self.calc_hipotenusa())):
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isósceles"

class Rombo:
    def __init__(self, diagonal_mayor, diagonal_menor):
        self.diagonal_mayor = float(diagonal_mayor)
        self.diagonal_menor = float(diagonal_menor)
    
    def calc_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2
    
    def calc_perimetro(self):
        return 2 * self.diagonal_mayor + 2 * self.diagonal_menor
    
    def mostrar(self):
        print("Rombo:")
        print("Diagonal mayor: ", self.diagonal_mayor)
        print("Diagonal menor: ", self.diagonal_menor)
        print("Area: ", self.calc_area())
        print("Perimetro: ", self.calc_perimetro(),"\n")

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = float(base_mayor)
        self.base_menor = float(base_menor)
        self.altura = float(altura)
    
    def calc_area(self):
        return (self.base_mayor + self.base_menor) * self.altura / 2
    
    def calc_perimetro(self):
        return self.base_mayor + self.base_menor + self.altura + self.altura
    
    def mostrar(self):
        print("Trapecio:")
        print("Base mayor: ", self.base_mayor)
        print("Base menor: ", self.base_menor)
        print("Altura: ", self.altura)
        print("Area: ", self.calc_area())
        print("Perimetro: ", self.calc_perimetro(),"\n")

#por si acaso esto solo esta quemando codigo para probar
Circulo_figura1 = Circulo(2)
Rectangulo_figura2 = Rectangulo(1,2)
Cuadrado_figura3 = Cuadrado(3)
Triangulorectangulo_figura4 = Triangulorectangulo(3,5)
#estos son los propuestos
Rombo_figura5 = Rombo(3,5)
Rombo_figura5.mostrar()
Trapecio_figura6 = Trapecio(3,5,7)
Trapecio_figura6.mostrar()

Circulo_figura1.mostrar()
Rectangulo_figura2.mostrar()
Cuadrado_figura3.mostrar()
Triangulorectangulo_figura4.mostrar()
