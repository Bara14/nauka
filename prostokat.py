import math
class prostakat:
    def __init__(self, dlugosc, szerokosc):
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def pole(self):
        pole = self.dlugosc * self.szerokosc
        return print(f"pole to: {pole}")

    def obwod(self):
        obwod = 2*self.dlugosc + 2* self.szerokosc
        return  print(f"obwod to: {obwod}")

    def przekatna(self):
        przekatna = math.sqrt(self.dlugosc**2 + self.szerokosc**2)
        return print(f"przekatna to: {przekatna}")


moj_pierwszy_prastakat = prostakat(7,4)
moj_pierwszy_prastakat.pole()
moj_pierwszy_prastakat.obwod()
moj_pierwszy_prastakat.przekatna()
