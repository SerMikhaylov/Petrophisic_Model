
from PySide6 import QtWidgets, QtCore, QtGui
from Pet_model_design import Ui_MainWindow
from dataclasses import dataclass
import re
import openpyxl
import glob
import pandas as pd
import os


@dataclass
class Petrophisical_properties:
    poro: float  # пористость
    perm: float  # проницаемость
    density: float  # плотность
    warer_irr: float  # остаточная водонасыщенность

@dataclass
class File_directory:
    file_directory: str  # переменная, в которую записывается путь в открываемому файлу excel

class Chart:
    def __init__(self, width, height, x_min, x_max, y_min, y_max):
        self.width = width  # ширина графика
        self.height = height    # высота графика


class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #         self.timer = Thread_1()
        #         self.timer.signal_1.connect(self.setLineEditText)

        self.ui.Open_File_Excel.clicked.connect(self.onPushButton_Open_File)  # Кнопка Открыть файл Excel
        # self.ui.Loading_FES.clicked.connect(self.onPushButton_Loading_FES)  # Кнопка Загрузка ФЕС

    # функция для выбора файла excel и предварительного просмотра
    def onPushButton_Open_File(self):
        # выбор файла
        file_new = QtWidgets.QFileDialog.getOpenFileUrl(self, "Выберите файл")
        # преобразование пути к файлу в строковый вид
        file_str = str(file_new)
        # удаление лишних символов с помощью регулярных выражений
        regex = r'(\/\w+\S+[xlsx])'
        matches = str(re.findall(regex, file_str))
        # итоговый путь к файлу
        file = matches[2:(len(matches) - 2)]
        file_directory = File_directory(file)
        wb = openpyxl.load_workbook(filename=file_directory.file_directory)
        # выбор листа файла excel
        sheet = wb['Core_FES']
        # считывание содержимого excel-файла
        text_exel = ""
        for row in sheet.values:
            text_exel += str(row) + "" + "\n"
        # вывод информации в TextBrowser
        self.ui.Preview_Data.append(text_exel)

    # Функция для загрузки ФЕС, т.е. подготовки данных excel для построения графиков
    # def onPushButton_Loading_FES(self):
    #     # Load spreadsheet
    #     xl = pd.ExcelFile(self.file)
    #     # Загрузим exel-лист в DataFrame под именем: df1
    #     df1 = xl.parse('Core_FES')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
