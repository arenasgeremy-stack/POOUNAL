'''Se tiene un archivo de texto denominado prueba.txt en una cierta localización en un sistema de archivos.
Se requiere desarrollar un programa
que lea dicho archivo de texto utilizando un flujo de bytes que muestre los
contenidos del archivo en pantalla.'''
class LectorArchivo:
    def __init__(self, ruta: str):
        self.ruta = ruta

    def mostrar_contenido_en_pantalla(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                print(contenido)
        except FileNotFoundError:
            print(f"Error: El archivo en '{self.ruta}' no fue encontrado.")
        except IOError as e:
            print(f"Error al leer el archivo: {e}")

'''Ejercicios propuestos
Escribir un programa que lea por teclado el nombre de un archivo
de texto y muestre su contenido en pantalla.
Desarrollar un método que lea el contenido del archivo y lo muestre en pantalla con 
todos los caracteres en minúsculas convertidos
a mayúsculas.'''

class LectorMayus:
    def __init__(self, ruta: str):
        self.ruta = ruta

    def mostrar_contenido_mayus(self):
        try:
            with open(self.ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                print(contenido.upper())
        except FileNotFoundError:
            print(f"Error: El archivo en '{self.ruta}' no fue encontrado.")
        except IOError as e:
            print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
    lector = LectorArchivo(input("Ingrese el archivo de texto a leer: "))
    lector.mostrar_contenido_en_pantalla()
    lectorMm = LectorMayus(input("Ingrese el archivo para pasar a mayusculas: "))
    lectorMm.mostrar_contenido_mayus()


