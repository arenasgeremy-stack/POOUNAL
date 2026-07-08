'''Realizar una aplicacion de interfaz grafica, que ingrese, consulte, elimine y  modifique registros en un archivo de texto.
How to create
How to read
How to update
How to delete
'''
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class EditorTexto:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Archivos de Texto")
        self.root.geometry("700x500")

        self.archivo_actual = None

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(fill=tk.X, padx=5, pady=5)

        tk.Button(frame_botones, text="Nuevo", command=self.nuevo_archivo, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Abrir", command=self.abrir_archivo, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Guardar", command=self.guardar_archivo, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Guardar como...", command=self.guardar_como, width=15).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_botones, text="Eliminar archivo", command=self.eliminar_archivo, width=15).pack(side=tk.LEFT, padx=5)

        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.area_texto = tk.Text(self.root, yscrollcommand=scrollbar.set, font=("Consolas", 12))
        self.area_texto.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.area_texto.yview)

    def nuevo_archivo(self):
        self.area_texto.delete(1.0, tk.END)
        self.archivo_actual = None
        self.root.title("Gestor de Archivos de Texto - Nuevo Archivo")

    def abrir_archivo(self):
        ruta = filedialog.askopenfilename(defaultextension=".txt", 
            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    contenido = f.read()
                self.area_texto.delete(1.0, tk.END)
                self.area_texto.insert(tk.END, contenido)
                self.archivo_actual = ruta
                self.root.title(f"Gestor de Archivos de Texto - {os.path.basename(ruta)}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{str(e)}")

    def guardar_archivo(self):
        if self.archivo_actual:
            try:
                contenido = self.area_texto.get(1.0, tk.END + "-1c")
                with open(self.archivo_actual, "w", encoding="utf-8") as f:
                    f.write(contenido)
                messagebox.showinfo("Éxito", "Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
        else:
            self.guardar_como()

    def guardar_como(self):
        ruta = filedialog.asksaveasfilename(defaultextension=".txt", 
                                            filetypes=[("Archivos de Texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta:
            try:
                contenido = self.area_texto.get(1.0, tk.END + "-1c")
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write(contenido)
                self.archivo_actual = ruta
                self.root.title(f"Gestor de Archivos de Texto - {os.path.basename(ruta)}")
                messagebox.showinfo("Listo", "Archivo guardado correctamente")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")

    def eliminar_archivo(self):
        if self.archivo_actual and os.path.exists(self.archivo_actual):
            respuesta = messagebox.askyesno("Confirmar", f"¿Seguro que desea eliminar permanentemente el archivo:\n{self.archivo_actual}?")
            if respuesta:
                try:
                    os.remove(self.archivo_actual)
                    messagebox.showinfo("Listo", "Archivo borrado correctamente")
                    self.nuevo_archivo()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo eliminar el archivo:\n{str(e)}")
        else:
            messagebox.showwarning("Epa, cuidado", "No hay ningún archivo abierto guardado en el disco para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EditorTexto(root)
    root.mainloop()