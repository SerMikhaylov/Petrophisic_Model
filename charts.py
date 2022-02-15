import matplotlib.pyplot as plt

class Chart:
    def __init__(self, title, xlabel_title, ylabel_title, width, height, x_min, x_max, y_min, y_max):
        """

        :param title: название графика
        :param xlabel_title: название оси OX
        :param ylabel_title: название оси OY
        :param width: ширина графика
        :param height: высота графика
        :param x_min: минимальное значение параметра по оси Х
        :param x_max: максимальное значение параметра по оси Х
        :param y_min: минимальное значение параметра по оси Y
        :param y_max: максимальное значение параметра по оси Y
        """
        self.title = title
        self.xlabel_title = xlabel_title
        self.ylabel_title = ylabel_title
        self.width = width
        self.height = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.chart_view = chart_view

        fig = plt.figure(figsize=(width, height))
        ax = fig.add_subplot(111)
        # plt.title(title, fontsize=22, color='blue', fontweight='bold')  # заголовок
        plt.xlabel(xlabel_title, fontsize=24, fontweight='bold')  # ось абсцисс
        plt.ylabel(ylabel_title, fontsize=24, fontweight='bold')  # ось ординат
        plt.grid(True)  # включение отображение сетки

        # диапазоны осей
        ax.set_ylim(y_min, y_max)
        ax.set_xlim(x_min, x_max)

        #  Добавляем линии основной сетки:
        ax.grid(which='major',
                color='gray',
                linestyle=':')

        # параметры легенды
        plt.legend(fontsize=24)



