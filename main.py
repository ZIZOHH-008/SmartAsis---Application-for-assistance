from PySide6.QtWidgets import QApplication
import sys

# Importamos la clase iniciar_sesion desde frontPage
from frontPage import iniciar_sesion

# Crear la aplicación
app = QApplication(sys.argv)

# Crear una instancia de la clase iniciar_sesion
login_window = iniciar_sesion()

# Ejecutar la aplicación de login
login_window.ejecutar_login()  # Ejecuta el bucle de eventos de la ventana de login

# Cierra la aplicación al salir de login
app.quit()

# Iniciar el bucle de eventos y garantiza salida con 0 al cerrar
sys.exit(0)  # Esto garantiza que la aplicación se cierre con un código de salida 0
