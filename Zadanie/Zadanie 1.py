"""
Dekorator logujący wywołania funkcji
Napisz dekorator log_calls, który wypisuje w konsoli informację o każdym wywołaniu funkcji, 
wraz z jej argumentami i wynikiem

Przykład wyniku:
Wywołano: add((2, 3), {}) -> 5

"""



#Rozwiązanie
def log_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Wywołano: {func.__name__}({args}, {kwargs}) -> {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

add(2, 3)

