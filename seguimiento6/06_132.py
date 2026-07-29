class Pedido:

    def calcularPedido(self, *args):

        if len(args) == 4:
            # Caso 1: primerPlato, costoPrimerPlato, bebida, costoBebida
            primerPlato, costoPrimerPlato, bebida, costoBebida = args
            total = costoPrimerPlato + costoBebida
            print(f"El costo de {primerPlato} y {bebida} es = ${total}")

        elif len(args) == 6:
            # Caso 2: primerPlato, costoPrimerPlato, segundoPlato, costoSegundoPlato, bebida, costoBebida
            primerPlato, costoPrimerPlato, segundoPlato, costoSegundoPlato, bebida, costoBebida = args
            total = costoPrimerPlato + costoSegundoPlato + costoBebida
            print(f"El costo de {primerPlato} + {segundoPlato} + {bebida} es = ${total}")

        elif len(args) == 8:
            # Caso 3: primerPlato, costoPrimerPlato, segundoPlato, costoSegundoPlato, postre, costoPostre, bebida, costoBebida
            primerPlato, costoPrimerPlato, segundoPlato, costoSegundoPlato, postre, costoPostre, bebida, costoBebida = args
            total = costoPrimerPlato + costoSegundoPlato + costoBebida + costoPostre
            print(f"El costo de {primerPlato} + {segundoPlato} + {bebida} + {postre} es = ${total}")
        
        else:
            raise TypeError("Número de argumentos no válido para calcularPedido")


if __name__ == "__main__":
    # Método main que crea tres diferentes tipos de pedidos en el restaurante
    pedido1 = Pedido()
    pedido1.calcularPedido("Sancocho", 5000, "Gaseosa", 2000)

    pedido2 = Pedido()
    pedido2.calcularPedido("Crema de verduras", 5000, "Churrasco", 6000, "Gaseosa", 2000)

    pedido3 = Pedido()
    pedido3.calcularPedido("Crema de espinacas", 5000, "Salmón", 10000, "Tiramisú", 5000, "Gaseosa", 2000)

class Suma:
    """
    Clase denominada Suma, la cual tiene varios métodos sumar sobrecargados.
    """

    def sumar(self, *args):
        """
        Método sumar sobrecargado utilizando tipo y número de argumentos
        recibidos en Python.
        """
        # Validar la cantidad de parámetros
        if len(args) == 2:
            a, b = args
            # Comprobar si ambos son enteros
            if isinstance(a, int) and not isinstance(a, bool) and isinstance(b, int) and not isinstance(b, bool):
                print(f"Llamando a sumar(int, int): {a} + {b}")
                return a + b
            # Comprobar si son floats
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
                print(f"Llamando a sumar(float, float): {a} + {b}")
                return float(a + b)

        elif len(args) == 3:
            a, b, c = args
            # Comprobar si los tres son enteros
            if isinstance(a, int) and not isinstance(a, bool) and isinstance(b, int) and not isinstance(b, bool) and isinstance(c, int) and not isinstance(c, bool):
                print(f"Llamando a sumar(int, int, int): {a} + {b} + {c}")
                return a + b + c
            # Comprobar si son floats
            elif isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
                print(f"Llamando a sumar(float, float, float): {a} + {b} + {c}")
                return float(a + b + c)

        raise TypeError("Parámetros no válidos para el método sumar (deben ser 2 o 3 enteros o números reales)")


if __name__ == "__main__":
    calc = Suma()
    
    # 1. Un método sumar que obtiene la suma de dos valores enteros
    res1 = calc.sumar(5, 10)
    print(f"Resultado: {res1}\n")

    # 2. Un método sumar que obtiene la suma de tres valores enteros
    res2 = calc.sumar(5, 10, 15)
    print(f"Resultado: {res2}\n")

    # 3. Un método sumar que obtiene la suma de dos valores double/float
    res3 = calc.sumar(5.5, 10.5)
    print(f"Resultado: {res3}\n")

    # 4. Un método sumar que obtiene la suma de tres valores double/float
    res4 = calc.sumar(5.5, 10.5, 20.2)
    print(f"Resultado: {res4}\n")
