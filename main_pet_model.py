from PySide6 import QtWidgets, QtCore, QtGui
from Pet_model_design import Ui_MainWindow
from dataclasses import dataclass
import re
import openpyxl
from charts import Chart
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import glob
import pandas as pd
import os


@dataclass
class Petrophisical_properties:
    poro: float  # пористость
    perm: float  # проницаемость
    density: float  # плотность
    water_irr: float  # остаточная водонасыщенность


@dataclass
class File_directory:
    file_directory: str  # переменная, в которую записывается путь к открываемому файлу excel


class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #         self.timer = Thread_1()
        #         self.timer.signal_1.connect(self.setLineEditText)

        self.ui.Open_File_Excel.clicked.connect(self.onPushButton_Open_File)  # Кнопка Открыть файл Excel
        self.ui.Loading_FES.clicked.connect(self.onPushButton_Loading_FES)  # Кнопка Загрузка ФЕС

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
        way_to_file = file_directory.file_directory
        # выбор листа файла excel
        sheet = wb['Core_FES']
        # считывание содержимого excel-файла
        text_exel = ""
        for row in sheet.values:
            text_exel += str(row) + "" + "\n"
        # вывод информации в TextBrowser
        self.ui.Preview_Data.append(text_exel)
        return way_to_file

    # Функция для загрузки ФЕС, т.е. подготовки данных excel для построения графиков
    def onPushButton_Loading_FES(self, way_to_file):
        # Load spreadsheet
        xl = pd.ExcelFile(way_to_file)
        # Загрузим exel-лист в DataFrame под именем: df_excel
        df_excel = xl.parse('Core_FES')
        # исключаем строки, в которых имеются пропуски данных в любой из колонок
        df_excel = df_excel.dropna()
        # porosity = []       # пористость
        # permeability = []   # проницаемость
        # density = []        # плотность
        # wat_ir = []         # остаточная водонасыщенность
        # porosity = [elem for elem in df_excel.KPO]
        # permeability = [elem for elem in df_excel.KPR]
        # density = [elem for elem in df_excel.PLO]
        # wat_ir = [elem for elem in df_excel.KVS]
        return print(df_excel)






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
