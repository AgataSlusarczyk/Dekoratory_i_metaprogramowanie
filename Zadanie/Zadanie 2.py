"""
Dekorator mierzący czas wykonania funkcji
Zaimplementuj dekorator measure_time, który zmierzy czas wykonania funkcji i wypisze go w konsoli.

Przykład wyświetlania:
Czas wykonania slow_function: 1.000123 s
"""

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        # TODO: Zapisz aktualny czas przed wywołaniem funkcji.
        start = time.time()

        # TODO: Wywołaj oryginalną funkcję 'func' z przekazanymi argumentami i zapisz jej wynik.
        result = func(*args, **kwargs)

        # TODO: Zapisz aktualny czas po wywołaniu funkcji.
        end = time.time()

        # TODO: Oblicz różnicę między 'end' a 'start', aby uzyskać czas wykonania.
        duration = end - start

        # TODO: Wypisz czas wykonania w konsoli, używając formatu z przykładu.
        # Użyj nazwy funkcji i zmierzonego czasu .
        # Sformatuj czas do 6 miejsc po przecinku.
        print(f"Czas wykonania {func.__name__}: {duration:.6f} s")

        # TODO: Zwróć wynik oryginalnej funkcji
        return result
    return wrapper

@measure_time
def slow_function():
    """Symuluje operację zajmującą czas."""
    time.sleep(1)
    return "Gotowe!"

print("Wywołuję slow_function...")
slow_function()
print("slow_function zakończona.")