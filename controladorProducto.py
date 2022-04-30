from baseDatos import conexion

#Insertar

def insertarProducto(nombre, precio, stock, categoria):
    conexionloc = conexion()
    with conexionloc.cursor() as cursor:
        cursor.execute("insert into producto(nombre, precio, stock, categoria) values (%s,%s,%s,%s)", (nombre, precio, stock, categoria))
        conexionloc.commit()
    conexionloc.close()

#Consultar todos los productos
def obtenerProductos():
    conexionloc = conexion()
    productos = []
    with conexionloc.cursor() as cursor:
        cursor.execute("select id, nombre, precio, stock, categoria from producto")
        productos = cursor.fetchall()
    conexionloc.close()
    return productos

#Consultar un producto por id
def obtenerProductoId(id):
    conexionloc = conexion()
    producto = None
    with conexionloc.cursor() as cursor:
        cursor.execute("select id, nombre, precio, stock, categoria from producto where id = %s", (id))
        producto = cursor.fetchone()
    conexionloc.close()
    return producto


#Eliminar producto
def eliminarProducto(id):
    conexionloc = conexion()
    with conexionloc.cursor() as cursor:
        cursor.execute("delete from producto where id = %s",(id))
        conexionloc.commit()
    conexionloc.close()

#Editar producto
def editarProducto(nombre, precio, stock, categoria, id):
    conexionloc = conexion()
    with conexionloc.cursor() as cursor:
        cursor.execute("update producto set nombre = %s, precio = %s, stock = %s, categoria = %s where id = %s", (nombre, precio, stock, categoria, id))
        conexionloc.commit()
    conexionloc.close()