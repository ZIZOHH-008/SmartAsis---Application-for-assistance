from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import recursos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1271, 711)
        MainWindow.setMinimumSize(QSize(1271, 711))
        MainWindow.setMaximumSize(QSize(1271, 711))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setGeometry(QRect(0, 0, 91, 711))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(62, 62, 62);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.salir1 = QPushButton(self.icon_only_widget)
        self.salir1.setObjectName(u"salir1")
        self.salir1.setGeometry(QRect(20, 650, 51, 41))
        self.salir1.setStyleSheet(u"border-radius:15px;")
        icon = QIcon()
        icon.addFile(u":/Principal/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/Principal/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.salir1.setIcon(icon)
        self.salir1.setIconSize(QSize(30, 30))
        self.salir1.setCheckable(True)
        self.salir1.setAutoExclusive(True)
        self.dashboard1 = QPushButton(self.icon_only_widget)
        self.dashboard1.setObjectName(u"dashboard1")
        self.dashboard1.setGeometry(QRect(20, 170, 52, 38))
        self.dashboard1.setStyleSheet(u"border-radius:15px;\n"
"\n"
"QPushButton {\n"
"    border-radius: 15px;\n"
"    font: 12pt \"Holy Friday\";\n"
"    padding-left: 0px; \n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    border-radius: 3px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Principal/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/Principal/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard1.setIcon(icon1)
        self.dashboard1.setIconSize(QSize(30, 30))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setChecked(False)
        self.dashboard1.setAutoRepeat(False)
        self.dashboard1.setAutoExclusive(True)
        self.ajustes1 = QPushButton(self.icon_only_widget)
        self.ajustes1.setObjectName(u"ajustes1")
        self.ajustes1.setGeometry(QRect(20, 410, 52, 38))
        self.ajustes1.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        icon2 = QIcon()
        icon2.addFile(u":/Principal/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/Principal/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.ajustes1.setIcon(icon2)
        self.ajustes1.setIconSize(QSize(30, 30))
        self.ajustes1.setCheckable(True)
        self.ajustes1.setAutoExclusive(True)
        self.institucion1 = QPushButton(self.icon_only_widget)
        self.institucion1.setObjectName(u"institucion1")
        self.institucion1.setGeometry(QRect(20, 330, 52, 38))
        self.institucion1.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        icon3 = QIcon()
        icon3.addFile(u":/Principal/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/Principal/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institucion1.setIcon(icon3)
        self.institucion1.setIconSize(QSize(40, 40))
        self.institucion1.setCheckable(True)
        self.institucion1.setAutoExclusive(True)
        self.label_2 = QLabel(self.icon_only_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 51, 51))
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/Principal/logo_colegio.jpg"))
        self.label_2.setScaledContents(True)
        self.perfil1 = QPushButton(self.icon_only_widget)
        self.perfil1.setObjectName(u"perfil1")
        self.perfil1.setGeometry(QRect(20, 480, 52, 38))
        self.perfil1.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        icon4 = QIcon()
        icon4.addFile(u":/Principal/teacherssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/Principal/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.perfil1.setIcon(icon4)
        self.perfil1.setIconSize(QSize(32, 32))
        self.perfil1.setCheckable(True)
        self.perfil1.setAutoExclusive(True)
        self.gestion1 = QPushButton(self.icon_only_widget)
        self.gestion1.setObjectName(u"gestion1")
        self.gestion1.setGeometry(QRect(20, 250, 52, 38))
        self.gestion1.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        icon5 = QIcon()
        icon5.addFile(u":/Principal/logosmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/Principal/logosmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.gestion1.setIcon(icon5)
        self.gestion1.setIconSize(QSize(40, 40))
        self.gestion1.setCheckable(True)
        self.gestion1.setAutoExclusive(True)
        self.info_smart1 = QPushButton(self.icon_only_widget)
        self.info_smart1.setObjectName(u"info_smart1")
        self.info_smart1.setGeometry(QRect(20, 550, 52, 38))
        self.info_smart1.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        icon6 = QIcon()
        icon6.addFile(u":/Principal/informacion.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_smart1.setIcon(icon6)
        self.info_smart1.setIconSize(QSize(32, 32))
        self.info_smart1.setCheckable(True)
        self.info_smart1.setAutoExclusive(True)
        self.icon_text_widget = QWidget(self.centralwidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setGeometry(QRect(100, 0, 171, 721))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(62, 62, 62);\n"
"	color:black;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.salir2 = QPushButton(self.icon_text_widget)
        self.salir2.setObjectName(u"salir2")
        self.salir2.setGeometry(QRect(20, 650, 131, 41))
        self.salir2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        self.salir2.setIcon(icon)
        self.salir2.setIconSize(QSize(30, 30))
        self.salir2.setCheckable(True)
        self.ajustes2 = QPushButton(self.icon_text_widget)
        self.ajustes2.setObjectName(u"ajustes2")
        self.ajustes2.setGeometry(QRect(20, 410, 131, 41))
        self.ajustes2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        self.ajustes2.setIcon(icon2)
        self.ajustes2.setIconSize(QSize(30, 30))
        self.ajustes2.setCheckable(True)
        self.ajustes2.setAutoExclusive(True)
        self.dashboard2 = QPushButton(self.icon_text_widget)
        self.dashboard2.setObjectName(u"dashboard2")
        self.dashboard2.setGeometry(QRect(20, 170, 131, 38))
        self.dashboard2.setMouseTracking(False)
        self.dashboard2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";\n"
"\n"
"QPushButton {\n"
"    border-radius: 15px;\n"
"    font: 12pt \"Holy Friday\";\n"
"    padding-left: 0px; \n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	 color:rgb(21, 101, 51);\n"
"}")
        self.dashboard2.setIcon(icon1)
        self.dashboard2.setIconSize(QSize(30, 30))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)
        self.institucion2 = QPushButton(self.icon_text_widget)
        self.institucion2.setObjectName(u"institucion2")
        self.institucion2.setGeometry(QRect(20, 330, 131, 38))
        self.institucion2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        self.institucion2.setIcon(icon3)
        self.institucion2.setIconSize(QSize(40, 40))
        self.institucion2.setCheckable(True)
        self.institucion2.setAutoExclusive(True)
        self.perfil2 = QPushButton(self.icon_text_widget)
        self.perfil2.setObjectName(u"perfil2")
        self.perfil2.setGeometry(QRect(20, 480, 131, 38))
        self.perfil2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        self.perfil2.setIcon(icon4)
        self.perfil2.setIconSize(QSize(32, 32))
        self.perfil2.setCheckable(True)
        self.perfil2.setAutoExclusive(True)
        self.label_7 = QLabel(self.icon_text_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 10, 121, 131))
        self.label_7.setMinimumSize(QSize(40, 40))
        self.label_7.setPixmap(QPixmap(u":/Principal/Logo app.png"))
        self.label_7.setScaledContents(True)
        self.gestion2 = QPushButton(self.icon_text_widget)
        self.gestion2.setObjectName(u"gestion2")
        self.gestion2.setGeometry(QRect(20, 250, 131, 38))
        self.gestion2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        self.gestion2.setIcon(icon5)
        self.gestion2.setIconSize(QSize(40, 40))
        self.gestion2.setCheckable(True)
        self.gestion2.setAutoExclusive(True)
        self.info_smart2 = QPushButton(self.icon_text_widget)
        self.info_smart2.setObjectName(u"info_smart2")
        self.info_smart2.setGeometry(QRect(20, 550, 131, 38))
        self.info_smart2.setStyleSheet(u"border-radius:15px;\n"
"font: 12pt \"Holy Friday\";")
        self.info_smart2.setIcon(icon6)
        self.info_smart2.setIconSize(QSize(32, 32))
        self.info_smart2.setCheckable(True)
        self.info_smart2.setAutoExclusive(True)
        self.main_screen_widget = QWidget(self.centralwidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setGeometry(QRect(290, 180, 981, 531))
        self.main_screen_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(101, 127, 0, 255)\n"
"}")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 961, 531))
        self.stackedWidget.setMaximumSize(QSize(961, 16777215))
        self.gestion_pag = QWidget()
        self.gestion_pag.setObjectName(u"gestion_pag")
        self.usegestion_2 = QPushButton(self.gestion_pag)
        self.usegestion_2.setObjectName(u"usegestion_2")
        self.usegestion_2.setGeometry(QRect(160, 330, 251, 41))
        self.usegestion_2.setStyleSheet(u"border: 4px solid black;\n"
"border-radius: 20px;\n"
"background-color: rgb(224, 196, 24);\n"
"font: 16pt \"Holy Friday\";\n"
"color:black;\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/Principal/add student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.usegestion_2.setIcon(icon7)
        self.usegestion_2.setIconSize(QSize(25, 25))
        self.usegestion_2.setCheckable(True)
        self.label_8 = QLabel(self.gestion_pag)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(190, 100, 191, 191))
        self.label_8.setMinimumSize(QSize(40, 40))
        self.label_8.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.label_8.setPixmap(QPixmap(u":/Principal/gestion 2.png"))
        self.label_8.setScaledContents(True)
        self.label_9 = QLabel(self.gestion_pag)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 30, 511, 31))
        self.label_9.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(211, 211, 211);\n"
