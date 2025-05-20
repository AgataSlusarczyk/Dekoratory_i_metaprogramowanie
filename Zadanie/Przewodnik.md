## Zad1
Dekorator logujący wywołania funkcji
Napisz dekorator log_calls, który wypisuje w konsoli informację o każdym wywołaniu funkcji, 
wraz z jej argumentami i wynikiem

Przykład wyniku:
Wywołano: add((2, 3), {}) -> 5

## Zad2
Dekorator mierzący czas wykonania funkcji
Zaimplementuj dekorator measure_time, który zmierzy czas wykonania funkcji i wypisze go w konsoli.

Przykład wyświetlania:
Czas wykonania slow_function: 1.000123 s

## Zad3
napisz funkcję , która dekorując jakąś klasę , zmieni nazwy zmienncyh na odwrót

przykład:
jeśli jakaś klasa ma zmienne :name,age
to po dekoracji powinna mieć zmienne :eman,ega

UWAGA:
na potrzeby zadania zakładamy że urzytkownik nie tworzy zmiennych zaczynających się i kończących __ (podwójną podłogą)
stare zmienne powinny być usunięte!! urzytkownik nie powinien korzystać ze starych zmiennych!!
nie zmieniaj zmiennych magicznych!!

Użyj cls.__dict__!!

## Zad4
Stwórz klasę MyTuple(x1, x2, ..., xn)  która zwraca wartość x, t.ż.
x.a == x1, x.b == x2 etc. n może być dowolne, z zakresu 0..26. Innymi słowy,
musisz stworzyć krotkę indeksowaną literami z zakresu abcdefghijklmnopqrstuvwxyz, a nie liczbami.

jeśli urzytkownik poda dla przykładu 3 zmienne i będzie chciał odczytać 4, zwróć AttributeError
jeśli urzytkownik poda zbyt dużą ilość zmiennych przekraczającą 26 liczb, zwróć IndexError

Użyj self._data
