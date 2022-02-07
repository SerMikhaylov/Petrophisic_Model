# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pet_model_design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextBrowser,
    QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1194, 779)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon = QIcon()
        icon.addFile(u"Resourses/icons8-create-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action.setIcon(icon)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        icon1 = QIcon()
        icon1.addFile(u"Resourses/icons8-save-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_2.setIcon(icon1)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        icon2 = QIcon()
        icon2.addFile(u"Resourses/icons8-logout-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_3.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Open_File_Excel = QPushButton(self.tab_3)
        self.Open_File_Excel.setObjectName(u"Open_File_Excel")

        self.horizontalLayout_5.addWidget(self.Open_File_Excel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.Preview_Data = QTextBrowser(self.tab_3)
        self.Preview_Data.setObjectName(u"Preview_Data")

        self.verticalLayout_4.addWidget(self.Preview_Data)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Loading_FES = QPushButton(self.tab_3)
        self.Loading_FES.setObjectName(u"Loading_FES")

        self.horizontalLayout_6.addWidget(self.Loading_FES)

        self.Loading_UES = QPushButton(self.tab_3)
        self.Loading_UES.setObjectName(u"Loading_UES")

        self.horizontalLayout_6.addWidget(self.Loading_UES)

        self.Loading_Capil_Data = QPushButton(self.tab_3)
        self.Loading_Capil_Data.setObjectName(u"Loading_Capil_Data")

        self.horizontalLayout_6.addWidget(self.Loading_Capil_Data)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setIndent(-3)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Field = QLabel(self.tab)
        self.Field.setObjectName(u"Field")

        self.verticalLayout.addWidget(self.Field)

        self.Plast = QLabel(self.tab)
        self.Plast.setObjectName(u"Plast")

        self.verticalLayout.addWidget(self.Plast)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_5 = QSpacerItem(168, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Name_Field = QLineEdit(self.tab)
        self.Name_Field.setObjectName(u"Name_Field")

        self.verticalLayout_2.addWidget(self.Name_Field)

        self.Name_Layer = QLineEdit(self.tab)
        self.Name_Layer.setObjectName(u"Name_Layer")

        self.verticalLayout_2.addWidget(self.Name_Layer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Statistic_info_model = QPushButton(self.tab)
        self.Statistic_info_model.setObjectName(u"Statistic_info_model")

        self.horizontalLayout_8.addWidget(self.Statistic_info_model)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.gridLayout_2.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Num_Well_core = QLabel(self.tab)
        self.Num_Well_core.setObjectName(u"Num_Well_core")

        self.verticalLayout_3.addWidget(self.Num_Well_core)

        self.Num_Core_PORO = QLabel(self.tab)
        self.Num_Core_PORO.setObjectName(u"Num_Core_PORO")

        self.verticalLayout_3.addWidget(self.Num_Core_PORO)

        self.Num_Core_PERM = QLabel(self.tab)
        self.Num_Core_PERM.setObjectName(u"Num_Core_PERM")

        self.verticalLayout_3.addWidget(self.Num_Core_PERM)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.Num_Well_GIS = QLabel(self.tab)
        self.Num_Well_GIS.setObjectName(u"Num_Well_GIS")

        self.verticalLayout_3.addWidget(self.Num_Well_GIS)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(208, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.View_Num_Well_core = QTextBrowser(self.tab)
        self.View_Num_Well_core.setObjectName(u"View_Num_Well_core")

        self.verticalLayout_5.addWidget(self.View_Num_Well_core)

        self.View_Num_Poro_core = QTextBrowser(self.tab)
        self.View_Num_Poro_core.setObjectName(u"View_Num_Poro_core")

        self.verticalLayout_5.addWidget(self.View_Num_Poro_core)

        self.View_Num_Perm_core = QTextBrowser(self.tab)
        self.View_Num_Perm_core.setObjectName(u"View_Num_Perm_core")

        self.verticalLayout_5.addWidget(self.View_Num_Perm_core)

        self.View_Num_WaterIrr_core = QTextBrowser(self.tab)
        self.View_Num_WaterIrr_core.setObjectName(u"View_Num_WaterIrr_core")

        self.verticalLayout_5.addWidget(self.View_Num_WaterIrr_core)

        self.View_Num_Well_GIS = QTextBrowser(self.tab)
        self.View_Num_Well_GIS.setObjectName(u"View_Num_Well_GIS")

        self.verticalLayout_5.addWidget(self.View_Num_Well_GIS)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.Relation_Perm_Poro = QGraphicsView(self.tab_2)
        self.Relation_Perm_Poro.setObjectName(u"Relation_Perm_Poro")

        self.verticalLayout_6.addWidget(self.Relation_Perm_Poro)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.Relation_Density_Poro = QGraphicsView(self.tab_2)
        self.Relation_Density_Poro.setObjectName(u"Relation_Density_Poro")

        self.verticalLayout_7.addWidget(self.Relation_Density_Poro)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.View_Koef_Relation_Perm_Poro = QTextBrowser(self.tab_2)
        self.View_Koef_Relation_Perm_Poro.setObjectName(u"View_Koef_Relation_Perm_Poro")

        self.verticalLayout_8.addWidget(self.View_Koef_Relation_Perm_Poro)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.View_Koef_Relation_Density_Poro = QTextBrowser(self.tab_2)
        self.View_Koef_Relation_Density_Poro.setObjectName(u"View_Koef_Relation_Density_Poro")

        self.verticalLayout_9.addWidget(self.View_Koef_Relation_Density_Poro)


        self.gridLayout.addLayout(self.verticalLayout_9, 1, 1, 1, 1)

        self.Create_Graf_FES = QPushButton(self.tab_2)
        self.Create_Graf_FES.setObjectName(u"Create_Graf_FES")

        self.gridLayout.addWidget(self.Create_Graf_FES, 2, 0, 1, 1)

        self.Create_Relations_FES = QPushButton(self.tab_2)
        self.Create_Relations_FES.setObjectName(u"Create_Relations_FES")

        self.gridLayout.addWidget(self.Create_Relations_FES, 2, 1, 1, 1)

        self.But_View_Koef_Perm_Poro = QPushButton(self.tab_2)
        self.But_View_Koef_Perm_Poro.setObjectName(u"But_View_Koef_Perm_Poro")

        self.gridLayout.addWidget(self.But_View_Koef_Perm_Poro, 3, 0, 1, 1)

        self.But_View_Koef_Dens_Poro = QPushButton(self.tab_2)
        self.But_View_Koef_Dens_Poro.setObjectName(u"But_View_Koef_Dens_Poro")

        self.gridLayout.addWidget(self.But_View_Koef_Dens_Poro, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_4 = QGridLayout(self.tab_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.tab_4)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.Relation_WaterIrr_PoroDin = QGraphicsView(self.tab_4)
        self.Relation_WaterIrr_PoroDin.setObjectName(u"Relation_WaterIrr_PoroDin")

        self.verticalLayout_12.addWidget(self.Relation_WaterIrr_PoroDin)


        self.gridLayout_4.addLayout(self.verticalLayout_12, 1, 0, 1, 2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_11.addWidget(self.label_9)

        self.Relation_Perm_PoroDin = QGraphicsView(self.tab_4)
        self.Relation_Perm_PoroDin.setObjectName(u"Relation_Perm_PoroDin")

        self.verticalLayout_11.addWidget(self.Relation_Perm_PoroDin)


        self.gridLayout_4.addLayout(self.verticalLayout_11, 0, 2, 1, 2)

        self.Create_Graf_Limit_Value = QPushButton(self.tab_4)
        self.Create_Graf_Limit_Value.setObjectName(u"Create_Graf_Limit_Value")

        self.gridLayout_4.addWidget(self.Create_Graf_Limit_Value, 2, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.View_Limit_Values_FES = QTextBrowser(self.tab_4)
        self.View_Limit_Values_FES.setObjectName(u"View_Limit_Values_FES")

        self.verticalLayout_13.addWidget(self.View_Limit_Values_FES)


        self.gridLayout_4.addLayout(self.verticalLayout_13, 1, 2, 1, 2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.tab_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.Relation_Poro_PoroDin = QGraphicsView(self.tab_4)
        self.Relation_Poro_PoroDin.setObjectName(u"Relation_Poro_PoroDin")

        self.verticalLayout_10.addWidget(self.Relation_Poro_PoroDin)


        self.gridLayout_4.addLayout(self.verticalLayout_10, 0, 0, 1, 2)

        self.View_Limit_Values = QPushButton(self.tab_4)
        self.View_Limit_Values.setObjectName(u"View_Limit_Values")

        self.gridLayout_4.addWidget(self.View_Limit_Values, 2, 3, 1, 1)

        self.Create_Relation_Limit_Value = QPushButton(self.tab_4)
        self.Create_Relation_Limit_Value.setObjectName(u"Create_Relation_Limit_Value")

        self.gridLayout_4.addWidget(self.Create_Relation_Limit_Value, 2, 1, 1, 2)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_5 = QGridLayout(self.tab_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)

        self.Relation_Pp_Poro = QGraphicsView(self.tab_5)
        self.Relation_Pp_Poro.setObjectName(u"Relation_Pp_Poro")

        self.verticalLayout_14.addWidget(self.Relation_Pp_Poro)


        self.gridLayout_5.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.tab_5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_15.addWidget(self.label_13)

        self.Relation_Pn_WaterSat = QGraphicsView(self.tab_5)
        self.Relation_Pn_WaterSat.setObjectName(u"Relation_Pn_WaterSat")

        self.verticalLayout_15.addWidget(self.Relation_Pn_WaterSat)


        self.gridLayout_5.addLayout(self.verticalLayout_15, 0, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.tab_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_16.addWidget(self.label_14)

        self.View_Koef_AD = QTextBrowser(self.tab_5)
        self.View_Koef_AD.setObjectName(u"View_Koef_AD")

        self.verticalLayout_16.addWidget(self.View_Koef_AD)


        self.gridLayout_5.addLayout(self.verticalLayout_16, 0, 2, 1, 1)

        self.Create_Graf_AD = QPushButton(self.tab_5)
        self.Create_Graf_AD.setObjectName(u"Create_Graf_AD")

        self.gridLayout_5.addWidget(self.Create_Graf_AD, 1, 0, 1, 1)

        self.Create_Relation_AD = QPushButton(self.tab_5)
        self.Create_Relation_AD.setObjectName(u"Create_Relation_AD")

        self.gridLayout_5.addWidget(self.Create_Relation_AD, 1, 1, 1, 1)

        self.View_Koef_AD_2 = QPushButton(self.tab_5)
        self.View_Koef_AD_2.setObjectName(u"View_Koef_AD_2")

        self.gridLayout_5.addWidget(self.View_Koef_AD_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1194, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"&\u041d\u043e\u0432\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c", None))
#if QT_CONFIG(tooltip)
        self.action.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0439 \u043c\u043e\u0434\u0435\u043b\u0438", None))
#endif // QT_CONFIG(tooltip)
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"&\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.action_2.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"&\u0412\u044b\u0445\u043e\u0434", None))
#if QT_CONFIG(tooltip)
        self.action_3.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f \u043a\u0435\u0440\u043d\u043e\u0432\u043e\u0433\u043e \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430", None))
        self.Open_File_Excel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b Excel", None))
        self.Loading_FES.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0424\u0415\u0421", None))
        self.Loading_UES.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0423\u042d\u0421", None))
        self.Loading_Capil_Data.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u0430\u043f\u0438\u043b\u043b\u044f\u0440\u0438\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0442\u0440\u043e\u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.Field.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0441\u0442\u043e\u0440\u043e\u0436\u0434\u0435\u043d\u0438\u0435", None))
        self.Plast.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043b\u0430\u0441\u0442", None))
        self.Statistic_info_model.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u043e\u0431\u0449\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043f\u043e \u043c\u043e\u0434\u0435\u043b\u0438", None))
        self.Num_Well_core.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043a\u0432\u0430\u0436\u0438\u043d \u0441 \u043a\u0435\u0440\u043d\u043e\u043c", None))
        self.Num_Core_PORO.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0439 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.Num_Core_PERM.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0439 \u043f\u0440\u043e\u043d\u0438\u0446\u0430\u0435\u043c\u043e\u0441\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0439 \u043e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e\u0439 \u0432\u043e\u0434\u043e\u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u0438", None))
        self.Num_Well_GIS.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043a\u0432\u0430\u0436\u0438\u043d \u0441 \u0433\u0435\u043e\u0444\u0438\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u043c\u0438 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f\u043c\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u044c \u041f\u0440\u043e\u043d\u0438\u0446\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u041f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u044c \u041f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u0438 \u043e\u0442 \u041f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0442\u0438 \u043f\u0440\u043e\u043d\u0438\u0446\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u0438 \u043e\u0442 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.Create_Graf_FES.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0424\u0415\u0421", None))
        self.Create_Relations_FES.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0445", None))
        self.But_View_Koef_Perm_Poro.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b Perm=f(Poro)", None))
        self.But_View_Koef_Dens_Poro.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b Dens=f(Poro)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0424\u0415\u0421", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u041e\u0441\u0442\u0430\u0442\u043e\u0447\u043d\u043e\u0439 \u0412\u043e\u0434\u043e\u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u043e\u0442 \u0414\u0438\u043d\u0430\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u0441\u043c\u043e\u0441\u0442\u0438 \u041f\u0440\u043e\u043d\u0438\u0446\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u0414\u0438\u043d\u0430\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.Create_Graf_Limit_Value.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u043d\u0438\u0447\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0424\u0415\u0421", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u041f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438 \u043e\u0442 \u0414\u0438\u043d\u0430\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.View_Limit_Values.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0433\u0440\u0430\u043d\u0438\u0447\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.Create_Relation_Limit_Value.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u0433\u0440\u0430\u043d\u0438\u0447\u043d\u044b\u0445 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435 \u0424\u0415\u0421", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043f = f(\u041a\u043f)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043d = f(\u041a\u0432)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0444\u043e\u0440\u043c\u0443\u043b\u044b \u0410\u0440\u0447\u0438-\u0414\u0430\u0445\u043d\u043e\u0432\u0430", None))
        self.Create_Graf_AD.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0410\u0440\u0447\u0438-\u0414\u0430\u0445\u043d\u043e\u0432\u0430", None))
        self.Create_Relation_AD.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u0410\u0440\u0447\u0438-\u0414\u0430\u0445\u043d\u043e\u0432\u0430", None))
        self.View_Koef_AD_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0410\u0440\u0447\u0438-\u0414\u0430\u0445\u043d\u043e\u0432\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u044d\u043b\u0435\u043a\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u0438\u0445 \u0441\u0432\u043e\u0439\u0441\u0442\u0432", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

