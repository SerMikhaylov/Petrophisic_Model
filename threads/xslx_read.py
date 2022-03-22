from PySide6 import QtCore
import openpyxl
import pandas as pd


class XSLXReader(QtCore.QThread):
    XLSXReaderSignal = QtCore.Signal(str)

    def setFileName(self, file_name: str) -> None:
        self.file_name = file_name

    def run(self):
        if not self.file_name:
            raise AttributeError

        wb = openpyxl.load_workbook(filename=self.file_name)
        xl = pd.ExcelFile(self.file_name)
        df_excel = xl.parse('Core_FES')
        # выбор листа файла excel
        sheet = wb['Core_FES']
        # считывание содержимого excel-файла
        text_exel = ""
        for row in sheet.values:
            text_exel += str(row) + "" + "\n"

        self.XLSXReaderSignal.emit(text_exel)




