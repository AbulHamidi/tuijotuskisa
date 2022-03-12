import random
from typing import List


class Asiakas:
    __nimi: str
    __asiakasnro: List[int]
    __ika: int

    def __init__(self, nimi, ika) -> None:
        self.__nimi = nimi
        self.__ika = ika
        self.__luo_nro()


    @property
    def ika(self):
        return self.__ika

    @ika.setter
    def ika(self, ika: int):
        if(ika):
            self.__ika = ika
        else:
            raise Exception("Ika on pakollinen")


    @property
    def nimi(self):
        return self.__nimi

    @nimi.setter
    def nimi(self, nimi: str):
        if(nimi):
            self.__nimi = nimi
        else:
            raise Exception("Nimi on pakollinen!!")


    @property
    def asiakasnro(self):
        return f"{str(self.__asiakasnro[0:2])}-{self.__asiakasnro[2:5]}-{self.__asiakasnro[5:9]}"

    @asiakasnro.setter
    def asiakasnro(self, asiaksnro: list[int]):
        self.__asiakasnro = asiaksnro

    def _randfixed_digit(self, digits):
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, digits)])

    def __luo_nro(self):
        self.__asiakasnro = [self._randfixed_digit(
            2), self._randfixed_digit(3), self._randfixed_digit(3)]


class Palvelu():
    tuotenimi: str
    __asiakkaat: List[Asiakas]

    def __init__(self, tuotenimi: str):
        super()
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakarivi(self, asiakas: Asiakas) -> str:
        return f"{asiakas.nimi} ({asiakas.asiakasnro}) on {asiakas.ika} vuotta vanha!"

    def lisaa_asiakas(self, asiakas: Asiakas):
        if(asiakas):
            self.__asiakkaat.append(asiakas)

        else:
            raise Exception("Asiakas on pakollinen!!")

    def poista_asiakas(self, asiakas: Asiakas):
        try:
            self.__asiakkaat.remove(asiakas)
        except:
            print("Asiakas ei loytynyt!")
            pass

    def tulosta_asiakkaat(self):
        print(f"Tuoten {self.__asiakkaat[-1]} asiakkaat ovat:")
        print(self._luo_asiakarivi)
        



class ParempiPalvelu(Palvelu):
    __edut: List[str]

    def __init__(self, tuotenimi):
        super(ParempiPalvelu, self).__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, b: str):
        if(b):
            self.__edut.append(b)
        else:
            raise Exception("Edut on pakollinen!!")

    def poista_etu(self, b: str):
        try:
            self.__edut.remove(b)
        except:
            print("ei loytynyt edut")
            pass

    def tulosta_edut(self):
        print(f"Tuoten {self.__asiakkaat} edut ovat:")
        print(f"Jauhaa {self.__edut}.")

a = Asiakas('Jompainen', random.randint(20, 30))
b = Asiakas('Suvantolainen', random.randint(70, 90))
c = Asiakas('Louheatar', random.randint(40, 60))

# Palvelu
p = Palvelu('Sammas')

p.lisaa_asiakas(a)
p.lisaa_asiakas(b)
p.tulosta_asiakkaat()

# ParempiPalvelu
pp = ParempiPalvelu('Kirjokansi')

pp.lisaa_asiakas(c)
pp.tulosta_asiakkaat()

pp.lisaa_etu('Jauhaa rahaa.')
pp.lisaa_etu('Jauhaa viljaa.')
pp.lisaa_etu('Jauhaa suolaa.')
pp.tulosta_edut()

