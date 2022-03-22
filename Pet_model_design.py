# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pet_model_design_v4.ui'
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
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QTextBrowser, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1046, 769)
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
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        icon3 = QIcon()
        icon3.addFile(u"Resourses/icons8-open-document-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_4.setIcon(icon3)
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
        self.lineEditXlsxFile = QLineEdit(self.tab_3)
        self.lineEditXlsxFile.setObjectName(u"lineEditXlsxFile")

        self.horizontalLayout_5.addWidget(self.lineEditXlsxFile)

        self.Open_File_Excel = QPushButton(self.tab_3)
        self.Open_File_Excel.setObjectName(u"Open_File_Excel")

        self.horizontalLayout_5.addWidget(self.Open_File_Excel)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.Preview_Data = QTextBrowser(self.tab_3)
        self.Preview_Data.setObjectName(u"Preview_Data")

        self.verticalLayout_4.addWidget(self.Preview_Data)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Loading_FES = QPushButton(self.tab_3)
        self.Loading_FES.setObjectName(u"Loading_FES")

        self.horizontalLayout_6.addWidget(self.Loading_FES)


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
        self.splitter = QSplitter(self.tab_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Relation_Perm_Poro = QGraphicsView(self.layoutWidget)
        self.Relation_Perm_Poro.setObjectName(u"Relation_Perm_Poro")

        self.horizontalLayout_3.addWidget(self.Relation_Perm_Poro)

        self.Relation_Density_Poro = QGraphicsView(self.layoutWidget)
        self.Relation_Density_Poro.setObjectName(u"Relation_Density_Poro")

        self.horizontalLayout_3.addWidget(self.Relation_Density_Poro)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.View_Koef_Relation_Perm_Poro = QTextBrowser(self.layoutWidget1)
        self.View_Koef_Relation_Perm_Poro.setObjectName(u"View_Koef_Relation_Perm_Poro")

        self.verticalLayout_8.addWidget(self.View_Koef_Relation_Perm_Poro)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.Create_Graf_FES = QPushButton(self.layoutWidget1)
        self.Create_Graf_FES.setObjectName(u"Create_Graf_FES")

        self.verticalLayout_6.addWidget(self.Create_Graf_FES)

        self.But_View_Koef_Perm_Poro = QPushButton(self.layoutWidget1)
        self.But_View_Koef_Perm_Poro.setObjectName(u"But_View_Koef_Perm_Poro")

        self.verticalLayout_6.addWidget(self.But_View_Koef_Perm_Poro)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.View_Koef_Relation_Density_Poro = QTextBrowser(self.layoutWidget1)
        self.View_Koef_Relation_Density_Poro.setObjectName(u"View_Koef_Relation_Density_Poro")

        self.verticalLayout_9.addWidget(self.View_Koef_Relation_Density_Poro)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)

        self.Create_Relations_FES = QPushButton(self.layoutWidget1)
        self.Create_Relations_FES.setObjectName(u"Create_Relations_FES")

        self.verticalLayout_7.addWidget(self.Create_Relations_FES)

        self.But_View_Koef_Dens_Poro = QPushButton(self.layoutWidget1)
        self.But_View_Koef_Dens_Poro.setObjectName(u"But_View_Koef_Dens_Poro")

        self.verticalLayout_7.addWidget(self.But_View_Koef_Dens_Poro)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.splitter.addWidget(self.layoutWidget1)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1046, 24))
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
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_4)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.action_3)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


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
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"&\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.action_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_4.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u044f \u043a\u0435\u0440\u043d\u043e\u0432\u043e\u0433\u043e \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430", None))
        self.Open_File_Excel.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u0444\u0430\u0439\u043b Excel", None))
        self.Loading_FES.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0424\u0415\u0421", None))
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0442\u0438 \u043f\u0440\u043e\u043d\u0438\u0446\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043e\u0442 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.Create_Graf_FES.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0424\u0415\u0421", None))
        self.But_View_Koef_Perm_Poro.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b Perm=f(Poro)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u0434\u043b\u044f \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043f\u043b\u043e\u0442\u043d\u043e\u0441\u0442\u0438 \u043e\u0442 \u043f\u043e\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438", None))
        self.Create_Relations_FES.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438 \u043d\u0430 \u0433\u0440\u0430\u0444\u0438\u043a\u0430\u0445", None))
        self.But_View_Koef_Dens_Poro.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b Dens=f(Poro)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0430\u0444\u0438\u043a\u0438 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 \u0424\u0415\u0421", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

