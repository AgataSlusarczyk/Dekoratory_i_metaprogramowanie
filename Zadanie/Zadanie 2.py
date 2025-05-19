# Rozwiązanie ćwiczenia: Dekorator mierzący czas wykonania funkcji

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        # TODO: Zapisz aktualny czas przed wywołaniem funkcji.
        start = time.time()

        # TODO: Wywołaj oryginalną funkcję 'func' z przekazanymi argumentami
        # i zapisz jej wynik. -> POPRAWIONE
        result = func(*args, **kwargs)

        # TODO: Zapisz aktualny czas po wywołaniu funkcji.
        end = time.time()

        # TODO: Oblicz różnicę między 'end' a 'start', aby uzyskać czas wykonania.
        duration = end - start

        # TODO: Wypisz czas wykonania w konsoli, używając formatu z przykładu.
        # Użyj nazwy funkcji (func.__name__) i zmierzonego czasu (duration).
        # Sformatuj czas do 6 miejsc po przecinku. -> POPRAWIONE
        print(f"Czas wykonania {func.__name__}: {duration:.6f} s")

        # TODO: Zwróć wynik oryginalnej funkcji
        return result
    return wrapper

@measure_time
def slow_function():
    """Symuluje operację zajmującą czas."""
    time.sleep(1) # Czekaj 1 sekundę
    return "Gotowe!"

print("Wywołuję slow_function...")
slow_function()
print("slow_function zakończona.")