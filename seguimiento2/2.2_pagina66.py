"""Ejercicio 2.2. Definición de atributos de una clase con tipos
primitivos de datos
Se requiere un programa que modele el concepto de un planeta del sistema
solar. Un planeta tiene los siguientes atributos:
u Un nombre de tipo Sring con valor inicial de null.
u Cantidad de satélites de tipo int con valor inicial de cero.
u Masa en kilogramos de tipo double con valor inicial de cero.
68 Ejercicios de programación orientada a objetos con Java y UML
u Volumen en kilómetros cúbicos de tipo double con valor inicial de
cero.
u Diámetro en kilómetros de tipo int con valor inicial de cero.
u Distancia media al Sol en millones de kilómetros, de tipo int con
valor inicial de cero.
u Tipo de planeta de acuerdo con su tamaño, de tipo enumerado con
los siguientes valores posibles: GASEOSO, TERRESTRE y ENANO.
u Observable a simple vista, de tipo booleano con valor inicial false.
La clase debe incluir los siguientes métodos:
u La clase debe tener un constructor que inicialice los valores de sus
respectivos atributos.
u Definir un método que imprima en pantalla los valores de los atributos de un planeta.
u Calcular la densidad un planeta, como el cociente entre su masa y
su volumen.
u Determinar si un planeta del sistema solar se considera exterior.
Un planeta exterior está situado más allá del cinturón de asteroides. El cinturón de asteroides se encuentra entre 2.1 y 3.4 UA. Una
unidad astronómica (UA) es la distancia entre la Tierra y el Sol=
149597870 Km.
u En un mmétodo main se deben crear dos planetas y mostrar los valores de sus atributos en pantalla. Adeás, se debe imprimir la
densidad de cada planeta y si el planeta es un planeta exterior del
sistema solar."""
from enum import Enum
class TipoPlaneta(Enum):
    GASEOSO = "gaseoso"
    TERRESTRE = "terrestre"
    ENANO = "enano"
    
class Planeta:
    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_media_sol, tipo, observable_simple_vista, periodo_orbital, periodo_rotacion):
        self.nombre = str(nombre)
        self.cantidad_satelites = int(cantidad_satelites)
        self.masa = float(masa)
        self.volumen = float(volumen)
        self.diametro = int(diametro)
        self.distancia_media_sol = int(distancia_media_sol)
        self.tipo = tipo
        self.observable_simple_vista = bool(observable_simple_vista)
        self.periodo_orbital = float(periodo_orbital)
        self.periodo_rotacion = float(periodo_rotacion)
    
    def calcular_densidad(self):
        return self.masa / self.volumen
    ua = int(149597870)
    def es_planeta_exterior(self):
        if self.distancia_media_sol > (2.1*self.ua):
            return True
        elif self.distancia_media_sol < (3.4*self.ua):
            return False
        else:
            return "en el cinturon de asteroides"
    
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Cantidad de satélites: ", self.cantidad_satelites)
        print("Masa: ", self.masa, " kg")
        print("Volumen: ", self.volumen, " km³")
        print("Diámetro: ", self.diametro, " km")
        print("Distancia media al Sol: ", self.distancia_media_sol, " millones de km")
        print("Tipo: ", self.tipo.value.capitalize())
        print("Observable a simple vista: ", self.observable_simple_vista)
        print("Densidad: ", self.calcular_densidad(),"kg/km³")
        print("Es planeta exterior: ", self.es_planeta_exterior(),)
        print("Periodo orbital: ", self.periodo_orbital, " años")
        print("Periodo de rotacion: ", self.periodo_rotacion, " dias","\n")
#objetos quemados
planeta1 = Planeta("Tierra", 1, 5972000000000000000000000, 1083210000000, 12742, 149600000, TipoPlaneta.TERRESTRE, True, 1, 1)
planeta1.mostrar()
planeta2 = Planeta("Marte", 2, 641700000000000000000000, 163180000000, 6779, 227900000, TipoPlaneta.TERRESTRE, True, 2, 1.026)
planeta2.mostrar()
#objeto ingresado por el usuario
print("--- Ingreso de datos para el Planeta 3 ---")
nombre_p3 = input("Ingrese el nombre del planeta 3: ")
satelites_p3 = int(input("Ingrese la cantidad de satélites: "))
masa_p3 = float(input("Ingrese la masa (en kg): "))
volumen_p3 = float(input("Ingrese el volumen (en km³): "))
diametro_p3 = int(input("Ingrese el diámetro (en km): "))
distancia_p3 = int(input("Ingrese la distancia media al Sol: "))

tipo_p3= str(input("digite el tipo de planeta entre gaseoso, terrestre y enano: ")).lower()
tipo_p3 = TipoPlaneta(tipo_p3)

obs_p3_str = input("¿Es observable a simple vista? (s/n): ")
obs_p3 = obs_p3_str.lower() == 's'

periodo_orbital_p3 = float(input("Ingrese el periodo orbital en años: "))
periodo_rotacion_p3 = float(input("Ingrese el periodo de rotacio en dias: "))

planeta3 = Planeta(nombre_p3, satelites_p3, masa_p3, volumen_p3, diametro_p3, distancia_p3, tipo_p3, obs_p3)
print("\n--- Datos del Planeta 3 ---")
planeta3.mostrar()