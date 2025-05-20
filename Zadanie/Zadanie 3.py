"""
napisz funkcję , która dekorując jakąś klasę , zmieni nazwy zmienncyh na odwrót

przykład:
jeśli jakaś klasa ma zmienne :name,age
to po dekoracji powinna mieć zmienne :eman,ega

UWAGA:
na potrzeby zadania zakładamy że urzytkownik nie tworzy zmiennych zaczynających się i kończących __ (podwójną podłogą)
stare zmienne powinny być usunięte!! urzytkownik nie powinien korzystać ze starych zmiennych!!
nie zmieniaj zmiennych magicznych!!

Użyj cls.__dict__!!
"""


def reverse_attributes(cls):
    

def TEST():
    @reverse_attributes
    class A:
        alan = "pawel"
        test = "example"
    a = A()
    assert a.nala=="pawel"
    assert a.tset=="example"
    try:
        a.alan
    except Exception as e:
        isinstance(e,AttributeError)
    print("OK")
TEST()
