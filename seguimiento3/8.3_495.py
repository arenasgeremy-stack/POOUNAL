'''Se requiere desarrollar un programa con interfaz grafica de usuario que
permita calcular el volumen y superficie de varias figuras geometricas. Las
figuras geometricas son el cilindro, la esfera y la piramide.
Para el cilindro se solicitan su radio y altura (en centimetros).
Para la esfera, su radio (en centimetros).
Para la piramide, su base, altura y apotema (en centimetros).
Una vez ingresados estos datos, el programa calcula el volumen y
superficie de cada figura. Para desarrollar el programa se debe crear una
jerarquia de clases para las diferentes figuras geometricas requeridas.
Agregar el calculo del volumen y superficie de otras figuras geometricas como el cubo y el prisma.
Agregar a cada figura geometrica correspondiente su imagen correspondiente.'''
import math
import tkinter as tk
#decidi no hacer la clase figuras geometricas como un menu de vinculos para las otras
#sino hacerla directamente la ventana principal
class FiguraGeometrica:
    #clase base para todas las figuras geometricas
    def volumen(self):
        raise NotImplementedError("Subclase debe implementar volumen()")#esto solo es para escalar el codigo
    def superficie(self):
        raise NotImplementedError("Subclase debe implementar superficie()")#para que al llamarlo no se confunda

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    def volumen(self):
        return math.pi * self.radio**2 * self.altura
    def superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    def volumen(self):
        return (4/3) * math.pi * self.radio**3
    def superficie(self):
        return 4 * math.pi * self.radio**2

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    def volumen(self):
        return (1/3) * self.base**2 * self.altura
    def superficie(self):
        return self.base**2 + 2 * self.base * self.apotema

