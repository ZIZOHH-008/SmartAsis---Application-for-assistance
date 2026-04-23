from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from conexion import Registro_datos

class Registro(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0, row=0)
        self.frame2 = Frame(master, bg='#304f4f')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='black')
        self.frame4.grid(column=0, row=2)

        self.codigo = StringVar()
        self.nombreEst = StringVar()
        self.apellidoEst = StringVar()
        self.gradoEst = StringVar()
        self.edadEst = StringVar()
        self.buscar = StringVar()
        self.buscarCod = StringVar()
        self.telEst = StringVar()

        self.base_datos = Registro_datos()
        self.create_widgets()





    def create_widgets(self):
        Label(self.frame1, text='R E G I S T R O \t D E \t D A T O S', bg='gray22', fg='white', font=('Holy Friday', 25, 'bold')).grid(column=0, row=0)

        Label(self.frame2, text='Agregar Nuevos Datos', fg='white', bg='#304f4f', font=('Holy Friday', 17)).grid(columnspan=2, column=0, row=0, pady=5)
        Label(self.frame2, text='Código:', fg='white', bg='#304f4f', font=('Holy Friday', 14)).grid(column=0, row=1, pady=15)
        Label(self.frame2, text='Nombre:', fg='white', bg='#304f4f', font=('Holy Friday', 14)).grid(column=0, row=2, pady=15)
        Label(self.frame2, text='Apellido:', fg='white', bg='#304f4f', font=('Holy Friday', 14)).grid(column=0, row=3, pady=15)
        Label(self.frame2, text='Grado:', fg='white', bg='#304f4f', font=('Holy Friday', 14)).grid(column=0, row=4, pady=15)
        Label(self.frame2, text='Edad:', fg='white', bg='#304f4f', font=('Holy Friday', 14)).grid(column=0, row=5, pady=15)
        Label(self.frame2, text='Teléfono:', fg='white', bg='#304f4f', font=('Holy Friday', 14)).grid(column=0, row=6, pady=15)

        Entry(self.frame2, textvariable=self.codigo, font=('Holy Friday', 12)).grid(column=1, row=1, padx=5)
        Entry(self.frame2, textvariable=self.nombreEst, font=('Holy Friday', 12)).grid(column=1, row=2)
        Entry(self.frame2, textvariable=self.apellidoEst, font=('Holy Friday', 12)).grid(column=1, row=3)
        Entry(self.frame2, textvariable=self.gradoEst, font=('Holy Friday', 12)).grid(column=1, row=4)
        Entry(self.frame2, textvariable=self.edadEst, font=('Holy Friday', 12)).grid(column=1, row=5)
        Entry(self.frame2, textvariable=self.telEst, font=('Holy Friday', 12)).grid(column=1, row=6)

        Label(self.frame4, text='Control', fg='white', bg='black', font=('Holy Friday', 13)).grid(columnspan=3, column=0, row=0, pady=1, padx=4)
        Button(self.frame4, command=self.agregar_datos, text='REGISTRAR', font=('Holy Friday', 11), bg='#fdffb6').grid(column=0, row=1, pady=10, padx=4)
        Button(self.frame4, command=self.limpiar_datos, text='LIMPIAR', font=('Holy Friday', 11), bg='#ffc6ff').grid(column=1, row=1, padx=10)
        Button(self.frame4, command=self.eliminar_fila, text='ELIMINAR', font=('Holy Friday', 11), bg='#fdffb6').grid(column=2, row=1, padx=4)

        Button(self.frame4, command=self.buscar_nombre, text='BUSCAR POR NOMBRE', font=('Holy Friday', 10), bg='#ed7656').grid(columnspan=2, column=1, row=2)
        Entry(self.frame4, textvariable=self.buscar, font=('Arial', 12), width=10).grid(column=0, row=2, pady=1, padx=8)

        Button(self.frame4, command=self.buscar_codigo, text='BUSCAR POR CÓDIGO', font=('Holy Friday', 10), bg='#ed7656').grid(columnspan=2, column=1, row=3, pady=10)
        Entry(self.frame4, textvariable=self.buscarCod, font=('Arial', 12), width=10).grid(column=0, row=3, pady=1, padx=8)

        Button(self.frame4, command=self.mostrar_todo, text='MOSTRAR DATOS', font=('Holy Friday', 10),  bg='#caffbf').grid(columnspan=2, column=0, row=4, pady=8, padx=4)
        Button(self.frame4, text='EXCEL', font=('Holy Friday', 10), bg='#caffbf').grid(columnspan=2, column=1, row=4, pady=8, padx=4)
        #Button(self.frame4, command=self.sacarExcel, text='EXCEL', font=('Holy Friday', 10), bg='#caffbf').grid(columnspan=2, column=1, row=4, pady=8, padx=4)
        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient=HORIZONTAL, command=self.tabla.xview)
        ladox.grid(column=0, row=1, sticky='ew')
        ladoy = Scrollbar(self.frame3, orient=VERTICAL, command=self.tabla.yview)
        ladoy.grid(column=1, row=0, sticky='ns')

        self.tabla.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

        self.tabla['columns'] = ('Nombre', 'Apellido', 'Grado', 'Edad', 'Teléfono')


        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130, anchor='center')
        self.tabla.column('Apellido', minwidth=100, width=120, anchor='center')
        self.tabla.column('Grado', minwidth=100, width=120, anchor='center')
        self.tabla.column('Edad', minwidth=100, width=105, anchor='center')
        self.tabla.column('Teléfono', minwidth=100, width=130, anchor='center')

        self.tabla.heading('#0', text='Codigo', anchor='center')
        self.tabla.heading('Nombre', text='Nombre', anchor='center')
        self.tabla.heading('Apellido', text='Apellido', anchor='center')
        self.tabla.heading('Grado', text='Grado', anchor='center')
        self.tabla.heading('Edad', text='Edad', anchor='center')
        self.tabla.heading('Teléfono', text='Teléfono', anchor='center')

        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt')  # ('clam', 'alt', 'default', 'classic')

        estilo.configure("Treeview.Heading", font=('Holy Friday', 10))

        estilo.configure(".", font=('Holy Friday', 12, 'bold'), foreground='black')
        estilo.configure("Treeview", font=('Holy Friday', 10, 'bold'), foreground='black', background='white')
        estilo.map('Treeview', background=[('selected', '#D3D3D3')], foreground=[('selected', 'black')])

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila


    #def exportar_a_excel(self):
     #   datos = self.base_datos.mostrar_estudiante()  # Llama a la función para obtener todos los estudiantes

      #  columnas = ['ID', 'Código', 'Nombre', 'Apellido', 'Grado', 'Edad', 'Teléfono']
       # df = pd.DataFrame(datos, columns=columnas)

        #df_filtered = df.iloc[:, 1:]  # Esto excluye la columna ID

        #file_path = os.path.expanduser("~/Desktop/datos_exportados.xlsx")

        #df_filtered.to_excel(file_path, index=False)
        #print(f"Datos exportados a {file_path}")



    def busca_codigoEst(self, codigo):
        query = "SELECT * FROM estudiante WHERE codigoEst = %s"  # Búsqueda por código
        cur = self.conn.cursor()
        self.cursor.execute(query, (codigo,))
        return self.cursor.fetchall()


    def buscar_codigo(self):
        codigo = self.buscarCod.get()  # Obtener el valor del código
        resultado = self.base_datos.busca_codigoEst(codigo)
        self.tabla.delete(*self.tabla.get_children())  # Limpiar la tabla antes de mostrar resultados
        for i, dato in enumerate(resultado):
            self.tabla.insert('', i, text=dato[1], values=dato[2:7])



    def buscar_nombre(self):
        nombre_estudiante = self.buscar.get()
        nombre_buscado = self.base_datos.busca_estudiante(nombre_estudiante)
        self.tabla.delete(*self.tabla.get_children())
        for i, dato in enumerate(nombre_buscado):
            self.tabla.insert('', i, text=dato[1], values=dato[2:7])  # Incluye el teléfono en los valores

    def busca_estudiante(self, nombre_estudiante):
        # Cambia la consulta SQL para usar un parámetro
        query = "SELECT * FROM estudiante WHERE nombreEst = %s"
        self.cursor.execute(query, (nombre_estudiante,))
        return self.cursor.fetchall()




    def agregar_datos(self):
        codigo = self.codigo.get()
        nombre = self.nombreEst.get()
        apellido = self.apellidoEst.get()
        grado = self.gradoEst.get()
        edad = self.edadEst.get()
        telefono = self.telEst.get()
        datos = (nombre, apellido, grado, edad, telefono)
        if codigo and nombre and apellido and grado and edad and telefono != '':
            self.tabla.insert('', 0, text=codigo, values=datos)
            self.base_datos.inserta_estudiante(codigo, nombre, apellido, grado, edad, telefono)

    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.codigo.set('')
        self.nombreEst.set('')
        self.apellidoEst.set('')
        self.gradoEst.set('')
        self.edadEst.set('')
        self.telEst.set('')



    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_estudiante()
        for i, dato in enumerate(registro):
            self.tabla.insert('', i, text=dato[1], values=dato[2:7])  # Incluye el teléfono en los valores



    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")
            self.base_datos.elimina_estudiante(nombre)

    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]


def main_conexion_dialogue():
    ventana = Tk()
    ventana.wm_title("Gestion de estudiantes")
    ventana.config(bg='gray22')
    ventana.geometry('1050x750')
    ventana.resizable(0, 0)
    app = Registro(ventana)
    app.mainloop()


#if __name__=="__main__":
 #   main()