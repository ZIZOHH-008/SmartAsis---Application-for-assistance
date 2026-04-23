import tkinter as tk
from tkinter import ttk
from datetime import date
import mysql.connector


class RegistroAsistenciaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Asistencia")

        # Conectar a la base de datos
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="base_datos"
        )
        self.cursor = self.conexion.cursor()

        # Crear una lista de estudiantes
        self.estudiantes = self.obtener_estudiantes()

        # Crear la tabla de asistencia en Tkinter
        self.tabla_asistencia = ttk.Treeview(root, columns=("Nombre", "Presente"), show="headings")
        self.tabla_asistencia.heading("Nombre", text="Nombre")
        self.tabla_asistencia.heading("Presente", text="Presente")

        for est in self.estudiantes:
            self.tabla_asistencia.insert("", "end", values=(est[1], False))

        self.tabla_asistencia.pack()

        # Botón para guardar la asistencia
        self.boton_guardar = tk.Button(root, text="Guardar Asistencia", command=self.guardar_asistencia)
        self.boton_guardar.pack()

    def obtener_estudiantes(self):
        # Consulta de estudiantes desde la base de datos
        self.cursor.execute("SELECT id, nombreEst FROM estudiante")
        return self.cursor.fetchall()

    def guardar_asistencia(self):
        # Guardar asistencia en la base de datos
        fecha_hoy = date.today()
        for item in self.tabla_asistencia.get_children():
            nombre, presente = self.tabla_asistencia.item(item, "values")
            presente = bool(presente)  # Convertir a booleano
            # Obtener ID del estudiante según el nombre (puedes optimizar el código para hacerlo más directo)
            self.cursor.execute("SELECT id FROM estudiante WHERE nombreEst = %s", (nombre,))
            estudiante_id = self.cursor.fetchone()[0]

            # Insertar el registro de asistencia
            self.cursor.execute(
                "INSERT INTO asistencia (estudiante_id, fecha, presente) VALUES (%s, %s, %s)",
                (estudiante_id, fecha_hoy, presente)
            )

        self.conexion.commit()
        print("Asistencia guardada correctamente")


# Crear la ventana de Tkinter y ejecutar el sistema de asistencia
root = tk.Tk()
app = RegistroAsistenciaApp(root)
root.mainloop()
