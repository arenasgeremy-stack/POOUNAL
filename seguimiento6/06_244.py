'''Se tiene una jerarquía taxonómica con los siguientes animales:
u Animal es la clase raíz con los atributos: sonidos, alimentos, hábitat y nombre científico (todos de tipo String). Esta clase tiene los
siguientes métodos abstractos:
○ public abstract String getNombreCientífico()
○ public abstract String getSonido()
○ public abstract String getAlimentos()
○ public abstract String getHábitat()
u Los cánidos y los felinos son subclases de Animal.
u Los perros son cánidos, su sonido es el ladrido, su alimentación es
carnívora, su hábitat es doméstico y su nombre científico es Canis
lupus familiaris.
Herencia y polimorfismo 245
u Los lobos son cánidos, su sonido es el aullido, su alimentación es
carnívora, su hábitat es el bosque y su nombre científico es Canis
lupus.
u Los leones son felinos, su sonido es el rugido, su alimentación es
carnívora, su hábitat es la pradera y su nombre científico es Panthera leo.
u Los gatos son felinos, su sonido es el maullido, su alimentación
son los ratones, su hábitat es doméstico y su nombre científico es
Felis silvestris catus.
Además, se requiere en una clase de prueba para desarrollar un método main que genere un array de animales y la pantalla debe mostrar los
valores de sus atributos.'''


from abc import ABC, abstractmethod

# Clase abstracta Animal
class Animal(ABC):
    @abstractmethod
    def get_nombre_cientifico(self):
        pass
    
    @abstractmethod
    def get_sonido(self):
        pass
    
    @abstractmethod
    def get_alimentos(self):
        pass
    
    @abstractmethod
    def get_habitat(self):
        pass

# Clase Cánidos
class Canidos(Animal):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat):
        self._nombre_cientifico = nombre_cientifico
        self._sonido = sonido
        self._alimentos = alimentos
        self._habitat = habitat
    
    def get_nombre_cientifico(self):
        return self._nombre_cientifico
    
    def get_sonido(self):
        return self._sonido
    
    def get_alimentos(self):
        return self._alimentos
    
    def get_habitat(self):
        return self._habitat

# Clase Felinos
class Felinos(Animal):
    def __init__(self, nombre_cientifico, sonido, alimentos, habitat):
        self._nombre_cientifico = nombre_cientifico
        self._sonido = sonido
        self._alimentos = alimentos
        self._habitat = habitat
    
    def get_nombre_cientifico(self):
        return self._nombre_cientifico
    
    def get_sonido(self):
        return self._sonido
    
    def get_alimentos(self):
        return self._alimentos
    
    def get_habitat(self):
        return self._habitat

# Clase Perro
class Perro(Canidos):
    def __init__(self):
        super().__init__("Canis lupus familiaris", "Ladrido", "Carnívora", "Doméstico")

# Clase Lobo
class Lobo(Canidos):
    def __init__(self):
        super().__init__("Canis lupus", "Aullido", "Carnívora", "Bosque")

# Clase León
class Leon(Felinos):
    def __init__(self):
        super().__init__("Panthera leo", "Rugido", "Carnívora", "Pradera")

# Clase Gato
class Gato(Felinos):
    def __init__(self):
        super().__init__("Felis silvestris catus", "Maullido", "Ratones", "Doméstico")

# Clase de prueba
class Prueba:
    @staticmethod
    def main():
        # Crear array de animales
        animales = [
            Perro(),
            Lobo(),
            Leon(),
            Gato()
        ]
        
        # Mostrar atributos de cada animal
        for animal in animales:
            print(f"Nombre científico: {animal.get_nombre_cientifico()}")
            print(f"Sonido: {animal.get_sonido()}")
            print(f"Alimentos: {animal.get_alimentos()}")
            print(f"Hábitat: {animal.get_habitat()}")
            print("-" * 20)

'''Definir una clase abstracta denominada Numérica que tenga los
siguientes métodos abstractos:
public String toString(): convierte el número a String.
public boolean equals (Object ob): compara el objeto con el parámetro.
public Numérica sumar(Numérica número): retorna la suma de
los dos números.
public Numérica restar(Numérica número): retorna la resta de
los dos números.
public Numérica multiplicar(Numérica número): retorna la
multiplicación de los dos números.
public Numérica dividir(Numérica número): retorna la división de los dos números.
Definir una clase Fracción que representa un número fraccionario,
el cual hereda de la clase Numérica y tiene dos atributos (tipo int)
que representan el numerador y denominador de la fracción. Se
deben implementar todos los métodos heredados.
Crear una clase de prueba que utilice los métodos implementados.'''
# Ejecutar el programa
if __name__ == "__main__":
    print("=== PRUEBA DE ANIMALES ===")
    Prueba.main()     

