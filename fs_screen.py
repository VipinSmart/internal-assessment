from PyQt5 import QtCore, QtGui, QtWidgets

from enter_food_info import Ui_food_entry_window
from edit_food_info  import Ui_edit_food_window
from delete_fs_info  import Ui_delete_fs_info

class Ui_fs_screen(object):
    def setupUi(self, fs_screen):
        fs_screen.setObjectName("fs_screen")
        fs_screen.resize(631, 503)
        self.centralwidget = QtWidgets.QWidget(fs_screen)
        self.centralwidget.setObjectName("centralwidget")

        self.toggle_lang_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: toggle_lang())
        self.toggle_lang_button.setGeometry(QtCore.QRect(470, 0, 161, 31))
        self.toggle_lang_button.setObjectName("toggle_lang_button")

        self.edit_food_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_edit_food_screen())
        self.edit_food_button.setGeometry(QtCore.QRect(220, 40, 201, 31))
        self.edit_food_button.setObjectName("edit_food_button")

        self.add_food_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_add_food_screen())
        self.add_food_button.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.add_food_button.setObjectName("add_food_button")

        self.delete_food_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_delete_food_screen())
        self.delete_food_button.setGeometry(QtCore.QRect(440, 40, 181, 31))
        self.delete_food_button.setObjectName("delete_food_button")

        #self.home_button = QtWidgets.QPushButton(self.centralwidget)
        #self.home_button.setGeometry(QtCore.QRect(0, 0, 75, 23))
        #self.home_button.setObjectName("home_button")

        self.food_table = QtWidgets.QTableWidget(self.centralwidget)
        self.food_table.setGeometry(QtCore.QRect(10, 90, 611, 371))
        self.food_table.setObjectName("food_table")
        self.food_table.setColumnCount(4)
        self.food_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(3, item)
        fs_screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fs_screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 631, 21))
        self.menubar.setObjectName("menubar")
        fs_screen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(fs_screen)
        self.statusbar.setObjectName("statusbar")
        fs_screen.setStatusBar(self.statusbar)

        self.retranslateUi(fs_screen)
        QtCore.QMetaObject.connectSlotsByName(fs_screen)


        def open_add_food_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_food_entry_window()
            self.ui.setupUi(self.window)
            self.window.show()

        def open_edit_food_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_edit_food_window()
            self.ui.setupUi(self.window)
            self.window.show()

        def open_delete_food_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_delete_fs_info()
            self.ui.setupUi(self.window)
            self.window.show()

        def toggle_lang():
            pass

    def retranslateUi(self, fs_screen):
        _translate = QtCore.QCoreApplication.translate
        fs_screen.setWindowTitle(_translate("fs_screen", "Food and Storage"))
        self.toggle_lang_button.setText(_translate("fs_screen", "Toggle English/German"))
        self.edit_food_button.setText(_translate("fs_screen", "Edit Food"))
        self.add_food_button.setText(_translate("fs_screen", "Add Food"))
        self.delete_food_button.setText(_translate("fs_screen", "Delete Food"))
        #self.home_button.setText(_translate("fs_screen", "Home"))
        item = self.food_table.horizontalHeaderItem(0)
        item.setText(_translate("fs_screen", "Supply (kg)"))
        item = self.food_table.horizontalHeaderItem(1)
        item.setText(_translate("fs_screen", "Supplier"))
        item = self.food_table.horizontalHeaderItem(2)
        item.setText(_translate("fs_screen", "Supplier Phone Number"))
        item = self.food_table.horizontalHeaderItem(3)
        item.setText(_translate("fs_screen", "Supplier Email"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fs_screen = QtWidgets.QMainWindow()
    ui = Ui_fs_screen()
    ui.setupUi(fs_screen)
    fs_screen.show()
    sys.exit(app.exec_())
