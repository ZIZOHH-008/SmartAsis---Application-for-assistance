import mysql.connector  # pip install mysql-connector-python

class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database='base_datos',
            user='root',
            password=''  # Sin contraseña
        )

    def inserta_estudiante(self, codigo, nombreEst, apellidoEst, gradoEst, edadEst, telEst):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO estudiante (codigoEst, nombreEst, apellidoEst, gradoEst, edadEst, telEst) 
                 VALUES('{}', '{}', '{}', '{}', '{}', '{}')'''.format(codigo, nombreEst, apellidoEst, gradoEst, edadEst, telEst)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def mostrar_estudiante(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM estudiante"
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    def busca_estudiante(self, nombre_est):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM estudiante WHERE nombreEst = '{}'".format(nombre_est)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def busca_codigoEst(self, codigo):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM estudiante WHERE codigoEst = '{}'".format(codigo)
        cur.execute(sql)
        codigoX = cur.fetchall()
        cur.close()
        return codigoX

    def mostrar_codigoEst(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM estudiante"
        cursor.execute(sql)
        registro = cursor.fetchall()
        cursor.close()
        return registro

    def elimina_estudiante(self, nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM estudiante WHERE nombreEst = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()


  