class Cubo(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado
    def volumen(self):
        return self.lado**3
    def superficie(self):
        return 6 * self.lado**2

class Prisma(FiguraGeometrica):
    def __init__(self, largo, ancho, altura):
        self.largo = largo
        self.ancho = ancho
        self.altura = altura
    def volumen(self):
        return self.largo * self.ancho * self.altura
    def superficie(self):
        l, a, h = self.largo, self.ancho, self.altura
        return 2 * (l*a + l*h + a*h)

FIGURAS = ["Cilindro", "Esfera", "Piramide", "Cubo", "Prisma"]

CAMPOS = {
    "Cilindro": [("Radio (cm):",  "radio"), ("Altura (cm):", "altura")],
    "Esfera":   [("Radio (cm):",  "radio")],
    "Piramide": [("Base (cm):",   "base"),  ("Altura (cm):", "altura"), ("Apotema (cm):", "apotema")],
    "Cubo":     [("Lado (cm):",   "lado")],
    "Prisma":   [("Largo (cm):",  "largo"), ("Ancho (cm):",  "ancho"),  ("Altura (cm):",  "altura")],
}

COLORES = {
    "Cilindro": "#06B6D4",
    "Esfera":   "#8B5CF6",
    "Piramide": "#F59E0B",
    "Cubo":     "#10B981",
    "Prisma":   "#F97316",
}


class InterfazFiguras:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Figuras Geometricas")
        self.root.configure(bg="#1A1A2E")
        self.root.resizable(False, False)
        ancho, alto = 520, 690
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth()  // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto  // 2)
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.figura_actual = "Cilindro"
        self.entradas = {}
        self.botones_figura = {}
        self.crear_widgets()
        self.seleccionar_figura("Cilindro")

    def crear_widgets(self):
        header = tk.Frame(self.root, bg="#0F0F1A", pady=12)
        header.pack(fill="x")
        tk.Label(header, text="Figuras Geometricas",
                font=("Segoe UI", 16, "bold"), bg="#0F0F1A", fg="#FFFFFF").pack()
        tk.Label(header, text="Selecciona una figura e ingresa sus medidas",
                font=("Segoe UI", 9), bg="#0F0F1A", fg="#A0AEC0").pack()
        #esto es para la seleccion de la figura
        sel_frame = tk.Frame(self.root, bg="#16213E", pady=6)
        sel_frame.pack(fill="x")
        for figura in FIGURAS:
            btn = tk.Button(
                sel_frame, text=figura,
                font=("Segoe UI", 9, "bold"),
                bg="#16213E", fg="#A0AEC0",
                relief="flat", borderwidth=0, cursor="hand2",
                padx=6, pady=7,
                command=lambda f=figura: self.seleccionar_figura(f)
            )
            btn.pack(side="left", expand=True, fill="x", padx=2)
            self.botones_figura[figura] = btn
        # Tarjeta principal
        card = tk.Frame(self.root, bg="#1E1E2E", padx=20, pady=15)
        card.pack(fill="both", expand=True, padx=12, pady=10)
        # Canvas, segun gemini esta es la manera de dibujar las figuras
        self.canvas = tk.Canvas(card, width=460, height=160,
            bg="#0D1117", highlightthickness=1,
            highlightbackground="#2D2D4E")
        self.canvas.pack(fill="x", pady=(0, 12))
        # los campos de entrada
        self.inputs_frame = tk.Frame(card, bg="#1E1E2E")
        self.inputs_frame.pack(fill="x")
        # Etiqueta de error inivisble como en el anterior ejercicio
        self.lbl_error = tk.Label(card, text="",
            font=("Segoe UI", 9, "bold"),
            bg="#1E1E2E", fg="#EF4444",
            wraplength=450, justify="center", pady=3)
        self.lbl_error.pack(fill="x")
        # Boton calcular
        self.btn_calcular = tk.Button(
            card, text="Calcular",
            font=("Segoe UI", 10, "bold"),
            bg="#06B6D4", fg="#FFFFFF",
            activebackground="#0891B2", activeforeground="#FFFFFF",
            relief="flat", borderwidth=0, cursor="hand2", pady=9,
            command=self.calcular
        )
        self.btn_calcular.pack(fill="x", pady=(4, 10))
        self.btn_calcular.bind("<Enter>", lambda e: self.btn_calcular.config(bg="#0891B2"))
        self.btn_calcular.bind("<Leave>", lambda e: self.btn_calcular.config(bg=COLORES[self.figura_actual]))
        # Panel de resultados
        res_frame = tk.LabelFrame(card, text=" Resultados ",
            font=("Segoe UI", 10, "bold"),
            bg="#1E1E2E", fg="#06B6D4",
            relief="solid", borderwidth=1,
            padx=15, pady=10)
        res_frame.pack(fill="both", expand=True)
        self.lbl_volumen = self.crear_label_resultado(res_frame, "Volumen:", "--")
        self.lbl_superficie = self.crear_label_resultado(res_frame, "Superficie:", "--")

    def crear_label_resultado(self, parent, label_text, default_value):
        row = tk.Frame(parent, bg="#1E1E2E", pady=5)
        row.pack(fill="x")
        tk.Label(row, text=label_text, font=("Segoe UI", 10),
                bg="#1E1E2E", fg="#A0AEC0").pack(side="left")
        lbl_val = tk.Label(row, text=default_value,
                        font=("Segoe UI", 11, "bold"),
                        bg="#1E1E2E", fg="#FFFFFF")
        lbl_val.pack(side="right")
        return lbl_val

    def seleccionar_figura(self, figura):
        self.figura_actual = figura
        color = COLORES[figura]
        for f, btn in self.botones_figura.items():
            btn.config(bg=color if f == figura else "#16213E",
                    fg="#FFFFFF" if f == figura else "#A0AEC0")
        self.btn_calcular.config(bg=color)
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()
        self.entradas.clear()
        for label_text, key in CAMPOS[figura]:
            row = tk.Frame(self.inputs_frame, bg="#1E1E2E", pady=4)
            row.pack(fill="x")
            tk.Label(row, text=label_text, font=("Segoe UI", 10),
                    bg="#1E1E2E", fg="#FFFFFF", width=15, anchor="w").pack(side="left")
            entry = tk.Entry(row, font=("Segoe UI", 10),
            bg="#2D2D4E", fg="#FFFFFF",
            relief="flat", borderwidth=0,
            highlightthickness=1,
            highlightbackground="#3D3D5E",
            highlightcolor=color,
            insertbackground="#FFFFFF")
            entry.pack(side="left", fill="x", expand=True, ipady=5)
            self.entradas[key] = entry
        self.lbl_error.config(text="")
        self.lbl_volumen.config(text="--")
        self.lbl_superficie.config(text="--")
        self.dibujar_figura(figura)

#aqui vuelve lo de canvas, la verdad no entendi bien
    def dibujar_figura(self, figura):
        self.canvas.delete("all")
        cx, cy = 230, 80
        if   figura == "Cilindro": self.dibujar_cilindro(cx, cy)
        elif figura == "Esfera":   self.dibujar_esfera(cx, cy)
        elif figura == "Piramide": self.dibujar_piramide(cx, cy)
        elif figura == "Cubo":     self.dibujar_cubo(cx, cy)
        elif figura == "Prisma":   self.dibujar_prisma(cx, cy)

    def dibujar_cilindro(self, cx, cy):
        c, r, h, ry = "#06B6D4", 60, 75, 18
        self.canvas.create_rectangle(cx-r, cy-h//2, cx+r, cy+h//2, fill="#164E63", outline="")
        self.canvas.create_oval(cx-r, cy+h//2-ry, cx+r, cy+h//2+ry, fill="#0E7490", outline=c, width=2)
        self.canvas.create_oval(cx-r, cy-h//2-ry, cx+r, cy-h//2+ry, fill="#0E7490", outline=c, width=2)
        self.canvas.create_line(cx-r, cy-h//2, cx-r, cy+h//2, fill=c, width=2)
        self.canvas.create_line(cx+r, cy-h//2, cx+r, cy+h//2, fill=c, width=2)
        self.canvas.create_text(cx, cy+5, text="Cilindro", font=("Segoe UI", 11, "bold"), fill="#FFFFFF")

    def dibujar_esfera(self, cx, cy):
        c, r = "#8B5CF6", 68
        self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="#4C1D95", outline=c, width=2)
        self.canvas.create_oval(cx-r, cy-18, cx+r, cy+18, fill="", outline=c, width=1, dash=(5,3))
        self.canvas.create_oval(cx-18, cy-r, cx+18, cy+r, fill="", outline=c, width=1, dash=(5,3))
        self.canvas.create_text(cx, cy, text="Esfera", font=("Segoe UI", 11, "bold"), fill="#FFFFFF")

    def dibujar_piramide(self, cx, cy):
        c = "#F59E0B"
        bx, by = 58, 22
        bl  = (cx-bx,        cy+45)
        br  = (cx+bx,        cy+45)
        bbr = (cx+bx+bx//2,  cy+45-by)
        bbl = (cx-bx+bx//2,  cy+45-by)
        apex = (cx+bx//4,    cy-52)
        self.canvas.create_polygon(bl, br, bbr, bbl, fill="#78350F", outline=c, width=2)
        self.canvas.create_polygon(bl, br,  apex,    fill="#92400E", outline=c, width=2)
        self.canvas.create_polygon(br, bbr, apex,    fill="#B45309", outline=c, width=2)
        self.canvas.create_text(cx+5, cy+10, text="Piramide", font=("Segoe UI", 11, "bold"), fill="#FFFFFF")

    def dibujar_cubo(self, cx, cy):
        c, s, ox, oy = "#10B981", 52, 28, -20
        fl=(cx-s,cy-s); fr=(cx+s,cy-s); br=(cx+s,cy+s); bl=(cx-s,cy+s)
        bfl=(fl[0]+ox,fl[1]+oy); bfr=(fr[0]+ox,fr[1]+oy)
        bbr=(br[0]+ox,br[1]+oy)
        self.canvas.create_polygon(bfl,bfr,bbr, fill="#064E3B", outline=c, width=1)
        self.canvas.create_polygon(fl,fr,bfr,bfl,  fill="#065F46", outline=c, width=2)
        self.canvas.create_polygon(fr,br,bbr,bfr,  fill="#047857", outline=c, width=2)
        self.canvas.create_polygon(fl,fr,br,bl,    fill="#059669", outline=c, width=2)
        self.canvas.create_text(cx+ox//2, cy+oy//2+8, text="Cubo", font=("Segoe UI", 11, "bold"), fill="#FFFFFF")

    def dibujar_prisma(self, cx, cy):
        c, lx, ly, ox, oy = "#F97316", 72, 42, 30, -18
        fl=(cx-lx,cy-ly); fr=(cx+lx,cy-ly); br=(cx+lx,cy+ly); bl=(cx-lx,cy+ly)
        bfl=(fl[0]+ox,fl[1]+oy); bfr=(fr[0]+ox,fr[1]+oy)
        bbr=(br[0]+ox,br[1]+oy)
        self.canvas.create_polygon(bfl,bfr,bbr, fill="#431407", outline=c, width=1)
        self.canvas.create_polygon(fl,fr,bfr,bfl,  fill="#7C2D12", outline=c, width=2)
        self.canvas.create_polygon(fr,br,bbr,bfr,  fill="#9A3412", outline=c, width=2)
        self.canvas.create_polygon(fl,fr,br,bl,    fill="#C2410C", outline=c, width=2)
        self.canvas.create_text(cx+ox//2, cy+oy//2+8, text="Prisma", font=("Segoe UI", 11, "bold"), fill="#FFFFFF")

#validaciones para poder usar lo de calcular las figuras

    def calcular(self):
        self.lbl_error.config(text="")
        try:
            vals = {}
            for key, entry in self.entradas.items():
                texto = entry.get().strip().replace(",", ".")
                if not texto:
                    raise ValueError(f"El campo '{key}' esta vacio.")
                valor = float(texto)
                if valor <= 0:
                    raise ValueError(f"El campo '{key}' debe ser mayor que 0.")
                vals[key] = valor
            figura = self.figura_actual
            if   figura == "Cilindro": fig = Cilindro(vals["radio"], vals["altura"])
            elif figura == "Esfera":   fig = Esfera(vals["radio"])
            elif figura == "Piramide": fig = Piramide(vals["base"], vals["altura"], vals["apotema"])
            elif figura == "Cubo":     fig = Cubo(vals["lado"])
            elif figura == "Prisma":   fig = Prisma(vals["largo"], vals["ancho"], vals["altura"])
            self.lbl_volumen.config(text=f"{fig.volumen():.2f} cm3")
            self.lbl_superficie.config(text=f"{fig.superficie():.2f} cm2")
        except ValueError as e:
            self.lbl_error.config(text=str(e))
            self.lbl_volumen.config(text="--")
            self.lbl_superficie.config(text="--")
        except Exception as e:
            self.lbl_error.config(text=f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazFiguras(root)
    root.mainloop()
