import random
import time


class DivMul:
    def __init__(self):
        self.wynik = 0
        self.odp = 0
        self.rozmiar = 6
        self.aktualne = 1
        self.liczba_zadan = 0
        self.koniec_listy = False
        self.mnozenie = 0
        self.znak = 'x'
        self.rownanie = ''
        self.dzialania = []
        self.test = []
        self.bledy = []
        random.seed(time.time())
        random.shuffle(self.dzialania)

    def generuj_test(self, znak, liczba_testow):
        if not self.dzialania:
            for _a in range(1, self.rozmiar):
                for _b in range(1, 11):
                    self.dzialania.append([_a, _b])
        self.koniec_listy = False
        self.wynik = 0
        self.test = []
        self.bledy = []
        self.aktualne = 1
        self.liczba_zadan = 0
        self.znak = znak
        random.seed(time.time())
        random.shuffle(self.dzialania)
        self.test.clear()
        self.test.extend(self.dzialania[:liczba_testow])
        self.liczba_zadan = len(self.test)
        return self.test

    def pobierz_pytanie(self):
        if self.test:
            self.mnozenie = self.test[-1][0] * self.test[-1][1]
            if self.znak == 'x':
                self.rownanie = f'{self.test[-1][0]}{chr(215)}{self.test[-1][1]}='
            elif self.znak == ':':
                self.rownanie = f'{self.mnozenie}{chr(247)}{self.test[-1][1]}='

            if self.aktualne < self.liczba_zadan:
                self.aktualne += 1
            self.koniec_listy = False
            return True
        else:
            self.koniec_listy = True
            return False

    def sprawdz_wynik(self, odpowiedz):
        if self.znak == 'x':
            self.odp = self.mnozenie
        elif self.znak == ':':
            self.odp = int(self.mnozenie / self.test[-1][1])

        if int(odpowiedz) == self.odp:
            self.test.pop()
            self.wynik += 1
            return True
        else:
            _temp = [self.rownanie, odpowiedz, self.odp]
            self.bledy.append(_temp)
            self.test.pop()
            return False
