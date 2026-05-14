'''Se requiere un programa que modele el concepto de un automóvil. Un
automóvil tiene los siguientes atributos:
u Marca: el nombre del fabricante.
u Modelo: año de fabricación.
u Motor: volumen en litros del cilindraje del motor de un automóvil.
u Tipo de combustible: valor enumerado con los posibles valores de
gasolina, bioetanol, diésel, biodiésel, gas natural.
u Tipo de automóvil: valor enumerado con los posibles valores de
carro de ciudad, subcompacto, compacto, familiar, ejecutivo, SUV.
u Número de puertas: cantidad de puertas.
u Cantidad de asientos: número de asientos disponibles que tiene el
vehículo.
u Velocidad máxima: velocidad máxima sostenida por el vehículo
en km/h.
u Color: valor enumerado con los posibles valores de blanco, negro,
rojo, naranja, amarillo, verde, azul, violeta.
u Velocidad actual: velocidad del vehículo en un momento dado.
Clases y objetos 75
La clase debe incluir los siguientes métodos:
u Un constructor para la clase Automóvil donde se le pasen como
parámetros los valores de sus atributos.
u Métodos get y set para la clase Automóvil.
u Métodos para acelerar una cierta velocidad, desacelerar y frenar
(colocar la velocidad actual en cero). Es importante tener en cuenta que no se debe acelerar más allá de la velocidad máxima permitida para el automóvil. De igual manera, tampoco es posible
desacelerar a una velocidad negativa. Si se cumplen estos casos, se
debe mostrar por pantalla los mensajes correspondientes.
u Un método para calcular el tiempo estimado de llegada, utilizando
como parámetro la distancia a recorrer en kilómetros. El tiempo
estimado se calcula como el cociente entre la distancia a recorrer y
la velocidad actual.
u Un método para mostrar los valores de los atributos de un Automóvil en pantalla.
u Un método main donde se deben crear un automóvil, colocar su
velocidad actual en 100 km/h, aumentar su velocidad en 20 km/h,
luego decrementar su velocidad en 50 km/h, y después frenar. Con
cada cambio de velocidad, se debe mostrar en pantalla la velocidad
actual.'''
from enum import Enum
class enumcombustible(Enum):
    GASOLINA = "gasolina"
    BIOETANOL = "bioetanol"
    DIESEL = "diésel"
    BIODIÉSEL = "biodiésel"
    GAS_NATURAL = "gas natural"

class enumtipo_automovil(Enum):
    CARRO_DE_CIUDAD = "carro de ciudad"
    SUBCOMPACTO = "subcompacto"
    COMPACTO = "compacto"
    FAMILIAR = "familiar"
    EJECUTIVO = "ejecutivo"
    SUV = "SUV"

class enumcolor(Enum):
    BLANCO = "blanco"
    NEGRO = "negro"
    ROJO = "rojo"
    NARANJA = "naranja"
    AMARILLO = "amarillo"
    VERDE = "verde"
    AZUL = "azul"
    VIOLETA = "violeta"

class automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, numero_puertas, cantidad_asientos, velocidad_maxima, color, velocidad_actual, es_automatico):
        self.marca = str(marca).lower()
        self.modelo = int(modelo)
        self.motor = float(motor)
        self.tipo_combustible_dato = tipo_combustible
        self.tipo_automovil_dato = tipo_automovil
        self.numero_puertas = int(numero_puertas)
        self.cantidad_asientos = int(cantidad_asientos)
        self.velocidad_maxima = float(velocidad_maxima)
        self.color_dato = color
        self.velocidad_actual_dato = float(velocidad_actual)
        self.es_automatico_dato = bool(es_automatico)
        self.multas_dato = 0

    # # marca (Innecesario: no tiene validacion util)
    # @property
    # def marca(self):
    #     return self.marca_dato
    # @marca.setter
    # def marca(self, marca):
    #     self.marca_dato = str(marca).lower()

    # # modelo (Innecesario)
    # @property
    # def modelo(self):
    #     return self.modelo_dato
    # @modelo.setter
    # def modelo(self, modelo):
    #     self.modelo_dato = int(modelo)

    # # motor (Innecesario)
    # @property
    # def motor(self):
    #     return self.motor_dato
    # @motor.setter
    # def motor(self, motor):
    #     self.motor_dato = float(motor)

    # tipo_combustible (UTIL: Valida que sea un Enum correcto)
    @property
    def tipo_combustible(self):
        return self.tipo_combustible_dato
    @tipo_combustible.setter
    def tipo_combustible(self, tipo_combustible):
        if isinstance(tipo_combustible, enumcombustible):
            self.tipo_combustible_dato = tipo_combustible
        else:
            raise ValueError(f"{tipo_combustible} El tipo de combustible no es valido")

    # tipo_automovil (UTIL: Valida Enum)
    @property
    def tipo_automovil(self):
        return self.tipo_automovil_dato
    @tipo_automovil.setter
    def tipo_automovil(self, valor):
        if isinstance(valor, enumtipo_automovil):
            self.tipo_automovil_dato = valor
        else:
            raise ValueError(f"{valor} El tipo de automovil no es valido")

    # # numero_puertas (Innecesario)
    # @property
    # def numero_puertas(self):
    #     return self.numero_puertas_dato
    # @numero_puertas.setter
    # def numero_puertas(self, numero_puertas):
    #     self.numero_puertas_dato = int(numero_puertas)

    # # cantidad_asientos (Innecesario)
    # @property
    # def cantidad_asientos(self):
    #     return self.cantidad_asientos_dato
    # @cantidad_asientos.setter
    # def cantidad_asientos(self, cantidad_asientos):
    #     self.cantidad_asientos_dato = int(cantidad_asientos)

    # # velocidad_maxima (Innecesario)
    # @property
    # def velocidad_maxima(self):
    #     return self.velocidad_maxima_dato
    # @velocidad_maxima.setter
    # def velocidad_maxima(self, velocidad_maxima):
    #     self.velocidad_maxima_dato = float(velocidad_maxima)

    # color (UTIL: Valida Enum)
    @property
    def color(self):
        return self.color_dato
    @color.setter
    def color(self, valor):
        if isinstance(valor, enumcolor):
            self.color_dato = valor
        else:
            raise ValueError(f"{valor} El color no es valido")

    # velocidad_actual (MUY UTIL: Protege fisicamente al objeto)
    @property
    def velocidad_actual(self):
        return self.velocidad_actual_dato
    @velocidad_actual.setter
    def velocidad_actual(self, valor):
        valor_float = float(valor)
        # Nota: ahora usa self.velocidad_maxima sin _dato, porque la volvimos variable publica
        if 0 <= valor_float <= self.velocidad_maxima:
            self.velocidad_actual_dato = valor_float
        else:
            raise ValueError(f"Velocidad fuera de rango maximo o minimo(0 - {self.velocidad_maxima}).")

    # es_automatico
    @property
    def es_automatico(self):
        return self.es_automatico_dato
    @es_automatico.setter
    def es_automatico(self, es_automatico):
        self.es_automatico_dato = bool(es_automatico)

    # multas
    @property
    def multas(self):
        return self.multas_dato
    @multas.setter
    def multas(self, valor):
        self.multas_dato = int(valor)

    # --------------hasta aqui los get self(espero haberlo hecho bien)
    def acelerar(self, aumento_velocidad):
        if (self.velocidad_actual + aumento_velocidad) > self.velocidad_maxima:
            self.multas += 1
            print(f"No se puede acelerar mas alla de la velocidad maxima permitida. Multa generada. Multas actuales: {self.multas}")
        else:
            self.velocidad_actual += aumento_velocidad
            print(f"Velocidad actual despues de acelerar {aumento_velocidad} km/h: {self.velocidad_actual} km/h")

    def desacelerar(self, disminucion_velocidad):
        self.velocidad_actual -= disminucion_velocidad
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
            print(f"No se puede desacelerar a una velocidad negativa.")
        else:
            print(f"Velocidad actual despues de desacelerar {disminucion_velocidad} km/h: {self.velocidad_actual} km/h")

    def frenar(self):
        self.velocidad_actual = 0
        print(f"Frenando...")

    def tiempo_estimado_llegada(self, distancia_recorrer):
        if self.velocidad_actual == 0:
            print("El auto esta detenido. No se puede calcular el tiempo estimado.")
            return 0
        return distancia_recorrer / self.velocidad_actual

    def tiene_multas(self):
        return self.multas > 0

    def total_multas(self):
        return self.multas

    def mostrar(self):
        print(f"Marca: {self.marca.capitalize()}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor}")
        print(f"Tipo de combustible: {self.tipo_combustible.value}")
        print(f"Tipo de automovil: {self.tipo_automovil.value}")
        print(f"Numero de puertas: {self.numero_puertas}")
        print(f"Cantidad de asientos: {self.cantidad_asientos}")
        print(f"Velocidad maxima en km/h: {self.velocidad_maxima}")
        print(f"Color: {self.color.value}")
        print(f"Velocidad actual en km/h: {self.velocidad_actual}")
        print(f"Es automatico: {self.es_automatico}")
        print(f"Multas totales: {self.multas} \n")

auto1 = automovil("Toyota", 2022, 2.0, enumcombustible.GASOLINA, enumtipo_automovil.COMPACTO, 4, 5, 200, enumcolor.BLANCO, 100, False)
auto1.mostrar()
auto1.acelerar(20)
auto1.acelerar(100) # Intento de superar la velocidad maxima (120 + 100 = 220) -> Multa
auto1.desacelerar(50)
auto1.frenar()
print(f"Tiene multas: {auto1.tiene_multas()}")
print(f"Total multas a pagar: {auto1.total_multas()}")
auto1.tiempo_estimado_llegada(100)

print("\n--- Creacion de un nuevo automovil (autoinput) ---")
marca_in = input("Ingrese la marca: ")
modelo_in = int(input("Ingrese el modelo (año): "))
motor_in = float(input("Ingrese el cilindraje del motor: "))

print("Opciones de combustible:", [e.value for e in enumcombustible])
combustible_in = enumcombustible(input("Ingrese el tipo de combustible: ").lower())

print("Opciones de tipo de automovil:", [e.value for e in enumtipo_automovil])
tipo_auto_in = enumtipo_automovil(input("Ingrese el tipo de automovil: ").lower())

puertas_in = int(input("Ingrese el numero de puertas: "))
asientos_in = int(input("Ingrese la cantidad de asientos: "))
vel_max_in = float(input("Ingrese la velocidad maxima (km/h): "))

print("Opciones de color:", [e.value for e in enumcolor])
color_in = enumcolor(input("Ingrese el color: ").lower())

vel_actual_in = float(input("Ingrese la velocidad actual (km/h): "))
es_auto_in = input("¿Es automatico? (si/no): ").lower() == "si"

autoinput = automovil(
    marca=marca_in,
    modelo=modelo_in,
    motor=motor_in,
    tipo_combustible=combustible_in,
    tipo_automovil=tipo_auto_in,
    numero_puertas=puertas_in,
    cantidad_asientos=asientos_in,
    velocidad_maxima=vel_max_in,
    color=color_in,
    velocidad_actual=vel_actual_in,
    es_automatico=es_auto_in
)

print("\n--- Datos del auto creado ---")
autoinput.mostrar()
