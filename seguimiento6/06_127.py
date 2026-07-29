'''Realizar un programa en Java que permita realizar las siguientes 
conversiones de unidades de longitud:
Metros a centímetros.
Metros a milímetros.
Metros a pulgadas.
Metros a pies.
Metros a yardas.
'''
class distancia_metros:
    def __init__(self, metros):
        self.metros = metros
    def metros_centimetros(self):
        return self.metros * 100
    def metros_milimetros(self):
        return self.metros * 1000
    def metros_pulgadas(self):
        return self.metros * 39.3701
    def metros_pies(self):
        return self.metros * 3.28084
    def metros_yardas(self):
        return self.metros * 1.09361


metros = float(input("Ingrese los metros: "))
distancia_metros= distancia_metros(metros)
print("Los metros en centimetros son: ", distancia_metros.metros_centimetros())
print("Los metros en milimetros son: ", distancia_metros.metros_milimetros())
print("Los metros en pulgadas son: ", distancia_metros.metros_pulgadas())
print("Los metros en pies son: ", distancia_metros.metros_pies())
print("Los metros en yardas son: ", distancia_metros.metros_yardas())
#Me parece raro el codigo pero basicamente esto es lo que tenia el texto guia
'''Hacer clases similares para realizar conversiones de unidades de
medición como:Medidas de superficie o área: 
convertir áreas (1 área= 100 m2)
a: hectáreas (1 hectárea= 10000 m2); 
kilómetros cuadrados(1 kilómetro cuadrado= 1000000 m2); 
fanegas (1 fanega =6460 m2) 
y acres (1 acre= 4046.85 m2).
Medidas de volumen: convertir litros a: galones (1 galón=4,41
litros); pintas (1 pinta= 0.46 litros); barriles (1 barril= 158.99 litros), 
metros cúbicos (1 m3 = 1000 litros) y hectolitros (1 hectolitro= 100 litros).'''
#si es hhacer lo mismo entonces literalmente seria que ingrese un 
#area un volumen y el devuelva los resultados en las otras unidades
class area_metros: 
    def __init__(self, area):
        self.area = area
    def area_hectareas(self):
        return self.area / 10000
    def area_kilometros_cuadrados(self):
        return self.area / 1000000
    def area_fanegas(self):
        return self.area / 6460
    def area_acres(self):
        return self.area / 4046.85

area = float(input("Ingrese el area en metros cuadrados: "))
area_metros = area_metros(area)
print("El area en hectareas es: ", area_metros.area_hectareas())
print("El area en kilometros cuadrados es: ", area_metros.area_kilometros_cuadrados())
print("El area en fanegas es: ", area_metros.area_fanegas())
print("El area en acres es: ", area_metros.area_acres())

class volumen_litros:
    def __init__(self, litros):
        self.litros = litros
    def litros_galones(self):
        return self.litros / 4.41
    def litros_pintas(self):
        return self.litros / 0.46
    def litros_barriles(self):
        return self.litros / 158.99
    def litros_metros_cubicos(self):
        return self.litros / 1000
    def litros_hectolitros(self):
        return self.litros / 100

litros = float(input("Ingrese los litros: "))
volumen_litros = volumen_litros(litros)
print("Los litros en galones son: ", volumen_litros.litros_galones())
print("Los litros en pintas son: ", volumen_litros.litros_pintas())
print("Los litros en barriles son: ", volumen_litros.litros_barriles())
print("Los litros en metros cubicos son: ", volumen_litros.litros_metros_cubicos())
print("Los litros en hectolitros son: ", volumen_litros.litros_hectolitros())