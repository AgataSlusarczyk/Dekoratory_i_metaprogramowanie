"""
Dekorator logujący wywołania funkcji
Napisz dekorator log_calls, który wypisuje w konsoli informację o każdym wywołaniu funkcji, 
wraz z jej argumentami i wynikiem

Przykład wyniku:
Wywołano: add((2, 3), {}) -> 5

"""

def log_calls(func):
    def wrapper(*args, **kwargs):
        # TODO: Wywołaj oryginalną funkcję 'func' z przekazanymi argumentami i zapisz jej wynik
        result = func(*args, **kwargs)

        # TODO: Wypisz w konsoli informację zgodną z przykładem wyniku.
        # Użyj nazwy funkcji, argumentów i zapisanego wyniku (result)
        print(f"Wywołano: {func.__name__}({args}, {kwargs}) -> {result}")

        # TODO: Zwróć wynik oryginalnej funkcji
        return result
    return wrapper

@log_calls
def add(a, b):
    """Prosta funkcja dodająca dwie liczby."""
    return a + b

add(2, 3)
add(a=5, b=7)
add(10, b=20)

