import numpy as np


class Koef_fes:
    def __init__(self, n=30, min_koef_fes=0, max_koef_fes=1):
        """
        :param n_koef_fes: количество интервалов, на которые разбивается диапазон изменения коэфициента
        :param min_koef_fes: минимальная возможная величина коэффициента
        :param max_koef_fes: максимальная возможная величина коэффициента
        """
        # диапазоны изменения параметров
        self.var_koef_fes = np.linspace(min_koef_fes, max_koef_fes, n)
        self.n_koef_fes = n
        self.num_koef_fes = 0


def calk_function_perm(a, b, c, x):
    return 2.71 ** (a * (x ** b) - c)


def calk_function_density(a, b, x):
    return a * x + b
