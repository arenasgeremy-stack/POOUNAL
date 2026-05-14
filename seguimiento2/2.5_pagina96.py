'''Se requiere un programa que modele una cuenta bancaria que posee los
siguientes atributos:
u Nombres del titular.
u Apellidos del titular.
u Número de la cuenta bancaria.
u Tipo de cuenta: puede ser una cuenta de ahorros o una cuenta
corriente.
u Saldo de la cuenta.
Se debe definir un constructor que inicialice los atributos de la clase.
Cuando se crea una cuenta bancaria, su saldo inicial tiene un valor de cero.
En una determinada cuenta bancaria se puede:
u Imprimir por pantalla los valores de los atributos de una cuenta
bancaria.
u Consultar el saldo de una cuenta bancaria.
u Consignar un determinado valor en la cuenta bancaria, actualizando el saldo correspondiente.
u Retirar un determinado valor de la cuenta bancaria, actualizando
el saldo correspondiente. Es necesario tener en cuenta que no se
puede realizar el retiro si el valor solicitado supera el saldo actual
de la cuenta.Agregar a la clase CuentaBancaria, un atributo que represente el
porcentaje de interés mensual aplicado a la cuenta.
u Agregar un método que calcule un nuevo saldo aplicando la tasa
de interés correspondiente.'''
from enum import Enum

class tipo_cuenta_enum(Enum):
    AHORROS = "ahorros"
    CORRIENTE = "corriente"
class CuentaBancaria:
    def __init__(self, nombres, apellidos, numero_cuenta, tipo_cuenta, saldo, interes):
        self.nombres = str(nombres).strip().lower().capitalize()
        self.apellidos = str(apellidos).strip().lower().capitalize()
        self.numero_cuenta = int(numero_cuenta)
        self.tipo_cuenta = tipo_cuenta
        self.saldo = float(saldo)
        self.interes = float(interes)

    def mostrar(self):
        print("\n Nombres: ", self.nombres)
        print("Apellidos: ", self.apellidos)
        print("Numero de cuenta: ", self.numero_cuenta)
        print("Tipo de cuenta: ", self.tipo_cuenta.value)
        print("Saldo: ", self.saldo)
        print("Interes: ", self.interes, "\n")
    def consultar_saldo(self):
        return self.saldo
    
    def consignar_saldo(self, valor):
        self.saldo += valor
        print(f"Se consignó: +{valor} | Nuevo saldo: {self.saldo}")
        return self.saldo
    
    def retirar_saldo(self, valor):
        if valor > self.saldo:
            print(f"Intento de retiro: {valor} -> Fallido (Saldo insuficiente)")
            return "Saldo insuficiente"
        else:
            self.saldo -= valor
            print(f"Se retiró: -{valor} | Nuevo saldo: {self.saldo}")
            return self.saldo
    
    def calcular_interes(self):
        interes = self.saldo * (self.interes / 100)
        self.saldo -= interes # no se si se refiere a interes como una deduccion o una comision, por ahora lo deje en resta
        print(f"Se restó el interés: -{interes} | Nuevo saldo: {self.saldo}")
        return self.saldo
cuenta1 = CuentaBancaria("Pedro", "Perez", 123456789, tipo_cuenta_enum.AHORROS, 0, 5) # 5 representa un 5% de interés mensual
cuenta1.mostrar()
cuenta1.consignar_saldo(200000)
cuenta1.consignar_saldo(300000)
cuenta1.retirar_saldo(400000)
cuenta1.mostrar()

print("Aplicando intereses mensuales del 5% ")
cuenta1.calcular_interes()

print("\n""Creación de Cuenta 2 (Interactiva)")
nombres_input = input("Ingrese los nombres del titular: ")
apellidos_input = input("Ingrese los apellidos del titular: ")
numero_cuenta_input = input("Ingrese el número de la cuenta: ")

# Validar el tipo de cuenta para que encaje con el Enum
while True:
    tipo_input = input("Ingrese el tipo de cuenta (Ahorros o Corriente): ").strip().lower()
    try:
        tipo_cuenta_input = tipo_cuenta_enum(tipo_input)
        break
    except ValueError:
        print("Error: Tipo de cuenta inválido. Debe ser 'Ahorros' o 'Corriente'.")
'''si el man no se va a equivocar mejor asi, pero es claro que se va a equivocar.
print("Opciones de cuenta:", [e.value for e in tipo_cuenta_enum])
tipo_cuenta_input = tipo_cuenta_enum(input("Ingrese el tipo de cuenta: ").strip().lower())'''

interes_input = input("Ingrese el porcentaje de interés mensual: ")

# El requerimiento indica que el saldo inicial es cero
cuenta2 = CuentaBancaria(nombres_input, apellidos_input, numero_cuenta_input, tipo_cuenta_input, 0, interes_input)
cuenta2.mostrar()

print("\nTransacciones de Cuenta 2")
try:
    valor_consignar = float(input("Ingrese el valor a consignar en la Cuenta 2: "))
    cuenta2.consignar_saldo(valor_consignar)
    
    valor_retirar = float(input("Ingrese el valor a retirar de la Cuenta 2: "))
    cuenta2.retirar_saldo(valor_retirar)
except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para las transacciones.")
print(f"Aplicando intereses mensuales del {interes_input}% ")
cuenta2.calcular_interes()