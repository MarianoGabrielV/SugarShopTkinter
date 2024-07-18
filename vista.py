from tkinter import StringVar
from tkinter import DoubleVar
from tkinter import IntVar
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import PhotoImage

from Sugar_modelo import base
from Sugar_modelo import crear_tabla
from Sugar_modelo import alta
from Sugar_modelo import modificar
from Sugar_modelo import borrar


def vista_principal(sugar):
    

    sugar.title("Lista de precios de SugarShop")
    sugar.geometry("893x900")
    sugar.configure(bg="old lace")
    sugar.iconbitmap("C:\\Users\\Usuario\\Desktop\\Programacion\\Practica de lenguajes\\Python\\UTN.ELEAR\\Proyecto\\Entrega_final\\img\\sugarlogo_5Ze_icon.ico")
    imagen = PhotoImage(file="C:/Users/Usuario/Desktop/Programacion/Practica de lenguajes/Python/UTN.ELEAR/Proyecto/Entrega_final/img/sugarlogo.gif")
    imagen = imagen.subsample(3, 3)
    imagen_label = Label(sugar, image=imagen)
    imagen_label.grid(row=1, column=2, columnspan=3)

    titulo = Label(sugar, text="Esta es la la base donde se cargaran, modificaran y almacenaran \n los datos de los productos.",
    fg="gray30", background="linen", font=("arial black", 18), width=53, height=5)
    titulo.grid(row=0, column=0, sticky="w"+"e", columnspan=4, padx=1, pady=1)


    producto = Label(sugar, text="Ingrese el producto", font=(
    "calibri", 15), height=3, fg="gray30", bg="old lace")
    producto.grid(row=1, column=0, sticky="w")
    cantidad_unidades = Label(sugar, text="Cantidades en unidades", font=(
    "calibri", 15), height=3, fg="gray30", bg="old lace")
    cantidad_unidades.grid(row=2, column=0, sticky="w")
    precio_costo = Label(sugar, text="Precio de costo", font=(
    "calibri", 15), height=3, fg="gray30", bg="old lace")
    precio_costo.grid(row=3, column=0, sticky="w")
    precio_publico = Label(sugar, text="Precio de venta al publico", font=(
    "calibri", 15), height=3, fg="gray30", bg="old lace")
    precio_publico.grid(row=4, column=0, sticky="w")

    id_modificar_label = Label(sugar, text="ID a Modificar", font=(
    "calibri", 15), height=3, fg="gray30", bg="old lace")
    id_modificar_label.grid(row=5, column=0, sticky="w")
    prod_val = StringVar()
    cant_val = IntVar()
    costo_val = DoubleVar()
    precio_val = DoubleVar()

    id_modificar = IntVar()

    entradaA = Entry(sugar, textvariable=prod_val, font=10)
    entradaA.grid(row=1, column=1)
    entradaB = Entry(sugar, textvariable=cant_val, font=10)
    entradaB.grid(row=2, column=1)
    entradaC = Entry(sugar, textvariable=costo_val, font=10)
    entradaC.grid(row=3, column=1)
    entradaD = Entry(sugar, textvariable=precio_val, font=10)
    entradaD.grid(row=4, column=1)
    entrada_id_modificar = Entry(sugar, textvariable=id_modificar, font=10)
    entrada_id_modificar.grid(row=5, column=1)


    tree = ttk.Treeview(sugar)
    tree["columns"] = ("col1", "col2", "col3", "col4")
    tree.column("#0", width=90, minwidth=50, anchor="w")
    tree.column("col1", width=200, minwidth=80)
    tree.column("col2", width=200, minwidth=80)
    tree.column("col3", width=200, minwidth=80)
    tree.column("col4", width=200, minwidth=80)
    tree.heading("#0", text="ID")
    tree.heading("col1", text="Producto")
    tree.heading("col2", text="Cantidad")
    tree.heading("col3", text="Precio Costo")
    tree.heading("col4", text="Precio Publico")
    tree.grid(row=10, column=0, columnspan=3)

    alta_bot = Button(sugar, text="Ingresar", width=20, height=2, font=5, fg="white", bg="green", relief="solid",
                  command=lambda: alta(prod_val.get(), cant_val.get(), costo_val.get(), precio_val.get(), tree))
    alta_bot.grid(row=6, column=0)
    baja_bot = Button(sugar, text="Borrar", width=20, height=2, font=5,
                  fg="white", bg="red", relief="solid", command=lambda: borrar(tree))
    baja_bot.grid(row=6, column=1)
    modificar_bot = Button(sugar, text="Modificar", width=20, height=2, font=5, fg="white", bg="orange", relief="solid", command=lambda: modificar(
    id_modificar.get(), producto=prod_val.get(), cantidad_unidades=cant_val.get(), precio_costo=costo_val.get(), precio_publico=precio_val.get(), tree=tree))
    modificar_bot.grid(row=6, column=2)



