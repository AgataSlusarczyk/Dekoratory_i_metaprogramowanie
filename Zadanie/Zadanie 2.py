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

        # TODO: Wywołaj oryginalną funkcję 'func' z przekazanymi argumentami i zapisz jej wynik.

        # TODO: Zapisz aktualny czas po wywołaniu funkcji.

        # TODO: Oblicz różnicę między 'end' a 'start', aby uzyskać czas wykonania.

        # TODO: Wypisz czas wykonania w konsoli, używając formatu z przykładu.
        # Użyj nazwy funkcji i zmierzonego czasu .
        # Sformatuj czas do 6 miejsc po przecinku.

        # TODO: Zwróć wynik oryginalnej funkcji

    return wrapper

@measure_time
def slow_function():
    """Symuluje operację zajmującą czas."""
    time.sleep(1)
    return "Gotowe!"

print("Wywołuję slow_function...")
slow_function()
print("slow_function zakończona.")
