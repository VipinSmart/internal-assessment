from PyQt5 import QtCore, QtGui, QtWidgets

#import the classes so that we can open the windows from the buttons on the screen
from edit_animal_info   import Ui_edit_animal_window
from enter_animal_info  import Ui_animal_entry_window
from delete_animal_info import Ui_delete_from_animal_db
#from home_screen       import Ui_home_screen


class Ui_animals_screen(object):
    # all widgets are defined automatically, and the only part which i need to code is the ",clicked = lambda: function()"
    # and the functions themselves. all the buttons will perform their respective tasks when clicked.

    def setupUi(self, animals_screen):
        animals_screen.setObjectName("animals_screen")
        animals_screen.resize(601, 502)
        self.centralwidget = QtWidgets.QWidget(animals_screen)
        self.centralwidget.setObjectName("centralwidget")

        self.toggle_lang_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: toggle_lang())
        self.toggle_lang_button.setGeometry(QtCore.QRect(440, 0, 161, 31))
        self.toggle_lang_button.setObjectName("toggle_lang_button")

        self.add_animal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_add_animal_screen())
        self.add_animal_button.setGeometry(QtCore.QRect(20, 40, 171, 31))
        self.add_animal_button.setObjectName("add_animal_button")

        self.edit_animal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_edit_animal_screen())
        self.edit_animal_button.setGeometry(QtCore.QRect(210, 40, 181, 31))
        self.edit_animal_button.setObjectName("edit_animal_button")

        self.delete_animal_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_delete_animal_screen())
        self.delete_animal_button.setGeometry(QtCore.QRect(410, 40, 171, 31))
        self.delete_animal_button.setObjectName("delete_animal_button")

# ask why i cannot import this. error function says as follows
#ImportError: cannot import name 'Ui_home_screen' from partially initialized module 'home_screen' (most likely due to circular import)
# ALSO NEEDED TO COMMENT LINE 108 FOR THIS REASON
# WILL HAVE TO DO THIS FOR EVERY SCREEN UNTIL FIX THE PROBLEM

