import pymysql

#Conexion a BD
def conexion():
    return pymysql.connect(host='localhost', user='root', password='', db='productosflask', port=4306)