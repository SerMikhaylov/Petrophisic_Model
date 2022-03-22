import matplotlib

matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, xlabel='x', ylabel='y', title='Title', width=5, height=4, dpi=100, xmin=0, xmax=5,
                 ymin=0.1, ymax=10):
        """
        :param width: ширина графика
        :param height: высота графика
        # :param x_min: минимальное значение параметра по оси Х
        # :param x_max: максимальное значение параметра по оси Х
        # :param y_min: минимальное значение параметра по оси Y
        # :param y_max: максимальное значение параметра по оси Y
        :param dpi:
        """

        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set(facecolor="#6272a4")
        self.axes = fig.add_subplot(111)
        self.axes.grid(True, c='lightgrey', alpha=0.5)
        self.axes.set_title(title, fontsize=9)
        self.axes.set_xlabel(xlabel, fontsize=8)
        self.axes.set_ylabel(ylabel, fontsize=8)
        self.axes.set_xlim(xmin, xmax)
        self.axes.set_ylim(ymin, ymax)
        super(MplCanvas, self).__init__(fig)
