import sqlite3
from sqlite3 import Error

def conexion_sql():
    try: 
        con = sqlite3.connect('basededatos.db')
        return con 
    except Error:
        print(Error)

def sql_tabla(con):
    cursor_obj= con.cursor()
    cursor_obj.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, departamento text, puesto text, fecha_contratacion text)")
    con.commit()

con = conexion_sql()
sql_tabla(con)























