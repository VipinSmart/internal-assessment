from PyQt5 import QtCore, QtGui, QtWidgets

from edit_animal_info    import Ui_edit_animal_window
from enter_animal_info   import Ui_animal_entry_window
from delete_animal_info  import Ui_delete_from_animal_db
from home_screen import Ui_home_screen


class Ui_animals_screen(object):
    def setupUi(self, animals_screen):
        animals_screen.setObjectName("animals_screen")
        animals_screen.resize(600, 505)
        self.centralwidget = QtWidgets.QWidget(animals_screen)
        self.centralwidget.setObjectName("centralwidget")

        self.delete_animal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_delete_animal_screen())
        self.delete_animal_button.setGeometry(QtCore.QRect(410, 40, 171, 31))
        self.delete_animal_button.setObjectName("delete_animal_button")

        self.toggle_lang_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: toggle_lang())
        self.toggle_lang_button.setGeometry(QtCore.QRect(440, 0, 161, 31))
        self.toggle_lang_button.setObjectName("toggle_lang_button")

        self.add_animal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_add_animal_screen())
        self.add_animal_button.setGeometry(QtCore.QRect(20, 40, 171, 31))
        self.add_animal_button.setObjectName("add_animal_button")

        self.edit_animal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_edit_animal_screen())
        self.edit_animal_button.setGeometry(QtCore.QRect(210, 40, 181, 31))
        self.edit_animal_button.setObjectName("edit_animal_button")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 561, 371))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.home_button.setObjectName("home_button" )
        animals_screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(animals_screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        animals_screen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(animals_screen)
        self.statusbar.setObjectName("statusbar")
        animals_screen.setStatusBar(self.statusbar)

        self.retranslateUi(animals_screen)
        QtCore.QMetaObject.connectSlotsByName(animals_screen)
        def go_to_home():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_home_screen()
            self.ui.setupUi(self.window)
            self.window.show()

            animals_screen.hide()

        def open_add_animal_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_animal_entry_window()
            self.ui.setupUi(self.window)
            self.window.show()

        def open_edit_animal_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_edit_animal_window()
            self.ui.setupUi(self.window)
            self.window.show()

        def open_delete_animal_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_delete_from_animal_db()
            self.ui.setupUi(self.window)
            self.window.show()

        def toggle_lang():
            pass


    def retranslateUi(self, animals_screen):
        _translate = QtCore.QCoreApplication.translate
        animals_screen.setWindowTitle(_translate("animals_screen", "Animals"))
        self.delete_animal_button.setText(_translate("animals_screen", "Delete Animal"))
        self.toggle_lang_button.setText(_translate("animals_screen", "Toggle English/German"))
        self.add_animal_button.setText(_translate("animals_screen", "Add Animal"))
        self.edit_animal_button.setText(_translate("animals_screen", "Edit Animal"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("animals_screen", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("animals_screen", "Date Of Birth"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("animals_screen", "Species"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("animals_screen", "Breed"))
        self.home_button.setText(_translate("animals_screen", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    animals_screen = QtWidgets.QMainWindow()
    ui = Ui_animals_screen()
    ui.setupUi(animals_screen)
    animals_screen.show()
    sys.exit(app.exec_())