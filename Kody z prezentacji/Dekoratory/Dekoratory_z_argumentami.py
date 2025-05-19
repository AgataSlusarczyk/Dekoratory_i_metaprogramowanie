# Funkcja zewnetrzna, która przyjmuje argumenty dla dekoratora
def repeat(x):
    # Funkcja zagniezdzona, która jest wlasciwym dekoratorem
    def decorator(fun):
        # Funkcja wewnetrzna, która opakowuje oryginalna funkcję (wrapper)
        def inner(*args, **kwargs):
            # Petla powtarzajaca wywolanie funkcji
            for i in range(x):
                fun(*args, **kwargs) # Wywolanie oryginalnej funkcji z przekazanymi argumentami
        return inner
    return decorator

@repeat(3) # Zastosowanie dekoratora z argumentem 3
def helloFunction():
    print('Hello')

helloFunction() # Wywolanie udekorowanej funkcji

# Oczekiwany wynik:
# Hello
# Hello
# Hello