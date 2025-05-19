# Dekorator
def my_decorator(func):
    def wrapper():
        print("Przed wywołaniem funkcji")
        func()
        print("Po wywołaniu funkcji")
    return wrapper

# Funkcja do udekorowania
@my_decorator
def say_hello():
    print("Hello!")

# Wywołanie dekorowanej funkcji
say_hello()

# Oczekiwany wynik:
# Przed wywołaniem funkcji
# Hello!
# Po wywołaniu funkcji