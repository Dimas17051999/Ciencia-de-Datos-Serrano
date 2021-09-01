import sqlite3
from sqlite3 import Error

def conexion_sql(): #defnir un conector y manejo de errores
    try: 
        con = sqlite3.connect('basededatos.db') #la base a la que
        return con                               # queremos concetarnos 
    except Error:
        print(Error)

def sql_tabla(con): #creamos una tabla que utñiza el conector y definimos que elementos tendra nuestra tabla
    cursor_obj= con.cursor()    #y el tipo de datos que es cada elemento 
    cursor_obj.execute("CREATE TABLE empleados(id integer PRIMARY KEY, nombre text, salario real, departamento text, puesto text, fecha_contratacion text)")
    con.commit() #una vez que tenemos la conexión, ejecutamos el comando

def sql_insertar(con, valores_columna): # definición de función para poner info
    cursor_obj= con.cursor() #en la tabla creada anteriormente
    cursor_obj.execute("INSERT INTO empleados(id, nombre, salario, departamento, puesto, fecha_contratacion) VALUES(?,?,?,?,?,?)", valores_columna)
    con.commit()

con = conexion_sql() #manda a llamar la funcion 

# Datos con los que se va a llenar la tabla 
fila1=(1, 'Luis', 10000, 'Programación', 'Programador Jr', '2010-10-12')
fila2=(2, 'Antonio', 40000, 'Programación', 'Programador', '2000-10-12')
fila3=(3, 'Davida', 10000, 'Programación', 'Programador Jr', '2010-10-12')
fila4=(4, 'Marco', 40000, 'Programación', 'Secretario', '2000-10-12')
fila5=(5, 'Alejandra', 1000000, 'Programación', 'Desarrollo de aplicaciones móviles', '2010-10-12')
fila6=(6, 'Daniel', 90000, 'Programación', 'Programador Sr', '2000-10-12')

sql_insertar(con, fila1)
sql_insertar(con, fila2)
sql_insertar(con, fila3)
sql_insertar(con, fila4)
sql_insertar(con, fila5)
sql_insertar(con, fila6)