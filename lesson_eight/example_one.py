import time


class Cars:
    """
    автомобили
    """
    def __init__(self, model, color, year, probeg):
        """инициализируем атрибуты автомобиля"""
        self.model = model
        self.color = color
        self.year = year
        self.probeg = int(probeg)

    def show_car(self):
        "вывод информации об автомобиле"
        print(self.model, self.color, self.year, self.probeg)

    def drow_car(self, km: int):
        self.probeg += km


# our_car = Cars('Lada priora', 'Black', '2008', '300000')
# our_car.show_car()
# our_car.drow_car(300)
# our_car.show_car()
class Battary():
    """батареи электрокаров"""

    def __init__(self):
        self.charge = 100
        self.srok = 7000

    def schenchik(self, km):
        count = 0
        while count < km:
            count += 1
            self.srok -= 1
            time.sleep(1)

    def charge_change(self, km):
        charge = 25
        self.charge = self.charge - (km / 100 * charge)

class ElectroCars(Cars):
    """
    Электромобили
    """
    def __init__(self, model, color, year, probeg):
        "инициализация атрибутов электромобиля"
        super().__init__(model, color, year, probeg)
        self.battary = Battary()

    def drow_car(self, km: int):
        self.battary.schenchik(km)
        self.battary.charge_change(km)
        self.probeg += km

    def show_car(self):
        print(self.model, self.color, self.year, self.probeg, self.battary.charge, self.battary.srok)




our_car = ElectroCars('Tesla', 'Black', '2013', '100000')
our_car.show_car()
our_car.drow_car(10)

our_car.show_car()

