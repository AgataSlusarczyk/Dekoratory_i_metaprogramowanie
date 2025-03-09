"""
Dekorator mierzący czas wykonania funkcji
Zaimplementuj dekorator measure_time, który zmierzy czas wykonania funkcji i wypisze go w konsoli.

Przykład wyświetlania:
Czas wykonania slow_function: 1.000123 s
"""

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Czas wykonania {func.__name__}: {end - start:.6f} s")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(1)

slow_function()
