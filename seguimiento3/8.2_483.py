'''Enunciado: Notas
Se requiere desarrollar un programa con interfaz gráfica de usuario que
genere una ventana donde se solicite el ingreso de cinco notas obtenidas
por un estudiante.
El programa debe calcular y mostrar en la parte inferior de la ventana
los siguientes datos:
El promedio de notas ingresadas.
La desviación estándar de las notas ingresadas.
La mayor nota obtenida.
La menor nota obtenida.'''
# no instalo porque segun gemini ya viene instalada en windows
import math
import tkinter as tk
class CalculadoraNotas:
    def __init__(self,notas):
        self.notas = notas
    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas)/len(self.notas)
    def calcular_desviacion(self):
        if not self.notas:
            return 0.0
        promedio = self.calcular_promedio()
        varianza = sum((nota - promedio)**2 for nota in self.notas) / len(self.notas)
        return math.sqrt(varianza)
    def obtener_mayor(self):
        if not self.notas:
            return 0.0
        return max(self.notas)
    def obtener_menor(self):
        if not self.notas:
            return 0.0
        return min(self.notas)
'''notas = [3,4,5,2,4]
print(CalculadoraNotas(notas).calcular_promedio())
print(CalculadoraNotas(notas).calcular_desviacion())
print(CalculadoraNotas(notas).obtener_mayor())
print(CalculadoraNotas(notas).obtener_menor())''' #eso erapara probar
class InterfazGrafica:
    def __init__ (self, root):
        self.root = root
        self.root.title("Calculadora de Notas")
        self.root.configure(bg="#2C2C31")
        ancho = 420
        alto = 620
        self.root.geometry(f"{ancho}x{alto}")
        self.root.resizable(False,False)
        self.crear_widgets()
    def crear_widgets(self):
        header_frame = tk.Frame(self.root, bg="#1F1F24", pady=15)
        header_frame.pack(fill="x", side="top")
        label_titulo = tk.Label(header_frame,
        text = "Calculadora de Notas",
        font = ("Segoe UI", 16, "bold"),
        bg = "#1F1F24",
        fg = "#FFFFFF"
        )
        label_titulo.pack()
        label_subtitulo = tk.Label(
            header_frame, 
            text="Ingrese 5 calificaciones de 0.0 a 5.0", 
            font=("Segoe UI", 9), 
            bg="#1F1F24", 
            fg="#E0E7FF"
        )
        label_subtitulo.pack()#side="left")
        card = tk.Frame(self.root, bg="#2C2C31", padx=20, pady=18, relief="solid", borderwidth=0)
        card.pack(fill="both", expand=True, padx=15, pady=15)
        inputs_frame = tk.Frame(card, bg="#2C2C31")
        inputs_frame.pack(fill="x")
        self.entradas_notas = []
        for i in range(5):
            row_frame = tk.Frame(inputs_frame, bg="#2C2C31", pady=5)
            row_frame.pack(fill="x")
            lbl = tk.Label(
                row_frame,
                text = f"Nota {i+1}:",
                font = ("Segoe UI",10),
                bg = "#2C2C31",
                fg = "#FFFFFF",
                width = 10,
                anchor = "w"
            )
            lbl.pack(side="left")
            entry = tk.Entry(
                row_frame,
                font = ("Segoe UI", 10),
                bg = "#2C2C31",
                fg = "#FFFFFF",
                relief = "sunken",
                borderwidth = 3,
                highlightthickness = 0
            )
            entry.config(highlightbackground="#CBD5E1", highlightcolor="#4F46E5")
            entry.pack(side="left", fill="x", expand=True, ipady=3)
            self.entradas_notas.append(entry)
            
        self.lbl_error = tk.Label(
            card, 
            text="", 
            font=("Segoe UI", 9, "bold"), 
            bg="#2C2C31", 
            fg="#EF4444", 
            wraplength=340, 
            justify="center",
            pady=5
        )
        self.lbl_error.pack(fill="x")
        btn_frame = tk.Frame(card, bg="#2C2C31", pady=10)
        btn_frame.pack(fill="x")
        self.btn_calcular = tk.Button(
            btn_frame, 
            text="Calcular Estadísticas", 
            font=("Segoe UI", 10, "bold"), 
            bg="#2C2C31", 
            fg="#FFFFFF", 
            activebackground="#1F1F24", 
            activeforeground="#FFFFFF",
            relief="raised", 
            borderwidth=3, 
            cursor="hand2",
            command=self.calcular,
            pady=8
        )
        self.btn_calcular.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.btn_limpiar = tk.Button(
            btn_frame, 
            text="Limpiar", 
            font=("Segoe UI", 10, "bold"), 
            bg="#2C2C31", 
            fg="#FFFFFF", 
            activebackground="#1F1F24", 
            activeforeground="#FFFFFF",
            relief="raised", 
            borderwidth=3, 
            cursor="hand2",
            command=self.limpiar,
            pady=8
        )
        self.btn_limpiar.pack(side="right", fill="x", expand=True, padx=(5, 0))

        self.results_frame = tk.LabelFrame(
            card, 
            text=" Resultados Estadísticos ", 
            font=("Segoe UI", 10, "bold"),
            bg="#2C2C31", 
            fg="#FFFFFF",
            relief="sunken", 
            borderwidth=3, 
            padx=15, 
            pady=10
        )
        self.results_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.lbl_promedio = self.crear_label_resultado(self.results_frame, "Promedio de notas:", "0.0")
        self.lbl_desviacion = self.crear_label_resultado(self.results_frame, "Desviación estándar:", "0.0")
        self.lbl_mayor = self.crear_label_resultado(self.results_frame, "Nota más alta (Mayor):", "0.0")
        self.lbl_menor = self.crear_label_resultado(self.results_frame, "Nota más baja (Menor):", "0.0")
    def crear_label_resultado(self, parent, label_text, default_value):
        row = tk.Frame(parent, bg="#2C2C31", pady=4)
        row.pack(fill="x")
        lbl_desc = tk.Label(
            row, 
            text=label_text, 
            font=("Segoe UI", 9), 
            bg="#2C2C31", 
            fg="#FFFFFF"
        )
        lbl_desc.pack(side="left")
        lbl_val = tk.Label(
            row, 
            text=default_value, 
            font=("Segoe UI", 10, "bold"), 
            bg="#2C2C31", 
            fg="#FFFFFF"
        )
        lbl_val.pack(side="right")
        return lbl_val
    def validar_notas(self):
        notas = []
        for i, entry in enumerate(self.entradas_notas):
            valor_texto = entry.get().strip()
            
            # Validar vacío
            if not valor_texto:
                raise ValueError(f"Error: La Nota {i+1} está vacía. Complete todas las notas.")
            
            # Normalizar separadores decimales (, por .)
            valor_texto = valor_texto.replace(",", ".")
            try:
                nota = float(valor_texto)
            except ValueError:
                raise ValueError(f"Error: La Nota {i+1} ('{valor_texto}') no es un número válido.")
            
            # Validar rango (estándar escolar/universitario de 0.0 a 5.0)
            if not (0.0 <= nota <= 5.0):
                raise ValueError(f"Error: La Nota {i+1} ({nota}) debe estar en el rango de 0.0 a 5.0.")
            
            notas.append(nota)
        return notas
    def calcular(self):
        self.lbl_error.config(text="")
        try:
            notas = self.validar_notas()

            calculadora = CalculadoraNotas(notas)

            self.lbl_promedio.config(text=f"{calculadora.calcular_promedio():.2f}")
            self.lbl_desviacion.config(text=f"{calculadora.calcular_desviacion():.2f}")
            self.lbl_mayor.config(text=f"{calculadora.obtener_mayor():.2f}")
            self.lbl_menor.config(text=f"{calculadora.obtener_menor():.2f}")

        except ValueError as e:
            self.lbl_error.config(text=str(e))
        except Exception as e:
            self.lbl_error.config(text=f"Error inesperado: {str(e)}")

    def limpiar(self):
        for entry in self.entradas_notas:
            entry.delete(0, tk.END)
        self.lbl_promedio.config(text="0.0")
        self.lbl_desviacion.config(text="0.0")
        self.lbl_mayor.config(text="0.0")
        self.lbl_menor.config(text="0.0")
        self.lbl_error.config(text="")
        self.entradas_notas[0].focus()
if __name__ == "__main__":
    root = tk.Tk()
    ventana = InterfazGrafica(root)
    root.mainloop()

#Por si acaso profe si tuve en cuenta los ejercicios propuestos