"font: 25pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"")
        self.label_10 = QLabel(self.gestion_pag)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(600, 100, 191, 191))
        self.label_10.setMinimumSize(QSize(40, 40))
        self.label_10.setStyleSheet(u"border-radius:95px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.label_10.setPixmap(QPixmap(u":/Principal/asistencia_logo.png"))
        self.label_10.setScaledContents(True)
        self.asistencia_2 = QFrame(self.gestion_pag)
        self.asistencia_2.setObjectName(u"asistencia_2")
        self.asistencia_2.setGeometry(QRect(570, 320, 251, 151))
        self.asistencia_2.setStyleSheet(u"QWidget#centralwidget{\n"
"	background-color: \n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.asistencia_2.setFrameShape(QFrame.StyledPanel)
        self.asistencia_2.setFrameShadow(QFrame.Raised)
        self.useasistencia_2 = QPushButton(self.asistencia_2)
        self.useasistencia_2.setObjectName(u"useasistencia_2")
        self.useasistencia_2.setGeometry(QRect(0, 10, 241, 41))
        self.useasistencia_2.setStyleSheet(u"border: 4px solid black;\n"
"border-radius: 20px;\n"
"background-color: rgb(224, 196, 24);\n"
"font: 16pt \"Holy Friday\";\n"
"color:black;\n"
"\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/Principal/despliegue.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/Principal/despliegue2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.useasistencia_2.setIcon(icon8)
        self.useasistencia_2.setCheckable(True)
        self.layoutWidget = QWidget(self.asistencia_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 191, 91))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.resgistrar_asis_2 = QPushButton(self.layoutWidget)
        self.resgistrar_asis_2.setObjectName(u"resgistrar_asis_2")
        self.resgistrar_asis_2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(224, 196, 24);\n"
"font: 16pt \"Holy Friday\";\n"
"color:white;\n"
"\n"
"")
        self.resgistrar_asis_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.resgistrar_asis_2)

        self.ver_asis_2 = QPushButton(self.layoutWidget)
        self.ver_asis_2.setObjectName(u"ver_asis_2")
        self.ver_asis_2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 10px;\n"
