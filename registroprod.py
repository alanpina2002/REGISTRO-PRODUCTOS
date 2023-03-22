import tkinter as tk
from tkinter import ttk

def registrar_producto():
    nombre = nombre_entry.get()
    sku = sku_entry.get()
    departamento = departamento_var.get()
    proveedor = proveedor_combobox.get()
    idioma = idioma_var.get()
    
    print(f"Nombre: {nombre}")
    print(f"SKU: {sku}")
    print(f"Departamento: {departamento}")
    print(f"Proveedor: {proveedor}")
    print(f"Idioma: {idioma}")
    
root = tk.Tk()
root.title("Registro de productos")

# Nombre
nombre_label = ttk.Label(root, text="Nombre:")
nombre_label.grid(column=0, row=0, padx=5, pady=5)
nombre_entry = ttk.Entry(root)
nombre_entry.grid(column=1, row=0, padx=5, pady=5)

# SKU
sku_label = ttk.Label(root, text="SKU:")
sku_label.grid(column=0, row=1, padx=5, pady=5)
sku_entry = ttk.Entry(root)
sku_entry.grid(column=1, row=1, padx=5, pady=5)

# Departamento
departamento_label = ttk.Label(root, text="Departamento:")
departamento_label.grid(column=0, row=2, padx=5, pady=5)
departamento_var = tk.StringVar()
departamento_radiobutton1 = ttk.Radiobutton(root, text="Electrónica", variable=departamento_var, value="Electrónica")
departamento_radiobutton1.grid(column=1, row=2, padx=5, pady=5)
departamento_radiobutton2 = ttk.Radiobutton(root, text="Ropa", variable=departamento_var, value="Ropa")
departamento_radiobutton2.grid(column=2, row=2, padx=5, pady=5)

# Proveedor
proveedor_label = ttk.Label(root, text="Proveedor:")
proveedor_label.grid(column=0, row=3, padx=5, pady=5)
proveedor_combobox = ttk.Combobox(root, values=["Proveedor 1", "Proveedor 2", "Proveedor 3"])
proveedor_combobox.grid(column=1, row=3, padx=5, pady=5)

# Idioma
idioma_label = ttk.Label(root, text="Idioma:")
idioma_label.grid(column=0, row=4, padx=5, pady=5)
idioma_var = tk.StringVar()
idioma_radiobutton1 = ttk.Radiobutton(root, text="Español", variable=idioma_var, value="Español")
idioma_radiobutton1.grid(column=1, row=4, padx=5, pady=5)
idioma_radiobutton2 = ttk.Radiobutton(root, text="Inglés", variable=idioma_var, value="Inglés")
idioma_radiobutton2.grid(column=2, row=4, padx=5, pady=5)

# Botón de registro
registrar_button = ttk.Button(root, text="Registrar", command=registrar_producto)
registrar_button.grid(column=1, row=5, padx=5, pady=5)

root.mainloop()