# Ejercicios propuestos
# Definir una clase abstracta denominada Numérica
class Numerica(ABC):
    @abstractmethod
    def to_string(self) -> str:
        """Convierte el número a String."""
        pass
    
    @abstractmethod
    def equals(self, ob) -> bool:
        """Compara el objeto con el parámetro."""
        pass
    
    @abstractmethod
    def sumar(self, numero):
        """Retorna la suma de los dos números."""
        pass
    
    @abstractmethod
    def restar(self, numero):
        """Retorna la resta de los dos números."""
        pass
    
    @abstractmethod
    def multiplicar(self, numero):
        """Retorna la multiplicación de los dos números."""
        pass
    
    @abstractmethod
    def dividir(self, numero):
        """Retorna la división de los dos números."""
        pass

# Definir una clase Fracción que representa un número fraccionario
class Fraccion(Numerica):
    def __init__(self, numerador: int, denominador: int):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self._simplificar()
        
    def _simplificar(self):
        import math
        divisor = math.gcd(self.numerador, self.denominador)
        self.numerador //= divisor
        self.denominador //= divisor
        # Mantener el signo en el numerador
        if self.denominador < 0:
            self.numerador = -self.numerador
            self.denominador = -self.denominador

    def to_string(self) -> str:
        if self.denominador == 1:
            return str(self.numerador)
        return f"{self.numerador}/{self.denominador}"
        
    def __str__(self) -> str:
        return self.to_string()
        
    def equals(self, ob) -> bool:
        if not isinstance(ob, Fraccion):
            return False
        return self.numerador == ob.numerador and self.denominador == ob.denominador
        
    def __eq__(self, ob) -> bool:
        return self.equals(ob)
        
    def sumar(self, numero: Numerica) -> 'Fraccion':
        if not isinstance(numero, Fraccion):
            raise TypeError("El operando debe ser de tipo Fraccion")
        nuevo_num = self.numerador * numero.denominador + numero.numerador * self.denominador
        nuevo_den = self.denominador * numero.denominador
        return Fraccion(nuevo_num, nuevo_den)
        
    def restar(self, numero: Numerica) -> 'Fraccion':
        if not isinstance(numero, Fraccion):
            raise TypeError("El operando debe ser de tipo Fraccion")
        nuevo_num = self.numerador * numero.denominador - numero.numerador * self.denominador
        nuevo_den = self.denominador * numero.denominador
        return Fraccion(nuevo_num, nuevo_den)
        
    def multiplicar(self, numero: Numerica) -> 'Fraccion':
        if not isinstance(numero, Fraccion):
            raise TypeError("El operando debe ser de tipo Fraccion")
        nuevo_num = self.numerador * numero.numerador
        nuevo_den = self.denominador * numero.denominador
        return Fraccion(nuevo_num, nuevo_den)
        
    def dividir(self, numero: Numerica) -> 'Fraccion':
        if not isinstance(numero, Fraccion):
            raise TypeError("El operando debe ser de tipo Fraccion")
        if numero.numerador == 0:
            raise ZeroDivisionError("No se puede dividir por una fracción con numerador cero.")
        nuevo_num = self.numerador * numero.denominador
        nuevo_den = self.denominador * numero.numerador
        return Fraccion(nuevo_num, nuevo_den)

# Crear una clase de prueba que utilice los métodos implementados
class PruebaNumerica:
    @staticmethod
    def main():
        print("\n=== PRUEBA DE FRACCIONES (CLASE NUMÉRICA) ===")
        f1 = Fraccion(1, 2)
        f2 = Fraccion(3, 4)
        f3 = Fraccion(2, 4)  # Debería simplificarse a 1/2
        
        print(f"Fracción 1 (f1): {f1}")
        print(f"Fracción 2 (f2): {f2}")
        print(f"Fracción 3 (f3, inicializada como 2/4): {f3}")
        
        # Prueba de equals / __eq__
        print(f"¿f1 es igual a f3?: {f1.equals(f3)}")
        print(f"¿f1 es igual a f2?: {f1.equals(f2)}")
        
        # Prueba de operaciones
        suma = f1.sumar(f2)
        resta = f1.restar(f2)
        mult = f1.multiplicar(f2)
        div = f1.dividir(f2)
        
        print(f"Suma ({f1} + {f2}) = {suma}")
        print(f"Resta ({f1} - {f2}) = {resta}")
        print(f"Multiplicación ({f1} * {f2}) = {mult}")
        print(f"División ({f1} / {f2}) = {div}")

if __name__ == "__main__":
    PruebaNumerica.main()