"background-color: rgb(224, 196, 24);\n"
"font: 16pt \"Holy Friday\";\n"
"color:white;\n"
"\n"
"")
        self.ver_asis_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.ver_asis_2)

        self.stackedWidget.addWidget(self.gestion_pag)
        self.institu_pag = QWidget()
        self.institu_pag.setObjectName(u"institu_pag")
        self.label_3 = QLabel(self.institu_pag)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 150, 241, 51))
        self.label_3.setStyleSheet(u"font: 20pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_6 = QLabel(self.institu_pag)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 80, 221, 41))
        self.label_6.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_5 = QLabel(self.institu_pag)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 40, 281, 41))
        self.label_5.setStyleSheet(u"font: 20pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_4 = QLabel(self.institu_pag)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(440, 40, 171, 171))
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setStyleSheet(u"border: 4px solid rgb(253, 214, 0);")
        self.label_4.setPixmap(QPixmap(u":/Principal/logo_colegio.jpg"))
        self.label_4.setScaledContents(True)
        self.label_11 = QLabel(self.institu_pag)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(610, 240, 281, 191))
        self.label_11.setMinimumSize(QSize(40, 40))
        self.label_11.setStyleSheet(u"border: 4px solid rgb(253, 214, 0);")
        self.label_11.setPixmap(QPixmap(u":/Principal/colegio.jpeg"))
        self.label_11.setScaledContents(True)
        self.label_18 = QLabel(self.institu_pag)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 390, 221, 41))
        self.label_18.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_19 = QLabel(self.institu_pag)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 350, 281, 41))
        self.label_19.setStyleSheet(u"font: 20pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.layoutWidget1 = QWidget(self.institu_pag)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(51, 200, 242, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setFamilies([u"Holy Friday"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label_13)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        font1 = QFont()
        font1.setFamilies([u"Holy Friday"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(False)
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.label_15)

        self.layoutWidget2 = QWidget(self.institu_pag)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 240, 327, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.label_16 = QLabel(self.layoutWidget2)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setFamilies([u"Holy Friday"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.label_16)

        self.layoutWidget3 = QWidget(self.institu_pag)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(50, 280, 261, 33))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_14)

        self.label_17 = QLabel(self.layoutWidget3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.label_17)

        self.stackedWidget.addWidget(self.institu_pag)
        self.ajustes_pag = QWidget()
        self.ajustes_pag.setObjectName(u"ajustes_pag")
        self.label_20 = QLabel(self.ajustes_pag)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(60, 90, 681, 51))
        self.label_20.setStyleSheet(u"font: 30pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_21 = QLabel(self.ajustes_pag)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(70, 150, 441, 61))
        self.label_21.setStyleSheet(u"font: 30pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.stackedWidget.addWidget(self.ajustes_pag)
        self.perfil_pag = QWidget()
        self.perfil_pag.setObjectName(u"perfil_pag")
        self.label_22 = QLabel(self.perfil_pag)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(290, 200, 391, 41))
        self.label_22.setStyleSheet(u"font: 18pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_23 = QLabel(self.perfil_pag)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 150, 281, 41))
        self.label_23.setStyleSheet(u"font: 20pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.stackedWidget.addWidget(self.perfil_pag)
        self.estudian_pag = QWidget()
        self.estudian_pag.setObjectName(u"estudian_pag")
        self.registros_tableWidget = QTableWidget(self.estudian_pag)
        if (self.registros_tableWidget.columnCount() < 9):
            self.registros_tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.registros_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.registros_tableWidget.setObjectName(u"registros_tableWidget")
        self.registros_tableWidget.setGeometry(QRect(30, 190, 901, 331))
        self.registros_tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color: black;\n"
"	color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: black;\n"
"	background-color: white;\n"
"\n"
"}")
        self.registros_tableWidget.setAlternatingRowColors(True)
        self.grado_comboBox = QComboBox(self.estudian_pag)
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.addItem("")
        self.grado_comboBox.setObjectName(u"grado_comboBox")
        self.grado_comboBox.setGeometry(QRect(270, 110, 151, 51))
        self.grado_comboBox.setStyleSheet(u"QComboBox{\n"
"border: 2px solid white;\n"
"border-radius: 8px;\n"
"padding: 1px 18px 1px 3px;\n"
"background-color: black;\n"
"color: white;\n"
"height: 35px;\n"
"padding-left: 15px;\n"
"font-weight: bold;\n"
"selection-background-color: #298089;\n"
"font: 14pt \"Holy Friday\";\n"
"}")
        self.excel_Button = QPushButton(self.estudian_pag)
        self.excel_Button.setObjectName(u"excel_Button")
        self.excel_Button.setGeometry(QRect(640, 30, 231, 51))
        self.excel_Button.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/Principal/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.excel_Button.setIcon(icon9)
        self.excel_Button.setIconSize(QSize(25, 25))
        self.excel_Button.setCheckable(True)
        self.pdf_Button = QPushButton(self.estudian_pag)
        self.pdf_Button.setObjectName(u"pdf_Button")
        self.pdf_Button.setGeometry(QRect(350, 30, 231, 51))
        self.pdf_Button.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/Principal/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdf_Button.setIcon(icon10)
        self.pdf_Button.setIconSize(QSize(25, 25))
        self.pdf_Button.setCheckable(True)
        self.genero_comboBox = QComboBox(self.estudian_pag)
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.addItem("")
        self.genero_comboBox.setObjectName(u"genero_comboBox")
        self.genero_comboBox.setGeometry(QRect(90, 110, 151, 51))
        self.genero_comboBox.setStyleSheet(u"QComboBox{\n"
"border: 2px solid white;\n"
"border-radius: 8px;\n"
"padding: 1px 18px 1px 3px;\n"
"background-color: black;\n"
"color: white;\n"
"height: 35px;\n"
"padding-left: 15px;\n"
"font-weight: bold;\n"
"selection-background-color: #298089;\n"
"font: 14pt \"Holy Friday\";\n"
"}\n"
"\n"
"")
        self.buscar_lineEdit = QLineEdit(self.estudian_pag)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")
        self.buscar_lineEdit.setGeometry(QRect(470, 120, 361, 41))
        font3 = QFont()
        font3.setFamilies([u"Holy Friday"])
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        self.buscar_lineEdit.setFont(font3)
        self.buscar_lineEdit.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Holy Friday\";\n"
"color: rgb(115, 115, 115);")
        self.add_Button = QPushButton(self.estudian_pag)
        self.add_Button.setObjectName(u"add_Button")
        self.add_Button.setGeometry(QRect(70, 30, 231, 51))
        self.add_Button.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 15pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.add_Button.setIcon(icon7)
        self.add_Button.setIconSize(QSize(25, 25))
        self.add_Button.setCheckable(True)
        self.stackedWidget.addWidget(self.estudian_pag)
        self.registrarAsis = QWidget()
        self.registrarAsis.setObjectName(u"registrarAsis")
        self.excel_Button_2 = QPushButton(self.registrarAsis)
        self.excel_Button_2.setObjectName(u"excel_Button_2")
        self.excel_Button_2.setGeometry(QRect(640, 70, 231, 51))
        self.excel_Button_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.excel_Button_2.setIcon(icon9)
        self.excel_Button_2.setIconSize(QSize(25, 25))
        self.excel_Button_2.setCheckable(True)
        self.pdf_Button_2 = QPushButton(self.registrarAsis)
        self.pdf_Button_2.setObjectName(u"pdf_Button_2")
        self.pdf_Button_2.setGeometry(QRect(350, 70, 231, 51))
        self.pdf_Button_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.pdf_Button_2.setIcon(icon10)
        self.pdf_Button_2.setIconSize(QSize(25, 25))
        self.pdf_Button_2.setCheckable(True)
        self.add_Button_2 = QPushButton(self.registrarAsis)
        self.add_Button_2.setObjectName(u"add_Button_2")
        self.add_Button_2.setGeometry(QRect(60, 70, 231, 51))
        self.add_Button_2.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 15pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.add_Button_2.setIcon(icon7)
        self.add_Button_2.setIconSize(QSize(25, 25))
        self.add_Button_2.setCheckable(True)
        self.registros_tableWidget_2 = QTableWidget(self.registrarAsis)
        if (self.registros_tableWidget_2.columnCount() < 9):
            self.registros_tableWidget_2.setColumnCount(9)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.registros_tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        self.registros_tableWidget_2.setObjectName(u"registros_tableWidget_2")
        self.registros_tableWidget_2.setGeometry(QRect(30, 180, 901, 301))
        self.registros_tableWidget_2.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color: black;\n"
"	color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: black;\n"
"	background-color: white;\n"
"\n"
"}")
        self.registros_tableWidget_2.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.registrarAsis)
        self.verAsis = QWidget()
        self.verAsis.setObjectName(u"verAsis")
        self.genero_comboBox_3 = QComboBox(self.verAsis)
        self.genero_comboBox_3.addItem("")
        self.genero_comboBox_3.addItem("")
        self.genero_comboBox_3.addItem("")
        self.genero_comboBox_3.setObjectName(u"genero_comboBox_3")
        self.genero_comboBox_3.setGeometry(QRect(80, 110, 151, 51))
        self.genero_comboBox_3.setStyleSheet(u"QComboBox{\n"
"border: 2px solid white;\n"
"border-radius: 8px;\n"
"padding: 1px 18px 1px 3px;\n"
"background-color: black;\n"
"color: white;\n"
"height: 35px;\n"
"padding-left: 15px;\n"
"font-weight: bold;\n"
"selection-background-color: #298089;\n"
"font: 14pt \"Holy Friday\";\n"
"}\n"
"\n"
"")
        self.excel_Button_3 = QPushButton(self.verAsis)
        self.excel_Button_3.setObjectName(u"excel_Button_3")
        self.excel_Button_3.setGeometry(QRect(630, 30, 231, 51))
        self.excel_Button_3.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.excel_Button_3.setIcon(icon9)
        self.excel_Button_3.setIconSize(QSize(25, 25))
        self.excel_Button_3.setCheckable(True)
        self.grado_comboBox_3 = QComboBox(self.verAsis)
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.addItem("")
        self.grado_comboBox_3.setObjectName(u"grado_comboBox_3")
        self.grado_comboBox_3.setGeometry(QRect(260, 110, 151, 51))
        self.grado_comboBox_3.setStyleSheet(u"QComboBox{\n"
"border: 2px solid white;\n"
"border-radius: 8px;\n"
"padding: 1px 18px 1px 3px;\n"
"background-color: black;\n"
"color: white;\n"
"height: 35px;\n"
"padding-left: 15px;\n"
"font-weight: bold;\n"
"selection-background-color: #298089;\n"
"font: 14pt \"Holy Friday\";\n"
"}")
        self.pdf_Button_3 = QPushButton(self.verAsis)
        self.pdf_Button_3.setObjectName(u"pdf_Button_3")
        self.pdf_Button_3.setGeometry(QRect(340, 30, 231, 51))
        self.pdf_Button_3.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(21, 101, 51);\n"
