from PyQt6.QtWidgets import QMessageBox
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

import mysql.connector
from random import randint
from datetime import datetime


class Ui_StudentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(563, 635)
        self.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: qlineargradient(spread:pad, x1:0.0340909, y1:1, x2:1, y2:0, stop:0.295455 rgba(79, 130, 130, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"\n"
"QWidget{\n"
"		font: 15pt \"Holy Friday\";\n"
"		color: black;\n"
"}")
        self.cancel_button = QPushButton(self)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(350, 560, 181, 41))
        self.cancel_button.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(211, 211, 211);\n"
"font: 14pt \"Holy Friday\";\n"
"color: black;\n"
"")
        icon = QIcon()
        icon.addFile(u":/Men\u00fa/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_button.setIcon(icon)
        self.cancel_button.setIconSize(QSize(25, 25))
        self.add_button = QPushButton(self)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(150, 560, 181, 41))
        self.add_button.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.add_button.setIcon(icon)
        self.add_button.setIconSize(QSize(25, 25))
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 50, 311, 31))
        self.label.setStyleSheet(u"font: 22pt \"Holy Friday\";")
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 110, 507, 69))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setFamilies([u"Holy Friday"])
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.label_13.setFont(font)

        self.verticalLayout_13.addWidget(self.label_13)

        self.name_lineEdit = QLineEdit(self.layoutWidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.name_lineEdit.setStyleSheet(u"border-radius:15px;\n"
"color: black;\n"
"")

        self.verticalLayout_13.addWidget(self.name_lineEdit)

        self.layoutWidget_2 = QWidget(self)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(40, 180, 497, 368))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.lastname_lineEdit = QLineEdit(self.layoutWidget_2)
        self.lastname_lineEdit.setObjectName(u"lastname_lineEdit")
        self.lastname_lineEdit.setMinimumSize(QSize(0, 35))
        self.lastname_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.lastname_lineEdit.setStyleSheet(u"border-radius:15px;\n"
"color: black;\n"
"")

        self.verticalLayout.addWidget(self.lastname_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_8.addWidget(self.label_9)

        self.gender_comboBox = QComboBox(self.layoutWidget_2)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")
        self.gender_comboBox.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.gender_comboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.layoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_9.addWidget(self.label_10)

        self.class_comboBox = QComboBox(self.layoutWidget_2)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")
        self.class_comboBox.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.class_comboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.layoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.verticalLayout_10.addWidget(self.label_11)

        self.date_dateEdit = QDateEdit(self.layoutWidget_2)
        self.date_dateEdit.setObjectName(u"date_dateEdit")
        self.date_dateEdit.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.date_dateEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_10)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_5.addWidget(self.label_6)

        self.id_lineEdit = QLineEdit(self.layoutWidget_2)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setMinimumSize(QSize(0, 35))
        self.id_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.id_lineEdit.setStyleSheet(u"border-radius:15px;\n"
"color: black;\n"
"")

        self.verticalLayout_5.addWidget(self.id_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_6.addWidget(self.label_7)

        self.tel_lineEdit = QLineEdit(self.layoutWidget_2)
        self.tel_lineEdit.setObjectName(u"tel_lineEdit")
        self.tel_lineEdit.setMinimumSize(QSize(0, 35))
        self.tel_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.tel_lineEdit.setStyleSheet(u"border-radius:15px;\n"
"color: black;\n"
"")

        self.verticalLayout_6.addWidget(self.tel_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_7.addWidget(self.label_8)

        self.email_lineEdit = QLineEdit(self.layoutWidget_2)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.email_lineEdit.setStyleSheet(u"border-radius:15px;\n"
"color: black;\n"
"")

        self.verticalLayout_7.addWidget(self.email_lineEdit)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Dialog", None))
        self.cancel_button.setText(QCoreApplication.translate("StudentsDialog", u"Cancelar", None))
        self.add_button.setText(QCoreApplication.translate("StudentsDialog", u"A\u00f1adir estudiante", None))
        self.label.setText(QCoreApplication.translate("StudentsDialog", u"A\u00f1adir nuevo estudiante", None))
        self.label_13.setText(QCoreApplication.translate("StudentsDialog", u"Nombre", None))
        self.name_lineEdit.setText("")
        self.label_3.setText(QCoreApplication.translate("StudentsDialog", u"Apellidos", None))
        self.lastname_lineEdit.setText("")
        self.label_9.setText(QCoreApplication.translate("StudentsDialog", u"Seleccionar Genero", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Masculino", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Femenino", None))

        self.label_10.setText(QCoreApplication.translate("StudentsDialog", u"Seleccionar Grado", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grado...", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"11-3", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentsDialog", u"11-2", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentsDialog", u"11-1", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentsDialog", u"10-3", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentsDialog", u"10-2", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentsDialog", u"10-1", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StudentsDialog", u"9-3", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StudentsDialog", u"9-2", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StudentsDialog", u"9-1", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StudentsDialog", u"8-3", None))

        self.label_11.setText(QCoreApplication.translate("StudentsDialog", u"Fecha De Nacimiento", None))
        self.label_6.setText(QCoreApplication.translate("StudentsDialog", u" Id", None))
        self.id_lineEdit.setText("")
        self.label_7.setText(QCoreApplication.translate("StudentsDialog", u"Numero De Telefono", None))
        self.label_8.setText(QCoreApplication.translate("StudentsDialog", u"Email", None))
    # retranslateUi


        self.add_button.clicked.connect(self.add_student) #El añadir estudiante del formulario
        self.cancel_button.clicked.connect(self.close)


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

    def insert_new_student(self):
        try:
            cursor = self.create_connection().cursor()
            gender = self.gender_comboBox.currentText()
            student_id = self.generate_studentId(gender)

            edad_est = self.handleDateChange()

            birth_date = self.dob_dateEdit.date()
            age = self.calculate_age(birth_date)

            self.new_student = [
                self.name_lineEdit.text(),
                student_id,
                self.gender_comboBox.currentText(),
                self.class_comboBox.currentText(),
                edad_est,
                age,
                self.direc_est_lineEdit.text(),
                self.tel_est_lineEdit.text(),
                self.email_lineEdit.text()
            ]

            insert_student_query = f"""INSERT INTO estudiante (id_est, apelli_est, nom_est, grad_est, edad_est, sexo_est, direc_est, tel_est, email_est ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            cursor.execute(insert_student_query, self.new_student)
            self.mydb.commit()
            self.mydb.close

        except mysql.connector.Error as err:
            print(f"Error: {err}")



    def generate_studentId(self, gender):
        cursor = self.create_connection().cursor()

        while True:
            if gender == "Male":
                id_start_value = '24' + '/U/M'
            else:
                id_start_value = '24' + '/U/M'

            random_value = self.generate_randomNumber()
            student_id = id_start_value + random_value

            cursor.execute(f"SELECT id_est FROM estudiante WHERE id_est = %s", (student_id))
            existing_id = cursor.fetchone()

            if not existing_id:
                return student_id


    def generate_randomNumber(self):
        number = randint(1,100)
        random_number = f"{number:04d}"
        return random_number

    def handleDataChange(self):
        selected_date = self.dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)

        return selected_date

    def calculate_age(self, birth_date):
        current_date = datetime.now().date()
        birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day()).date()

        age = current_date.year - birth_date.year

        if (current_date.moth, current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1
        return age

    def show_inserted_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Exitoso")
        msg_box.setText(self.name_lineEdit.text() + "Insertado en la base de datos")
        msg_box.exec()

    def add_student(self):
        self.insert_new_student()
        self.accept()