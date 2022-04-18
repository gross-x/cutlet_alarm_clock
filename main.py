# Котлетный будильник.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


def add_label():
    print("Кнопка нажата")


def application(): # Create windows and text and button
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Cutlets alarm clock")
    window.setGeometry(300, 250, 350, 200)

    # Create text
    main_text = QtWidgets.QLabel(window)
    main_text.setText("!...Базовая надпись...!")  # create text
    main_text.move(100, 100)  # move text the 100 pc
    main_text.adjustSize()  # embedding an object in the content
    main_text.setFixedWidth(200)

    # Create button
    btn = QtWidgets.QPushButton(window)  # create button
    btn.move(70, 150)
    btn.setText("Нажми меня")
    btn.setFixedWidth(200)
    btn.clicked.connect(add_label)  # объект.событие_объекта.метод(функция) Функцию не вызываем, только помещаем.

    window.show()  # show windows
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
