# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from PySide6 import QtWidgets, QtCore, QtGui
from Pet_model_design import Ui_MainWindow
import re
import openpyxl
import glob
import pandas as pd
import os

class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#         self.timer = Thread_1()
#         self.timer.signal_1.connect(self.setLineEditText)

        self.ui.Open_File_Excel.clicked.connect(self.onPushButton_Open_File)
        self.ui.Loading_FES.clicked.connect(self.onPushButton_Loading_FES)


    def onPushButton_Open_File(self):
        file_new = QtWidgets.QFileDialog.getOpenFileUrl(self, "Выберите файл")
        file_str = str(file_new)
        regex = r'(\/\w+\S+[xlsx])'
        matches = str(re.findall(regex, file_str))
        file = matches[2:(len(matches)-2)]
        wb = openpyxl.load_workbook(filename = file)
        sheet = wb['Core_FES']
        text_exel = ""
        for row in sheet.values:
            text_exel += str(row) + "" + "\n"
        self.ui.Preview_Data.append(text_exel)

    def onPushButton_Loading_FES(self):
        # Загрузим exel-лист в DataFrame под именем: df1
        # df1 = xl.parse('Core_FES')
        # for n in xl:
        #     self.ui.textEdit.append(str(n))
        # self.ui.Preview_Data.append(str(file))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
