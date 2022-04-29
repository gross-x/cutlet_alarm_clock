# Котлетный будильник.
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
#import sys
from cutlet import Ui_MainWindow


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())