"""
Stwórz klasę MyTuple(x1, x2, ..., xn)  która zwraca wartość x, t.ż.
x.a == x1, x.b == x2 etc. n może być dowolne, z zakresu 0..26. Innymi słowy,
musisz stworzyć krotkę indeksowaną literami z zakresu abcdefghijklmnopqrstuvwxyz, a nie liczbami.

jeśli urzytkownik poda dla przykładu 3 zmienne i będzie chciał odczytać 4, zwróć AttributeError
jeśli urzytkownik poda zbyt dużą ilość zmiennych przekraczającą 26 liczb, zwróć IndexError

Użyj self._data
"""

class MyTuple:
    
def TEST():
    t = MyTuple("ff", 2, 3)
    assert t.a == "ff" and t.b == 2 and t.c == 3
    try:
        t.d
    except AttributeError as a:
        isinstance(a,AttributeError)
    try :
        t = MyTuple(*range(0, 27))
    except Exception as  a:
        isinstance(a,IndexError)
    print("OK")
TEST()
