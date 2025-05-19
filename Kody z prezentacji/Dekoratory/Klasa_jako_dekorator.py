# Klasa jako dekorator
class DoubleReturnDecorator:
    def __init__(self, func):
        # Konstruktor przechowuje funkcję do udekorowania
        self.func = func

    def __call__(self, *args, **kwargs):
        # Metoda __call__ sprawia, że instancja jest wywoływalna
        # Wywołujemy oryginalną funkcję
        result = self.func(*args, **kwargs)
        # Modyfikujemy wynik i go zwracamy
        return result * 2

@DoubleReturnDecorator # Zastosowanie klasy jako dekoratora
def multiply(a, b):
    return a * b

# Użycie udekorowanej funkcji
print(multiply(3, 5))   # # (3 * 5) * 2 = 30
print(multiply(10, 20)) # # (10 * 20) * 2 = 400

# Oczekiwany wynik:
# 30
# 400