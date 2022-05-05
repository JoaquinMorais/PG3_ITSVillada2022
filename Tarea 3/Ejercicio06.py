import mysql.connector


def main():
    print("Tratando de meternos a una base de datos...")
    try:
        conexion = mysql.connector.connect(user='root', password='root', host='localhost', database='Ejercicio01')
        cursor = conexion.cursor()
        print("Conexion exitosa!!!")
    except:
        print("No se pudo conectar a la base de datos...")

main()