"font: 14pt \"Holy Friday\";\n"
"color: white;\n"
"")
        self.pdf_Button_3.setIcon(icon10)
        self.pdf_Button_3.setIconSize(QSize(25, 25))
        self.pdf_Button_3.setCheckable(True)
        self.buscar_lineEdit_3 = QLineEdit(self.verAsis)
        self.buscar_lineEdit_3.setObjectName(u"buscar_lineEdit_3")
        self.buscar_lineEdit_3.setGeometry(QRect(450, 120, 361, 41))
        self.buscar_lineEdit_3.setFont(font3)
        self.buscar_lineEdit_3.setStyleSheet(u"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"font: 15pt \"Holy Friday\";\n"
"color: rgb(115, 115, 115);")
        self.registros_tableWidget_3 = QTableWidget(self.verAsis)
        if (self.registros_tableWidget_3.columnCount() < 9):
            self.registros_tableWidget_3.setColumnCount(9)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.registros_tableWidget_3.setHorizontalHeaderItem(8, __qtablewidgetitem26)
        self.registros_tableWidget_3.setObjectName(u"registros_tableWidget_3")
        self.registros_tableWidget_3.setGeometry(QRect(30, 190, 901, 301))
        self.registros_tableWidget_3.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight:bold;\n"
"	background-color: black;\n"
"	color:white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: black;\n"
"	background-color: white;\n"
"\n"
"}")
        self.registros_tableWidget_3.setAlternatingRowColors(True)
        self.stackedWidget.addWidget(self.verAsis)
        self.infoSmart = QWidget()
        self.infoSmart.setObjectName(u"infoSmart")
        self.label_24 = QLabel(self.infoSmart)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(50, 100, 481, 51))
        self.label_24.setStyleSheet(u"font: 23pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_25 = QLabel(self.infoSmart)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 220, 291, 51))
        self.label_25.setStyleSheet(u"font: 25pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_26 = QLabel(self.infoSmart)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(50, 60, 361, 51))
        self.label_26.setStyleSheet(u"font: 25pt \"Holy Friday\";\n"
"color: rgb(45, 94, 52);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_27 = QLabel(self.infoSmart)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(660, 30, 221, 251))
        self.label_27.setStyleSheet(u"font: 30pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_27.setPixmap(QPixmap(u":/Principal/Logo app.png"))
        self.label_27.setScaledContents(True)
        self.label_28 = QLabel(self.infoSmart)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(50, 270, 641, 51))
        self.label_28.setStyleSheet(u"font: 23pt \"Holy Friday\";\n"
"color: rgb(48, 79, 79);\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.label_29 = QLabel(self.infoSmart)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(50, 350, 401, 131))
        font4 = QFont()
        font4.setFamilies([u"New Easter"])
        font4.setPointSize(100)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_29.setFont(font4)
        self.label_29.setStyleSheet(u"font: 100pt \"New Easter\";\n"
"color: rgb(104, 129, 50);\n"
"\n"
"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.943, y1:0.039, x2:0, y2:1, stop:1 rgba(101, 127, 0, 255));}\n"
"\n"
"")
        self.stackedWidget.addWidget(self.infoSmart)
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setGeometry(QRect(290, 0, 991, 181))
        self.header_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(62, 62, 62);\n"
"}")
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 40, 471, 91))
        self.label.setStyleSheet(u"border: 4px solid black;\n"
"border-radius: 20px;\n"
"background-color: rgb(211, 211, 211);\n"
"font: 25pt \"Holy Friday\";\n"
"color:black;\n"
"\n"
"")
        self.pushButton_20 = QPushButton(self.header_widget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(850, 40, 81, 101))
        self.pushButton_20.setStyleSheet(u"border-radius:15px;\n"
"alternate-background-color: rgb(13, 13, 13);")
        icon11 = QIcon()
        icon11.addFile(u":/Principal/profile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_20.setIcon(icon11)
        self.pushButton_20.setIconSize(QSize(70, 70))
        self.pushButton_11 = QPushButton(self.header_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(20, 40, 81, 81))
        self.pushButton_11.setStyleSheet(u"border-radius:15px;\n"
"\n"
"QPushButton {\n"
"    border-radius: 15px;\n"
"    font: 12pt \"Holy Friday\";\n"
"    padding-left: 0px; \n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    border-radius: 3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/Principal/menu (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_11.setIcon(icon12)
        self.pushButton_11.setIconSize(QSize(60, 60))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setChecked(False)
        self.pushButton_11.setAutoRepeat(False)
        self.pushButton_11.setAutoExclusive(False)
        self.layoutWidget4 = QWidget(self.centralwidget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout = QGridLayout(self.layoutWidget4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget5 = QWidget(self.centralwidget)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(0, 0, 2, 2))
        self.gridLayout_2 = QGridLayout(self.layoutWidget5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.salir1.toggled.connect(MainWindow.close)
        self.perfil2.toggled.connect(self.perfil1.setChecked)
        self.salir2.toggled.connect(MainWindow.close)
        self.ajustes2.toggled.connect(self.ajustes1.setChecked)
        self.salir2.toggled.connect(self.salir1.setChecked)
        self.gestion2.toggled.connect(self.gestion1.setChecked)
        self.institucion2.toggled.connect(self.institucion1.setChecked)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)
        self.salir1.toggled.connect(self.salir2.setChecked)
        self.pushButton_11.toggled.connect(self.icon_text_widget.setHidden)
        self.dashboard1.toggled.connect(self.dashboard2.setChecked)
        self.gestion1.toggled.connect(self.gestion2.setChecked)
        self.institucion1.toggled.connect(self.institucion2.setChecked)
        self.ajustes1.toggled.connect(self.ajustes2.setChecked)
        self.perfil1.toggled.connect(self.perfil2.setChecked)
        self.useasistencia_2.toggled.connect(self.resgistrar_asis_2.setHidden)
        self.useasistencia_2.toggled.connect(self.ver_asis_2.setHidden)
        self.info_smart2.toggled.connect(self.info_smart1.setChecked)
        self.info_smart1.toggled.connect(self.info_smart2.setChecked)
        self.info_smart2.toggled.connect(self.info_smart1.setChecked)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.salir1.setText("")
        self.dashboard1.setText("")
        self.ajustes1.setText("")
        self.institucion1.setText("")
        self.label_2.setText("")
        self.perfil1.setText("")
        self.gestion1.setText("")
        self.info_smart1.setText("")
        self.salir2.setText(QCoreApplication.translate("MainWindow", u"Salir de la app", None))
        self.ajustes2.setText(QCoreApplication.translate("MainWindow", u"  Ajustes", None))
        self.dashboard2.setText(QCoreApplication.translate("MainWindow", u"  Iniciar sesi\u00f3n", None))
        self.institucion2.setText(QCoreApplication.translate("MainWindow", u"  Instituci\u00f3n", None))
        self.perfil2.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.label_7.setText("")
        self.gestion2.setText(QCoreApplication.translate("MainWindow", u"  Gesti\u00f3n", None))
        self.info_smart2.setText(QCoreApplication.translate("MainWindow", u"Smart Asis", None))
        self.usegestion_2.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de estudiantes", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Comencemos...", None))
        self.label_10.setText("")
        self.useasistencia_2.setText(QCoreApplication.translate("MainWindow", u"Asistencia", None))
        self.resgistrar_asis_2.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.ver_asis_2.setText(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n - Sedes", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"https://iejega.edu.co/", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"P\u00e1gina Web institucional", None))
        self.label_4.setText("")
        self.label_11.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"(602)2859784", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Central:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Calle 41 #40-41", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Antonia Santos: ", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Cra 38 # 37a-35", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Tulio Raffo:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Cl. 37a #42110", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Para avisar de errores o fallos a ajustar...", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"smartasisJDO@gmail.com", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Datos personales del docente en cuesti\u00f3n (atributos y todo eso)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"LO QUE DEBE IR", None))
        ___qtablewidgetitem = self.registros_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.registros_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem2 = self.registros_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem3 = self.registros_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Grado", None));
        ___qtablewidgetitem4 = self.registros_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem5 = self.registros_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem6 = self.registros_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem7 = self.registros_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"N\u00famero tel", None));
        ___qtablewidgetitem8 = self.registros_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.grado_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Grado...", None))
        self.grado_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"11-3", None))
        self.grado_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"11-2", None))
        self.grado_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"11-1", None))
        self.grado_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"10-1", None))
        self.grado_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"10-2", None))
        self.grado_comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"10-3", None))
        self.grado_comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"10-4", None))
        self.grado_comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"9-3", None))
        self.grado_comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"9-2", None))
        self.grado_comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"9-1", None))
        self.grado_comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"8-3", None))
        self.grado_comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"8-2", None))
        self.grado_comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"8-1", None))
        self.grado_comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"7-3", None))
        self.grado_comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"7-2", None))
        self.grado_comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"7-1", None))
        self.grado_comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"6-3", None))
        self.grado_comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"6-2", None))
        self.grado_comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"6-1", None))

        self.excel_Button.setText(QCoreApplication.translate("MainWindow", u"Exportar a Excel", None))
        self.pdf_Button.setText(QCoreApplication.translate("MainWindow", u" Exportar a PDF", None))
        self.genero_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sexo...", None))
        self.genero_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.genero_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Femenino", None))

        self.buscar_lineEdit.setText(QCoreApplication.translate("MainWindow", u"Busca Aqu\u00ed...", None))
        self.add_Button.setText(QCoreApplication.translate("MainWindow", u" A\u00f1adir estudiante", None))
        self.excel_Button_2.setText(QCoreApplication.translate("MainWindow", u"Exportar a Excel", None))
        self.pdf_Button_2.setText(QCoreApplication.translate("MainWindow", u" Exportar a PDF", None))
        self.add_Button_2.setText(QCoreApplication.translate("MainWindow", u" A\u00f1adir estudiante", None))
        ___qtablewidgetitem9 = self.registros_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem10 = self.registros_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem11 = self.registros_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem12 = self.registros_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem13 = self.registros_tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem14 = self.registros_tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Grado", None));
        ___qtablewidgetitem15 = self.registros_tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem16 = self.registros_tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"N\u00famero tel", None));
        ___qtablewidgetitem17 = self.registros_tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.genero_comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Sexo...", None))
        self.genero_comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.genero_comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Femenino", None))

        self.excel_Button_3.setText(QCoreApplication.translate("MainWindow", u"Exportar a Excel", None))
        self.grado_comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Grado...", None))
        self.grado_comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"11-3", None))
        self.grado_comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"11-2", None))
        self.grado_comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"11-1", None))
        self.grado_comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"10-1", None))
        self.grado_comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"10-2", None))
        self.grado_comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"10-3", None))
        self.grado_comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"10-4", None))
        self.grado_comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"9-3", None))
        self.grado_comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"9-2", None))
        self.grado_comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"9-1", None))
        self.grado_comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"8-3", None))
        self.grado_comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"8-2", None))
        self.grado_comboBox_3.setItemText(13, QCoreApplication.translate("MainWindow", u"8-1", None))
        self.grado_comboBox_3.setItemText(14, QCoreApplication.translate("MainWindow", u"7-3", None))
        self.grado_comboBox_3.setItemText(15, QCoreApplication.translate("MainWindow", u"7-2", None))
        self.grado_comboBox_3.setItemText(16, QCoreApplication.translate("MainWindow", u"7-1", None))
        self.grado_comboBox_3.setItemText(17, QCoreApplication.translate("MainWindow", u"6-3", None))
        self.grado_comboBox_3.setItemText(18, QCoreApplication.translate("MainWindow", u"6-2", None))
        self.grado_comboBox_3.setItemText(19, QCoreApplication.translate("MainWindow", u"6-1", None))

        self.pdf_Button_3.setText(QCoreApplication.translate("MainWindow", u" Exportar a PDF", None))
        self.buscar_lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Busca Aqu\u00ed...", None))
        ___qtablewidgetitem18 = self.registros_tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo", None));
        ___qtablewidgetitem19 = self.registros_tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem20 = self.registros_tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem21 = self.registros_tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem22 = self.registros_tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem23 = self.registros_tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Grado", None));
        ___qtablewidgetitem24 = self.registros_tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Edad", None));
        ___qtablewidgetitem25 = self.registros_tableWidget_3.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"N\u00famero tel", None));
        ___qtablewidgetitem26 = self.registros_tableWidget_3.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"smartasisJDO@gmail.com", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"P\u00e1gina Web", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Correo electr\u00f3nico", None))
        self.label_27.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"https://ofbravon.wixsite.com/my-site-1", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u00a1Contactenos!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u00a1Bienvenido Docente!", None))
        self.pushButton_20.setText("")
        self.pushButton_11.setText("")
    # retranslateUi

