import sqlite3
from sqlite3 import Error

def conexion_sql(): #defnir un conector y manejo de errores
    try: 
        con = sqlite3.connect('basededatos.db') #la base a la que queremos concetarnos 
        return con 
    except Error:
        print(Error)

def sql_tabla(con): #creamos una tabla que utñiza el conector y definimos que elementos tendra nuestra tabla
    cursor_obj= con.cursor()    #y el tipo de datos que es cada elemento 
    cursor_obj.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, departamento text, puesto text, fecha_contratacion text)")
    con.commit() #una vez que tenemos la conexión, ejecutamos el comando
    
def sql_insertar(con, valores_columna): 
    cursor_obj= con.cursor()
    cursor_obj.execute("INSERT INTO empleados(id, nombre, salario, departamento, puesto, fecha_contratacion) VALUES(?,?,?,?,?,?)", valores_columna)
    con.commit()
    
def sql_actualizar(con):
    cursor_obj= con.cursor() 
    cursor_obj.execute('UPDATE empleados SET nombre = "Montserrat" WHERE id=2')
    con.commit()
    
def sql_seleccionar(con, comando):
    cursor_obj= con.cursor() 
    cursor_obj.execute(comando)
    filas= cursor_obj.fetchall()
    for fila in filas:
        print(fila)

def sql_borrar_tabla(con):
    cursor_obj= con.cursor()
    cursor_obj.execute('DROP table IF EXISTS empleados')
    con.commit()
    
con = conexion_sql() #manda a llamar la funcion 
#sql_actualizar(con)
#sql_seleccionar(con, 'SELECT * FROM empleados') #seleccionar todos los campos#
#sql_seleccionar(con, 'SELECT id, nombre FROM empleados WHERE salario>35000')
#sql_seleccionar(con, 'SELECT name FROM sqlite_master WHERE type="table" ')
sql_borrar_tabla(con)



