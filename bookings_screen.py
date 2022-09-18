from PyQt5 import QtCore, QtGui, QtWidgets

from edit_booking_info    import Ui_edit_booking_window
from enter_booking_info   import Ui_booking_entry_window
from delete_bookings_info import Ui_delete_from_booking_db





class Ui_bookings_screen(object):
    def setupUi(self, bookings_screen):
        bookings_screen.setObjectName("bookings_screen")
        bookings_screen.resize(729, 501)
        self.centralwidget = QtWidgets.QWidget(bookings_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.bookings_table = QtWidgets.QTableWidget(self.centralwidget)
        self.bookings_table.setGeometry(QtCore.QRect(10, 90, 711, 371))
        self.bookings_table.setObjectName("bookings_table")
        self.bookings_table.setColumnCount(6)
        self.bookings_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bookings_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookings_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookings_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookings_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookings_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookings_table.setHorizontalHeaderItem(5, item)
        self.home_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_button.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.home_button.setObjectName("home_button")
        self.delete_booking_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_delete_booking_screen())
        self.delete_booking_button.setGeometry(QtCore.QRect(500, 40, 221, 31))
        self.delete_booking_button.setObjectName("delete_booking_button")

        self.add_booking_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_add_booking_screen())
        self.add_booking_button.setGeometry(QtCore.QRect(10, 40, 221, 31))
        self.add_booking_button.setObjectName("add_booking_button")

        self.toggle_lang_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: toggle_lang())
        self.toggle_lang_button.setGeometry(QtCore.QRect(570, 0, 161, 31))
        self.toggle_lang_button.setObjectName("toggle_lang_button")

        self.edit_booking_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_edit_booking_screen())
        self.edit_booking_button.setGeometry(QtCore.QRect(250, 40, 231, 31))
        self.edit_booking_button.setObjectName("edit_booking_button")

        bookings_screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(bookings_screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 21))
        self.menubar.setObjectName("menubar")
        bookings_screen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(bookings_screen)
        self.statusbar.setObjectName("statusbar")
        bookings_screen.setStatusBar(self.statusbar)

        self.retranslateUi(bookings_screen)
        QtCore.QMetaObject.connectSlotsByName(bookings_screen)


        def open_add_booking_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_booking_entry_window()
            self.ui.setupUi(self.window)
            self.window.show()

        def open_edit_booking_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_edit_booking_window()
            self.ui.setupUi(self.window)
            self.window.show()

        def open_delete_booking_screen():
            self.window = QtWidgets
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_delete_from_booking_db()
            self.ui.setupUi(self.window)
            self.window.show()

        def toggle_lang():
            pass

            
    def retranslateUi(self, bookings_screen):
        _translate = QtCore.QCoreApplication.translate
        bookings_screen.setWindowTitle(_translate("bookings_screen", "Bookings"))
        item = self.bookings_table.horizontalHeaderItem(0)
        item.setText(_translate("bookings_screen", "Customer Name"))
        item = self.bookings_table.horizontalHeaderItem(1)
        item.setText(_translate("bookings_screen", "Single/Monthly"))
        item = self.bookings_table.horizontalHeaderItem(2)
        item.setText(_translate("bookings_screen", "Date"))
        item = self.bookings_table.horizontalHeaderItem(3)
        item.setText(_translate("bookings_screen", "Horse Name"))
        item = self.bookings_table.horizontalHeaderItem(4)
        item.setText(_translate("bookings_screen", "Private Horse"))
        item = self.bookings_table.horizontalHeaderItem(5)
        item.setText(_translate("bookings_screen", "Type of event"))
        self.home_button.setText(_translate("bookings_screen", "Home"))
        self.delete_booking_button.setText(_translate("bookings_screen", "Delete Booking"))
        self.add_booking_button.setText(_translate("bookings_screen", "Add Booking"))
        self.toggle_lang_button.setText(_translate("bookings_screen", "Toggle English/German"))
        self.edit_booking_button.setText(_translate("bookings_screen", "Edit Booking"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookings_screen = QtWidgets.QMainWindow()
    ui = Ui_bookings_screen()
    ui.setupUi(bookings_screen)
    bookings_screen.show()
    sys.exit(app.exec_())
