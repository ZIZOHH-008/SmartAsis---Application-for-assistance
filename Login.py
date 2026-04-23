from PyQt5 import QtWidgets, uic

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