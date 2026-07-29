# Clase Padre
class Profesor:
    def imprimir(self):
        print("Soy un profesor")
class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular")
def main():
    profesor1 = ProfesorTitular()
    profesor2 = profesor1
    profesor2.imprimir()
if __name__ == "__main__":
    main()

'''Se ejecuta exitosamente sin errores de compilación ni de ejecución. 
Imprime en pantalla el resultado del método imprimir() de la clase ProfesorTitular.
(Si en el ejercicio anterior del libro el método imprimir() de 
ProfesorTitular imprimía, por ejemplo, "Es un profesor titular", 
ese será exactamente el texto que se mostrará en la consola).'''