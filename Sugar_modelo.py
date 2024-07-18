from tkinter import *
import sqlite3
import re



########################## BASE DE DATOS COMO SE CREA    #######################################    

########################## BASE DE DATOS COMO SE CREA #######################################
################################ MODELO #################################
def base ():
    inicia = sqlite3.connect("base_sugar.db")
    return inicia

def crear_tabla():
    inicia = base()
    cursor = inicia.cursor()
    sql = """CREATE TABLE productos (id INTEGER PRIMARY KEY AUTOINCREMENT, producto varchar(30) NOT NULL, cantidad_unidades real, precio_costo real, precio_publico real)"""
    cursor.execute(sql)
    inicia.commit()

try:
    base()
    crear_tabla()
except:
    print("Hay un error")


def alta(producto, cantidad_unidades, precio_costo, precio_publico, tree):
    cadena = producto
    patron="^[A-Za-záéíóú ]*$"  #regex para el campo cadena
    if(re.match(patron, cadena)):
        print(producto, cantidad_unidades, precio_costo, precio_publico)
        con=base()
        cursor=con.cursor()
        data=(producto, cantidad_unidades, precio_costo, precio_publico)
        sql="INSERT INTO productos(producto, cantidad_unidades, precio_costo, precio_publico) VALUES(?, ?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
    else:
        print("error en campo producto")
    

def consultar():
    global compra
    print(compra)


def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']
    con=base()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)
    
def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)
    sql = "SELECT * FROM productos ORDER BY id ASC"
    con=base()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3], fila[4]))


def modificar(id_modificar, producto=None, cantidad_unidades=None, precio_costo=None, precio_publico=None, tree=None):
    con = base()
    cursor = con.cursor()

    # Construir la consulta SQL dinámicamente
    sql = "UPDATE productos SET"
    update_values = []

    if producto is not None:
        cadena = producto
        patron = "^[A-Za-záéíóú ]*$"  # regex para el campo producto
        if re.match(patron, cadena):
            sql += " producto=?,"
            update_values.append(producto)

    if cantidad_unidades is not None:
        sql += " cantidad_unidades=?,"
        update_values.append(cantidad_unidades)

    if precio_costo is not None:
        sql += " precio_costo=?,"
        update_values.append(precio_costo)

    if precio_publico is not None:
        sql += " precio_publico=?,"
        update_values.append(precio_publico)

    # Eliminar la última coma en la consulta SQL
    sql = sql.rstrip(',')

    # Agregar el ID para identificar el registro a modificar
    update_values.append(id_modificar)

    # Agregar el WHERE para la condición de actualización
    sql += " WHERE id=?"

    # Ejecutar la consulta SQL con los valores actualizados
    cursor.execute(sql, update_values)
    con.commit()
    print("Registro modificado con éxito.")
    
    if tree is not None:
        actualizar_treeview(tree)


# base()        # se tiene que llamar para que parezca el archivo


##############################   VISTA   ########################
'''sugar = Tk()

sugar.title("Lista de precios de SugarShop")
sugar.geometry("893x900")
sugar.configure(bg="old lace")
sugar.iconbitmap("C:\\Users\\Usuario\\Desktop\\Programacion\\Practica de lenguajes\\Python\\UTN.ELEAR\\Proyecto\\Entrega_final\\sugarlogo_5Ze_icon.ico")

imagen = PhotoImage(file="sugarlogo.gif")
imagen = imagen.subsample(3, 3)
imagen_label = Label(sugar, image=imagen)
imagen_label.grid(row=1, column=2, columnspan=3) 

titulo = Label(sugar, text="Esta es la la base donde se cargaran, modificaran y almacenaran \n los datos de los productos.",fg="gray30",background="linen",font=("arial black",18),width=53,height=5)
titulo.grid(row=0, column=0,sticky=W+E, columnspan=4, padx=1, pady=1)


producto = Label(sugar, text="Ingrese el producto", font=("calibri",15),height=3,fg="gray30",bg="old lace")
producto.grid(row=1,column=0,sticky=W)
cantidad_unidades = Label(sugar, text="Cantidades en unidades", font=("calibri",15),height=3,fg="gray30",bg="old lace")
cantidad_unidades.grid(row=2,column=0,sticky=W)
precio_costo = Label(sugar, text="Precio de costo",font=("calibri",15),height=3,fg="gray30",bg="old lace")
precio_costo.grid(row=3,column=0,sticky=W)
precio_publico = Label(sugar, text="Precio de venta al publico",font=("calibri",15),height=3,fg="gray30",bg="old lace")
precio_publico.grid(row=4,column=0,sticky=W)

id_modificar_label = Label(sugar, text="ID a Modificar", font=("calibri", 15), height=3, fg="gray30", bg="old lace")
id_modificar_label.grid(row=5, column=0, sticky=W)
prod_val=StringVar()
cant_val=IntVar()
costo_val=DoubleVar()
precio_val=DoubleVar()

id_modificar = IntVar()

entradaA = Entry(sugar,textvariable=prod_val,font=10)
entradaA.grid(row=1, column=1)
entradaB = Entry(sugar,textvariable=cant_val,font=10)
entradaB.grid(row=2, column=1)
entradaC = Entry(sugar, textvariable=costo_val,font=10)
entradaC.grid(row=3, column=1)
entradaD = Entry(sugar,textvariable=precio_val,font=10)
entradaD.grid(row=4, column=1)
entrada_id_modificar = Entry(sugar, textvariable=id_modificar, font=10)
entrada_id_modificar.grid(row=5, column=1)


tree = ttk.Treeview(sugar)
tree["columns"]=("col1", "col2", "col3","col4")
tree.column("#0", width=90, minwidth=50, anchor=W)
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

alta_bot = Button(sugar, text= "Ingresar", width=20,height=2,font=5,fg="white",bg="green",relief="solid",command=lambda:alta(prod_val.get(), cant_val.get(), costo_val.get(),precio_val.get(),tree))
alta_bot.grid(row=6, column=0)
baja_bot= Button(sugar,text="Borrar", width=20,height=2,font=5,fg="white",bg="red",relief="solid",command=lambda:borrar(tree))
baja_bot.grid(row=6,column=1)
modificar_bot = Button(sugar, text="Modificar", width=20, height=2, font=5, fg="white", bg="orange", relief="solid", command=lambda: modificar(id_modificar.get(), producto=prod_val.get(), cantidad_unidades=cant_val.get(), precio_costo=costo_val.get(), precio_publico=precio_val.get(), tree=tree))
modificar_bot.grid(row=6, column=2)




sugar.mainloop()'''