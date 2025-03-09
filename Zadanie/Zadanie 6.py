"""
Stwórz funkcję make_mytuple(x1, x2, ..., xn) z zakresu abcdefghijklmnopqrstuvwxyz, która zwraca wartość x, t.ż.
x.a == x1, x.b == x2 etc. n może być dowolne, z zakresu 0..26. Innymi słowy,
musisz stworzyć krotkę indeksowaną literami, a nie liczbami.
"""
def make_mytuple(*args):

    pass

def TEST():
    t = make_mytuple(1, 2, 3)
    assert t.a == 1 and t.b == 2 and t.c == 3
TEST()
