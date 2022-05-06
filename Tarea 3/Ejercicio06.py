import mysql.connector


def openUser():
    print("Tratando de meternos a una base de datos...")
    try:
        conexion = mysql.connector.connect(user='bdi', password='Pepe_1234', host='localhost', database='PruebasPython')
        cursor = conexion.cursor()
        print("Conexion exitosa!!!")
        
        getTable(cursor)
    except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.DatabaseError) as e:
        print(e)
        print("No se pudo conectar a la base de datos...")
        



def getTable(cursor):
    tabla = str(input("Ingrese el nombre de la tabla que quieres VER: \n>> "))
    try:
        cursor.execute(f"SELECT * FROM {tabla}")
        for id,nombre,edad in cursor.fetchall():
            print(id)
            print(nombre)
            print(edad)
        
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
        print("Error al entrar en la tabla...")



def main():
    openUser()
    
    

main()
#cursor.close()