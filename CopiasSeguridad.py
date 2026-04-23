#interfaz
from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
from principal import Ui_MainWindow

#Login
from PyQt5 import QtWidgets, uic
from recursos import *

#mysql
import mysql.connector



class iniciar_sesion:
    def __init__(self):
        # Crear la aplicación y cargar las interfaces de usuario
        self.app = QtWidgets.QApplication([])  # Esto se ejecutará al crear una instancia de iniciar_sesion
        self.login = uic.loadUi("QT/login.ui")
        self.entrar = uic.loadUi("QT/login_correcto.ui")
        self.error = uic.loadUi("QT/login_incorrecto.ui")

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
        elif name == 'Juan Parra' and password == "1234":
            #self.gui_entrar()
            # Abrir la ventana principal si el login es exitoso
            self.ventana_principal = MysideBar()  # Crear la ventana principal
            self.ventana_principal.show()  # Mostrarla
            self.app.quit()  # Salir de la ventana de login (termina la ejecución del bucle de eventos de la ventana de login)
        else:
            self.gui_error()

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

        # Activar barra lateral si es verdadero
        self.icon_only_widget.setHidden(False)

        # Activar menú asistencia si es verdadero
        self.useasistencia_2.setHidden(False)

    # Conectar botones
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

        self.info_smart1.clicked.connect(self.switch_infoSmartA)
        self.info_smart2.clicked.connect(self.switch_infoSmartA)

        self.usegestion_2.clicked.connect(self.switch_estudiantes)

        self.resgistrar_asis_2.clicked.connect(self.switch_registrar)

        self.ver_asis_2.clicked.connect(self.switch_registros)

        #MySQL
        #self.create_connection()
        #self.create_students_table()
        self.add_Button.clicked.connect(self.open_addStudent_dialog)



    # Páginas
    def switch_login(self):
        self.close()

        # Crea e inicia la ventana de inicio de sesión
        login_window = iniciar_sesion()  # Cambié el nombre de la instancia para evitar conflicto
        login_window.ejecutar_login()  # Ejecuta el login

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


class database():
    def create_connection(self):

        #identificar la base de datos
        host_name = 'localhost',
        user_name = 'root',
        mypassword = ''  # Sin contraseña
        database_name = 'SmartAsis',

        #Conectar con la base de datos
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = mypassword
        )

        #Crea cursor para SQL
        cursor = self.mydb.cursor()

        #Crea la base de datos si no existe
        cursor.execute(f'CREATE DATABASE IF NOT EXIST{database_name}')

        #Conectar con la base creada
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = mypassword,
            database = database_name
        )

        return self.mydb

    def create_students_table(self):
        cursor = self.create_connection().cursor
        create_students_table_query = f"""
        '''CREATE TABLE IF NOT EXISTS estudiante (
                        id_est INTEGER PRIMARY KEY,
                        apelli_est VARCHAR(20) NOT NULL,
                        nom_est VARCHAR(20) NOT NULL,
                        grad_est INTEGER NOT NULL, 
                        edad_est INTEGER NOT NULL, 
                        gen_est VARCHAR(20) NOT NULL,
                        dir_est VARCHAR(20) NOT NULL,                          
                        tel_est INTEGER NOT NULL,
                        direc_est VARCHAR(20) NOT NULL,
                        )"""
        cursor.execute(create_students_table_query)

        self.mydb.commit()
        self.mydb.close()

    def open_addStudent_dialog(self):
        from formulario import Ui_StudentsDialog

        addStudent_dialog = Ui_StudentsDialog(self)
        result = addStudent_dialog.exec()

        if result == Ui_StudentsDialog.accepted:
            pass


