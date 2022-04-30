from flask import Flask, render_template, request, redirect
import controladorProducto

app = Flask(__name__)

@app.route("/")
@app.route("/productos")
def productos():
    productos = controladorProducto.obtenerProductos()
    return render_template("productos.html", productos=productos)

@app.route("/agregarProducto")
def agregarProducto():
    return render_template("agregarProducto.html")


@app.route("/agregarProducto", methods=["POST"])
def insertarProducto():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    categoria = request.form["categoria"]
    controladorProducto.insertarProducto(nombre, precio, stock, categoria)
    return redirect("/productos")

@app.route("/eliminarProducto", methods=["POST"])
def eliminarProducto():
    controladorProducto.eliminarProducto(request.form["id"])
    return redirect("/productos")


@app.route("/formulario_editar_cliente/<int:id>")
def editarProducto(id):
    # Obtener el cliente por ID
    cliente = controladorProducto.obtenerProductoId(id)
    return render_template("editarProducto.html", cliente=cliente)


@app.route("/actualizarProducto", methods=["POST"])
def actualizarProducto():
    id = request.form["id"]
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    stock = request.form["stock"]
    categoria = request.form["categoia"]
    controladorProducto.actualizar_cliente(nombre, precio, stock, categoria, id)
    return redirect("/productos")


# Iniciar el servidor
if __name__ == "__main__":
    app.run(port=4306, debug=True)