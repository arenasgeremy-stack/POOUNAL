class Profesor:
    def imprimir(self):
        print("Es un profesor.")
class ProfesorTitular(Profesor):
    def __init__(self):
        super().__init__()
        self.años = 0
    def imprimir(self):
        print("Es un profesor titular.")
    def imprimir_años(self):
        print(f"Años = {self.años}")
if __name__ == "__main__":
    profesor1 = ProfesorTitular()
    profesor1.imprimir_años()

#ejercicio propuesto
class Profesor:
    def imprimir(self):
        print("Es un profesor.")
class ProfesorTitular(Profesor):
    def __init__(self):
        super().__init__()
        self.años = 0
    def imprimir(self):
        print("Es un profesor titular.")
    def imprimir_años(self):
        print(f"Años = {self.años}")

class Prueba:
    def __init__(self):
        self.profesores = []
if __name__ == "__main__":
    prueba = Prueba()
    profesor1 = Profesor()
    profesor2 = ProfesorTitular()
    prueba.profesores.append(profesor1)
    prueba.profesores.append(profesor2)

    for p in prueba.profesores:
        p.imprimir()

'''El programa sí compila en Java y se ejecuta con éxito en ambos lenguajes, 
imprimiendo lo siguiente en la consola:
Es un profesor.
Es un profesor titular.
'''