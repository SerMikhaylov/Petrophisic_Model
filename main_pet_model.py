from PySide6 import QtWidgets
from Pet_model_design import Ui_MainWindow
from dataclasses import dataclass
import openpyxl
from charts import MplCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
import pandas as pd
import itertools
from Podbor_koef import Koef_fes, calk_function_perm, calk_function_density
from threads.xslx_read import XSLXReader


class MainTestWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainTestWindow, self).__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.porosity = None
        self.permeability = None
        self.density = None
        self.wat_ir = None
        self.num_well = None
        self.num_poro = None
        self.num_perm = None
        self.num_wirr = None
        self.num_gis = None

        # init threads
        self.xlsx_reader_thread = XSLXReader()

        # threads events
        self.xlsx_reader_thread.started.connect(self.XLSXReadThreadStarted)
        self.xlsx_reader_thread.finished.connect(lambda: self.setEnabled(True))
        self.xlsx_reader_thread.XLSXReaderSignal.connect(lambda text: self.ui.Preview_Data.setText(text))

        # Window dimensions
        geometry = self.screen().availableGeometry()
        self.setFixedSize(geometry.width() * 0.95, geometry.height() * 0.95)

        self.ui.tabWidget.setCurrentWidget(self.ui.tab_3)

        self.ui.Open_File_Excel.clicked.connect(self.onPushButton_Open_File)  # Кнопка Открыть файл Excel
        self.ui.Loading_FES.clicked.connect(self.onPushButton_Loading_FES)  # Кнопка Загрузка ФЕС
        self.ui.Statistic_info_model.clicked.connect(self.onPushButton_Statistic)  # Кнопка загрузки статистики
        self.ui.Create_Graf_FES.clicked.connect(self.onPushButton_Create_Graf_FES)  # Кнопка построить графики ФЕС
        self.ui.But_View_Koef_Perm_Poro.clicked.connect(
            self.onPushButton_But_View_Koef_Perm_Poro)  # Кнопка показать коэф Perm=f(Poro)
        self.ui.But_View_Koef_Dens_Poro.clicked.connect(
            self.onPushButton_But_View_Koef_Dens_Poro)  # Кнопка показать коэф Dens=f(Poro)

    def XLSXReadThreadStarted(self):
        self.setEnabled(False)
        self.ui.Preview_Data.setText("Идёт загрузка данных. Подождите...")

    # функция для выбора файла excel и предварительного просмотра
    def onPushButton_Open_File(self):
        # выбор файла
        file_new = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", filter="*.xlsx")[0]
        # преобразование пути к файлу в строковый вид

        if not file_new:
            return

        self.ui.lineEditXlsxFile.setText(file_new)

        self.xlsx_reader_thread.setFileName(file_new)
        self.xlsx_reader_thread.start()

        # wb = openpyxl.load_workbook(filename=file_str)
        # xl = pd.ExcelFile(file_str)
        # df_excel = xl.parse('Core_FES')
        # # выбор листа файла excel
        # sheet = wb['Core_FES']
        # # считывание содержимого excel-файла
        # text_exel = ""
        # for row in sheet.values:
        #     text_exel += str(row) + "" + "\n"
        # # вывод информации в TextBrowser
        # self.ui.Preview_Data.append(text_exel)

    # Функция для загрузки ФЕС, т.е. подготовки данных excel для построения графиков
    def onPushButton_Loading_FES(self):
        filename = self.ui.lineEditXlsxFile.text()

        if not filename:
            QtWidgets.QMessageBox.warning(self, "Внимание!", "Обрабатываемый файл не выбран!")
            return

        # Load spreadsheet
        xl = pd.ExcelFile(filename)
        # Загрузим exel-лист в DataFrame под именем: df_excel
        df_excel = xl.parse('Core_FES')
        # Рассчитаем статистику
        self.num_well = str(len(list(set([elem for elem in df_excel.Well]))))  # количество скважин с керном
        self.num_poro = str(len([elem for elem in df_excel.KPO]))  # количество определений пористости
        self.num_perm = str(len([elem for elem in df_excel.KPR]))  # количество определений проницаемости
        self.num_wirr = str(len([elem for elem in df_excel.KVS]))  # количество определений остаточной водонасыщенности
        self.num_gis = str(len(list(set([elem for elem in df_excel.PLO]))))  # количество скважин с ГИС
        # исключаем строки, в которых имеются пропуски данных в любой из колонок
        df_excel = df_excel.dropna()
        self.porosity = [elem for elem in df_excel.KPO]
        self.permeability = [elem for elem in df_excel.KPR]
        self.density = [elem for elem in df_excel.PLO]
        self.wat_ir = [elem for elem in df_excel.KVS]

    def onPushButton_Statistic(self):
        # вывод информации в TextBrowser
        self.ui.View_Num_Well_core.append(self.num_well)
        self.ui.View_Num_Poro_core.append(self.num_poro)
        self.ui.View_Num_Perm_core.append(self.num_perm)
        self.ui.View_Num_WaterIrr_core.append(self.num_wirr)
        self.ui.View_Num_Well_GIS.append(self.num_gis)

    def onPushButton_Create_Graf_FES(self):
        self.chart_poro_perm = MplCanvas(self, 'Пористость, %', 'Проницаемость, мД',
                                         'Кросс-плот зависимости Проницаемости от Пористости', width=4, height=7,
                                         dpi=100, xmin=0, xmax=25, ymin=0.01, ymax=100)

        toolbar = NavigationToolbar2QT(self.chart_poro_perm, self)
        toolbar.setObjectName('toolbar')

        # create a layout inside the blank widget and add the matplotlib widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.chart_poro_perm)

        cw = QtWidgets.QWidget()
        cw.setObjectName('cw')
        cw.setLayout(layout)

        self.xdata = self.porosity
        self.ydata = self.permeability

        self.chart_poro_perm.axes.set_yscale('log')

        self.chart_poro_perm.axes.scatter(self.xdata, self.ydata, color='red')

        self.ui.Relation_Perm_Poro.setLayout(layout)

        self.chart_poro_density = MplCanvas(self, 'Пористость, %', 'Плотность, г/см3',
                                            'Кросс-плот зависимости Плотности горных пород от Пористости', width=4,
                                            height=7, dpi=100, xmin=0, xmax=25, ymin=2, ymax=2.8)

        toolbar = NavigationToolbar2QT(self.chart_poro_density, self)
        toolbar.setObjectName('toolbar')

        # create a layout inside the blank widget and add the matplotlib widget
        layout = QtWidgets.QVBoxLayout()
        # layout.addLayout(layout_title)
        layout.addWidget(toolbar)
        layout.addWidget(self.chart_poro_density)

        cw_2 = QtWidgets.QWidget()
        cw_2.setObjectName('cw_2')
        cw_2.setLayout(layout)

        self.xdata_2 = self.porosity
        self.ydata_2 = self.density

        self.chart_poro_density.axes.scatter(self.xdata_2, self.ydata_2)

        self.ui.Relation_Density_Poro.setLayout(layout)

    def onPushButton_But_View_Koef_Perm_Poro(self):
        self.koef_1 = Koef_fes(30, 0.001, 0.01)
        self.koef_2 = Koef_fes(30, 2, 3)
        self.koef_3 = Koef_fes(30, -1, 7)

        nev_min = 1000000000
        gen = itertools.product(self.koef_1.var_koef_fes, self.koef_2.var_koef_fes, self.koef_3.var_koef_fes)
        proiz = self.koef_1.n_koef_fes * self.koef_2.n_koef_fes * self.koef_3.n_koef_fes
        for i in range(proiz):
            g_ = next(gen)
            koef_1_r = g_[0]
            koef_2_r = g_[1]
            koef_3_r = g_[2]

            # Рассчитываем проницаемость
            perm_calk = calk_function_perm(koef_1_r, koef_2_r, koef_3_r, self.porosity)
            Raznica = perm_calk - self.permeability
            modul = abs(Raznica)
            summa = sum(modul)
            nev_perm_calk = summa
            if nev_perm_calk < nev_min:
                self.koef_1.num_koef_fes = g_[0]
                self.koef_2.num_koef_fes = g_[1]
                self.koef_3.num_koef_fes = g_[2]
                nev_min = nev_perm_calk
        self.ui.View_Koef_Relation_Perm_Poro.append(
            f'Perm = exp({self.koef_1.num_koef_fes}*(Poro**{self.koef_2.num_koef_fes}) - {self.koef_3.num_koef_fes})')

    def onPushButton_But_View_Koef_Dens_Poro(self):
        self.koef_1 = Koef_fes(30, -1, 0)
        self.koef_2 = Koef_fes(30, 2, 3)

        nev_min = 1000000000
        gen = itertools.product(self.koef_1.var_koef_fes, self.koef_2.var_koef_fes)
        proiz = self.koef_1.n_koef_fes * self.koef_2.n_koef_fes
        for i in range(proiz):
            g_ = next(gen)
            koef_1_r = g_[0]
            koef_2_r = g_[1]

            # Рассчитываем плотность
            dens_calk = calk_function_density(koef_1_r, koef_2_r, self.porosity)
            Raznica = dens_calk - self.density
            modul = abs(Raznica)
            summa = sum(modul)
            nev_dens_calk = summa
            if nev_dens_calk < nev_min:
                self.koef_1.num_koef_fes = g_[0]
                self.koef_2.num_koef_fes = g_[1]
                nev_min = nev_dens_calk
        self.ui.View_Koef_Relation_Density_Poro.append(
            f'Perm = {self.koef_1.num_koef_fes}*Poro + {self.koef_2.num_koef_fes}')

    def onPushButton_Create_Graf_FES(self):
        self.chart_poro_perm = MplCanvas(self, 'Пористость, %', 'Проницаемость, мД',
                                         'Кросс-плот зависимости Проницаемости от Пористости', width=4, height=7,
                                         dpi=100, xmin=0, xmax=25, ymin=0.01, ymax=100)

        toolbar = NavigationToolbar2QT(self.chart_poro_perm, self)
        toolbar.setObjectName('toolbar')

        # create a layout inside the blank widget and add the matplotlib widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.chart_poro_perm)

        cw = QtWidgets.QWidget()
        cw.setObjectName('cw')
        cw.setLayout(layout)

        self.xdata = self.porosity
        self.ydata = self.permeability

        self.chart_poro_perm.axes.set_yscale('log')

        self.chart_poro_perm.axes.scatter(self.xdata, self.ydata, color='red')

        self.ui.Relation_Perm_Poro.setLayout(layout)

        self.chart_poro_density = MplCanvas(self, 'Пористость, %', 'Плотность, г/см3',
                                            'Кросс-плот зависимости Плотности горных пород от Пористости', width=4,
                                            height=7, dpi=100, xmin=0, xmax=25, ymin=2, ymax=2.8)

        toolbar = NavigationToolbar2QT(self.chart_poro_density, self)
        toolbar.setObjectName('toolbar')

        # create a layout inside the blank widget and add the matplotlib widget
        layout = QtWidgets.QVBoxLayout()
        # layout.addLayout(layout_title)
        layout.addWidget(toolbar)
        layout.addWidget(self.chart_poro_density)

        cw_2 = QtWidgets.QWidget()
        cw_2.setObjectName('cw_2')
        cw_2.setLayout(layout)

        self.xdata_2 = self.porosity
        self.ydata_2 = self.density

        self.chart_poro_density.axes.scatter(self.xdata_2, self.ydata_2)

        self.ui.Relation_Density_Poro.setLayout(layout)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = MainTestWindow()
    window.show()

    app.exec()
