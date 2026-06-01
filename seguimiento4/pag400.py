'''¿Cuál es el resultado de la 
ejecución del método main del siguiente programa? Determinar qué se imprime en pantalla.'''
class ExcepcionDivision:
    @staticmethod
    def main():
        # --- Primer bloque try ---
        try:
            print("Ingresando al primer try: ")
            dividendo = int(10000)
            divisor = int(0)
            cociente = dividendo / divisor  # Se lanza una excepción (ZeroDivisionError)
            print("Después de la división")  # Esta instrucción nunca será ejecutada
        except ZeroDivisionError:  # Se captura la excepción específica
            print("División por cero")  # Se imprime en pantalla este mensaje
        except ValueError:
            print("Formato de número incorrecto")
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepción
            print("Ingresando al primer finally")

        # --- Segundo bloque try ---
        try:
            print()
            objeto = None
            objeto.__str__()  # Se lanza una excepción (AttributeError en Python)
            # Esta instrucción nunca se ejecuta porque se lanzó una excepción
            print("Imprimiendo objeto")
        except ZeroDivisionError:  # La excepción lanzada no es de este tipo
            print("División por cero")
        except Exception:  # Se captura la excepción general
            print("Ocurrió una excepción")  # Se imprime en pantalla este mensaje
        finally:
            # La sentencia finally siempre se ejecuta, ocurra o no una excepción
            print("Ingresando al segundo finally")

'''
Determinar qué se imprime en pantalla.
Selecciona el caracter numero 15 de una string y si no tiene 15 caracteres, se lanza una excepción.
'''
class ExcepcionFueraLimite:
    @staticmethod
    def main():
        try:
            texto = input("ingrese un texto de 15 caracteres: ")
            caracter = texto[14]
            print(caracter)
        except IndexError:
            print("Indice de string por fuera del límite")
            
'''
Determinar qué se imprime en pantalla.
El usuario ingresa un número entero, si el formato del número es incorrecto, se lanza una excepción.
'''
class ExcepcionFormatoNumero:
    @staticmethod
    def main():
        try:
            numero = int(input("Ingrese un número entero"))
            print(numero)
        except ValueError:
            print("Excepción de formato de número")
        finally:
            print("Ingresando al finally")

ExcepcionDivision.main()

ExcepcionFueraLimite.main()

ExcepcionFormatoNumero.main()

#. \  /
#.  \/
