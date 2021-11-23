import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.update_result()

    def update_result(self):
        cur = self.con.cursor()
        names = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
              'Описание вкуса', 'Цена', 'Обьем упаковки']
        # Получили результат запроса, который ввели в текстовое поле
        queue = "SELECT * FROM coffee"
        result = cur.execute(queue).fetchall()
        # Заполнили размеры таблицы
        self.table.setRowCount(len(result))
        if not result:
            return
        self.table.setColumnCount(len(result[0]))
        self.table.setHorizontalHeaderLabels(names)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))
        self.table.resizeColumnsToContents()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())