class Sieunhan:
    suc_manh = 50
    def __init__(self, name, vu_khi, color):
        self.ten = name
        self.vukhi = vu_khi
        self.mau_sac = color


class Sieunhanteam(Sieunhan):
    def __init__(self, name, vu_khi, color, animal):
        super().__init__(name, vu_khi, color)
        self.sieuthu = animal

gaodo = Sieunhanteam("do", "kiem", "do", "su tu")

print(gaodo.__dict__)


