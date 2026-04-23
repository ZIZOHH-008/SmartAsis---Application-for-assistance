from borrar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MySideBar(QMainWindow, Ui_MainWindow):
    def _init_(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Menu desplegable")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.switch_to_dashboardPage)

        self.profile_1.clicked.connect(self.switch_to_profilePage)
        self.profile_2.clicked.connect(self.switch_to_profilePage)

        self.messages_1.clicked.connect(self.switch_to_messagesPage)
        self.messages_2.clicked.connect(self.switch_to_messagesPage)

        self.notifications_1.clicked.connect(self.switch_to_notificationsPage)
        self.notifications_2.clicked.connect(self.switch_to_notificationsPage)

        self.settings_1.clicked.connect(self.switch_to_settingsPage)
        self.settings_2.clicked.connect(self.switch_to_settingsPage)


    def swich_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def swich_to_profilePage(self):
        self.stackedWidget.setCurrentIndex(1)

    def swich_to_messagesPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def swich_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def swich_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(4)