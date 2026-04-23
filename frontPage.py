#interfaz
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from principal import Ui_MainWindow

#Login
from PyQt5 import QtWidgets, uic
import recursos

#mysql
import mysql.connector
from main_conexion import main_conexion_dialogue
from conexion import Registro_datos


class iniciar_sesion:
    def __init__(self):
        # Crear la aplicación y cargar las interfaces de usuario
        self.app = QtWidgets.QApplication([])   # Esto se ejecutará al crear una instancia de iniciar_sesion
        self.login = uic.loadUi("QT/login.ui")
        self.entrar = uic.loadUi("QT/login_correcto.ui")
        self.error = uic.loadUi("QT/login_incorrecto.ui")

        self.db = Registro_datos()

        # Configurar eventos de botones
        self.configurar_eventos()

    def configurar_eventos(self):
        # Conectar los botones con las funciones correspondientes
        self.login.ingresar_qt.clicked.connect(self.gui_login)
        self.login.salirqt.clicked.connect(self.salir)

        self.entrar.ingresar_qt.clicked.connect(self.regresar_entrar)
        self.entrar.salirqt.clicked.connect(self.salir)

        self.error.ingresar_qt.clicked.connect(self.regresar_error)
        self.error.salirqt.clicked.connect(self.salir)

    def mostrar_advertencia(self, texto):
        # Muestra un mensaje de advertencia en el login
        self.login.advertencia_qt.setText(texto)

    def gui_login(self):
        # Verificar credenciales de usuario
        name = self.login.usuario_qt.text()
        password = self.login.password_qt.text()

        if len(name) == 0 or len(password) == 0:
            self.mostrar_advertencia('Ingrese todos los datos')
            return

        try:
            cursor = self.db.conexion.cursor()  # Obtener el cursor de la conexión

            query = "SELECT * FROM profesor WHERE usuario_prof = %s AND codigo_prof = %s"
            cursor.execute(query, (name, password))
            result = cursor.fetchone()

            if result:
                self.ventana_principal = MysideBar()
                self.ventana_principal.show()
                self.login.hide()
            else:
                self.gui_error()
        except Exception as e:
            print("Error al conectarse a la base de datos:", e)
            self.mostrar_advertencia("Error en el sistema")
        finally:
            cursor.close()



    #def #gui_entrar(self):
        # Mostrar la ventana de login correcto y ocultar el login
        #self.login.hide()
        #self.entrar.show()

    def gui_error(self):
        # Mostrar la ventana de login incorrecto y ocultar el login
        self.login.hide()
        self.error.show()

    def regresar_entrar(self):
        # Regresar a la pantalla de login desde la pantalla de éxito
        self.entrar.hide()
        self.login.advertencia_qt.clear()
        self.login.show()

    def regresar_error(self):
        # Regresar a la pantalla de login desde la pantalla de error
        self.error.hide()
        self.login.advertencia_qt.clear()
        self.login.show()

    def salir(self):
        # Salir de la aplicación
        self.app.exit()

    def ejecutar_login(self):
        # Ejecutar la aplicación mostrando la ventana de login
        self.login.show()
        self.app.exec()  # Bucle de eventos de la ventana de login


class MysideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SmartAsis")

        # Activar barra lateral y otros componentes según la configuración
        self.icon_only_widget.setHidden(False)
        self.useasistencia_2.setHidden(False)

        # Conectar los botones de salida a la función `salir`
        self.salir1.clicked.connect(self.salir)
        self.salir2.clicked.connect(self.salir)

        # Conectar otros botones
        self.dashboard1.clicked.connect(self.switch_login)
        self.dashboard2.clicked.connect(self.switch_login)

        self.gestion1.clicked.connect(self.switch_gestion)
        self.gestion2.clicked.connect(self.switch_gestion)

        self.institucion1.clicked.connect(self.switch_institucion)
        self.institucion2.clicked.connect(self.switch_institucion)

        self.ajustes1.clicked.connect(self.switch_ajustes)
        self.ajustes2.clicked.connect(self.switch_ajustes)

        self.perfil1.clicked.connect(self.switch_perfil)
        self.perfil2.clicked.connect(self.switch_perfil)

        self.usegestion_2.clicked.connect(main_conexion_dialogue)

        self.resgistrar_asis_2.clicked.connect(self.switch_registrar)

        self.ver_asis_2.clicked.connect(self.switch_registros)

        self.info_smart1.clicked.connect(self.switch_infoSmartA)
        self.info_smart2.clicked.connect(self.switch_infoSmartA)

        # Inicializar en la página de gestión
        self.switch_gestion()

    # Función para salir de la aplicación
    def salir(self):
        # Cerrar la ventana principal y salir de la aplicación
        self.close()  # Cierra la ventana principal
        QtWidgets.QApplication.instance().quit()  # Cierra la aplicación completa

    # Páginas
    def switch_login(self):
        self.close()
        login_window = iniciar_sesion()
        login_window.ejecutar_login()

    def switch_gestion(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_institucion(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_ajustes(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_perfil(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_estudiantes(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_registrar(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_registros(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_infoSmartA(self):
        self.stackedWidget.setCurrentIndex(7)


#Conexión
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(
            host='localhost',
            database='base_datos',
            user='root',
            password=''  # Sin contraseña
        )

    def inserta_producto(self, codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql = '''INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos "
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()
        return nombreX

    def elimina_productos(self, nombre):
        cur = self.conexion.cursor()
        sql = '''DELETE FROM productos WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()
        cur.close()