#        self.home_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: go_to_home_screen())
#        self.home_button.setGeometry(QtCore.QRect(0, 0, 75, 23))
#        self.home_button.setObjectName("home_button")

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
        animals_screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(animals_screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        animals_screen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(animals_screen)
        self.statusbar.setObjectName("statusbar")
        animals_screen.setStatusBar(self.statusbar)

        self.retranslateUi(animals_screen)
        QtCore.QMetaObject.connectSlotsByName(animals_screen)

        #giving tasks to the buttons to do
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


        #def go_to_home_screen():
            #self.window = QtWidgets
            #self.window = QtWidgets.QMainWindow()
            #self.ui = Ui_home_screen()
            #self.ui.setupUi(self.window)
            #self.window.show()

            #animals_screen.hide()
            

    def retranslateUi(self, animals_screen):
        _translate = QtCore.QCoreApplication.translate
        animals_screen.setWindowTitle(_translate("animals_screen", "Animals"))
        self.toggle_lang_button.setText(_translate("animals_screen", "Toggle English/German"))
        self.add_animal_button.setText(_translate("animals_screen", "Add Animal"))
        self.edit_animal_button.setText(_translate("animals_screen", "Edit Animal"))
        self.delete_animal_button.setText(_translate("animals_screen", "Delete Animal"))
        #self.home_button.setText(_translate("animals_screen", "Home"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("animals_screen", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("animals_screen", "Date Of Birth"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("animals_screen", "Species"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("animals_screen", "Breed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    animals_screen = QtWidgets.QMainWindow()
    ui = Ui_animals_screen()
    ui.setupUi(animals_screen)
    animals_screen.show()
    sys.exit(app.exec_())


################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets

from edit_booking_info    import Ui_edit_booking_window
from enter_booking_info   import Ui_booking_entry_window
from delete_bookings_info import Ui_delete_from_booking_db

class Ui_bookings_screen(object):
    def setupUi(self, bookings_screen):
        bookings_screen.setObjectName("bookings_screen")
        bookings_screen.resize(730, 506)
        self.centralwidget = QtWidgets.QWidget(bookings_screen)
        self.centralwidget.setObjectName("centralwidget")

        self.toggle_lang_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: toggle_lang())
        self.toggle_lang_button.setGeometry(QtCore.QRect(570, 0, 161, 31))
        self.toggle_lang_button.setObjectName("toggle_lang_button")

        self.delete_booking_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_delete_booking_screen())
        self.delete_booking_button.setGeometry(QtCore.QRect(500, 40, 221, 31))
        self.delete_booking_button.setObjectName("delete_booking_button")

        self.add_booking_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_add_booking_screen())
        self.add_booking_button.setGeometry(QtCore.QRect(10, 40, 221, 31))
        self.add_booking_button.setObjectName("add_booking_button")

        self.edit_booking_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_edit_booking_screen())
        self.edit_booking_button.setGeometry(QtCore.QRect(250, 40, 231, 31))
        self.edit_booking_button.setObjectName("edit_booking_button")

        #self.home_button = QtWidgets.QPushButton(self.centralwidget)
        #self.home_button.setGeometry(QtCore.QRect(0, 0, 75, 23))
        #self.home_button.setObjectName("home_button")

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

        bookings_screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(bookings_screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
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


    def retranslateUi(self, bookings_screen):
        _translate = QtCore.QCoreApplication.translate
        bookings_screen.setWindowTitle(_translate("bookings_screen", "Bookings"))
        self.toggle_lang_button.setText(_translate("bookings_screen", "Toggle English/German"))
        self.delete_booking_button.setText(_translate("bookings_screen", "Delete Booking"))
        self.add_booking_button.setText(_translate("bookings_screen", "Add Booking"))
        item = self.bookings_table.horizontalHeaderItem(0)
        item.setText(_translate("bookings_screen", "Customer Name"))
        item = self.bookings_table.horizontalHeaderItem(1)
        item.setText(_translate("bookings_screen", "Single/Monthly"))
        item = self.bookings_table.horizontalHeaderItem(2)
        item.setText(_translate("bookings_screen", "New Column"))
        item = self.bookings_table.horizontalHeaderItem(3)
        item.setText(_translate("bookings_screen", "Horse Name"))
        item = self.bookings_table.horizontalHeaderItem(4)
        item.setText(_translate("bookings_screen", "Private Horse"))
        item = self.bookings_table.horizontalHeaderItem(5)
        item.setText(_translate("bookings_screen", "Type of event"))
        self.edit_booking_button.setText(_translate("bookings_screen", "Edit Booking"))
        #self.home_button.setText(_translate("bookings_screen", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    bookings_screen = QtWidgets.QMainWindow()
    ui = Ui_bookings_screen()
    ui.setupUi(bookings_screen)
    bookings_screen.show()
    sys.exit(app.exec_())



################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
################################################################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets

from enter_food_info import Ui_food_entry_window
from edit_food_info  import Ui_edit_food_window
from delete_fs_info  import Ui_delete_fs_info



class Ui_fs_screen(object):
    def setupUi(self, fs_screen):
        fs_screen.setObjectName("fs_screen")
        fs_screen.resize(630, 503)
        self.centralwidget = QtWidgets.QWidget(fs_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.food_table = QtWidgets.QTableWidget(self.centralwidget)
        self.food_table.setGeometry(QtCore.QRect(10, 90, 611, 371))
        self.food_table.setObjectName("food_table")
        self.food_table.setColumnCount(5)
        self.food_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.food_table.setHorizontalHeaderItem(4, item)

        self.toggle_lang_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: toggle_lang())
        self.toggle_lang_button.setGeometry(QtCore.QRect(470, 0, 161, 31))
        self.toggle_lang_button.setObjectName("toggle_lang_button")

        #self.home_button = QtWidgets.QPushButton(self.centralwidget)
        #self.home_button.setGeometry(QtCore.QRect(0, 0, 75, 23))
        #self.home_button.setObjectName("home_button")

        self.add_food_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_add_food_screen())
        self.add_food_button.setGeometry(QtCore.QRect(10, 40, 191, 31))
        self.add_food_button.setObjectName("add_food_button")

        self.edit_food_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_edit_food_screen())
        self.edit_food_button.setGeometry(QtCore.QRect(220, 40, 201, 31))
        self.edit_food_button.setObjectName("edit_food_button")

        self.delete_food_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: open_delete_food_screen())
        self.delete_food_button.setGeometry(QtCore.QRect(440, 40, 181, 31))
        self.delete_food_button.setObjectName("delete_food_button")      
          
        fs_screen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(fs_screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
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
        item = self.food_table.horizontalHeaderItem(0)
        item.setText(_translate("fs_screen", "Row ID"))
        item = self.food_table.horizontalHeaderItem(1)
        item.setText(_translate("fs_screen", "Supply (kg)"))
        item = self.food_table.horizontalHeaderItem(2)
        item.setText(_translate("fs_screen", "Supplier"))
        item = self.food_table.horizontalHeaderItem(3)
        item.setText(_translate("fs_screen", "Supplier Phone Number"))
        item = self.food_table.horizontalHeaderItem(4)
        item.setText(_translate("fs_screen", "Supplier Email"))
        self.delete_food_button.setText(_translate("fs_screen", "Delete Food"))
        self.toggle_lang_button.setText(_translate("fs_screen", "Toggle English/German"))
        #self.home_button.setText(_translate("fs_screen", "Home"))
        self.add_food_button.setText(_translate("fs_screen", "Add Food"))
        self.edit_food_button.setText(_translate("fs_screen", "Edit Food"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fs_screen = QtWidgets.QMainWindow()
    ui = Ui_fs_screen()
    ui.setupUi(fs_screen)
    fs_screen.show()
    sys.exit(app.exec_())