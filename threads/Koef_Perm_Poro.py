from PySide6 import QtCore
import itertools
from Podbor_koef import calk_function_perm


class Koef_Perm_Poro_Thread(QtCore.QThread):
    Koef_Perm_Poro_Signal = QtCore.Signal(dict)

    def setParameters(self, koef_1, koef_2, koef_3, porosity, permeability):
        self.koef_1 = koef_1
        self.koef_2 = koef_2
        self.koef_3 = koef_3
        self.porosity = porosity
        self.permeability = permeability

    def run(self) -> None:
        # todo проверить, что заданы коэффициенты
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
        self.Koef_Perm_Poro_Signal.emit(
            {
                "log": f'Perm = exp({self.koef_1.num_koef_fes}*(Poro**{self.koef_2.num_koef_fes}) - {self.koef_3.num_koef_fes})',
                "koef_1": self.koef_1,
                "koef_2": self.koef_2,
                "koef_3": self.koef_3
                }
        )
