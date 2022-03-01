class Laskija:
    """Luokka, joka toteuttaa eri laskutoimituksia.
    Julkiset metodit:
        summaa(Union[int, float], Union[int, float])
        kerro(Union[int, float], Union[int, float])
    """

    def summaa(self, a, b):
        """Palauttaa kahden luvun summan.
        :param a: summan ensimmäinen luku
        :type a: Union[int, float]
        :param b: summan toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b summa
        :rtype: Union[int, float]
        """
        return sum([a, b])

    def kerro(self, a, b):
        """Palauttaa kahden luvun tulon.
        :param a: tulon ensimmäinen luku
        :type a: Union[int, float]
        :param b: tulon toinen luku
        :type b: Union[int, float]
        :return: lukujen a ja b tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in [a, b]:
            tulo *= luku
        return tulo


### Lisää MonenLaskija ja argumenttien_tulostaja tähän.

class MonenLaskija(Laskija):
    """Luokka, joka toteuttaa eri laskutoimituksia.
    Julkiset metodit:
        summaa(Union[int, float])
        kerro(Union[int, float])
    """
    def summaa(self, *args):
        """Palauttaa monta luvun summan.
        :param args: summan kaikki luku
        :type args: Union[int, float]
        :return: lukujen args:ssa summa
        :rtype: Union[int, float]
        """
        return sum(args)
    
    def kerro(self, *args):
        """Palauttaa monta luvun tulon.
        :param args: tulon kaikki luku
        :type args: Union[int, float]
        :return: lukujen args:ssa tulo
        :rtype: Union[int, float]
        """
        tulo = 1
        for luku in args:
            tulo *= luku
        return tulo

def argumenttien_tulostaja(**kwargs):
    """Tulostaa sanakirjan sisällöt.
        :param kwargs: tlostaa kaikki sanakirjan sisällöt
        :type kwargs: Union[str ,int, float]
        :return: kaikki sanakirjan sisällöt
        :rtype: Union[str]
        """
    for avainsana, arvo in kwargs.items():
        print(f'Argumentin "{avainsana}" arvo on {arvo}.')
        

### Seuraavat rivit tekevät tarkistustulostukset. Älä koske niihin.

l = Laskija()
ml = MonenLaskija()

print(l.summaa(11, 31))
print(l.kerro(3, 12))
print()
print(ml.summaa(1, 2, 3, 4, 5))
print(ml.kerro(1, 2, 3, 4, 5))
print()
print(ml.summaa(1, 2, 3, 4, 5, 6, 7))
print(ml.kerro(1, 2, 3, 4, 5, 6 ,7))
print()
argumenttien_tulostaja(eka=42, toka='foo', kolmas=[0, 1, 2])
print()
argumenttien_tulostaja(nimi='Tero', ika=41, kaupunki='Turku', oppilaitos='TAI')
