import os

from PySide6 import QtCore
import openpyxl
import os
import pandas as pd


class XSLXReader(QtCore.QThread):
    XLSXReaderSignal = QtCore.Signal(str)

    def setFileName(self, file_name: str) -> None:
        if not os.path.exists(file_name):
            raise FileNotFoundError("Файл не найден")
        self._file_name = file_name

    def run(self):
        if not self._file_name:
            raise AttributeError

        wb = openpyxl.load_workbook(filename=self._file_name)
        xl = pd.ExcelFile(self._file_name)
        df_excel = xl.parse('Core_FES')
        # выбор листа файла excel
        sheet = wb['Core_FES']
        # считывание содержимого excel-файла
        text_exel = ""
        for row in sheet.values:
            text_exel += str(row) + "" + "\n"

        self.XLSXReaderSignal.emit(text_exel)




