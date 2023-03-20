
class Cars:
    """
    Автомобили
    """
    def __init__(self, color, mark, probeg, god):
        self.cvet = color
        self.marka = mark
        self.probeg = probeg
        self.god = god

    def moove(self, km: int):
        self.probeg += km

    def printCar(self):
        print(self.marka, self.god, self.cvet, self.probeg)


class ElectroCars(Cars):
    def __init__(self, color, mark, probeg, god):
        super().__init__(color, mark, probeg, god)
    pass
