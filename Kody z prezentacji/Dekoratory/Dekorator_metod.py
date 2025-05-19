def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Przed wywołaniem funkcji") # W kontekście metody: Przed wywołaniem metody
        res = func(self, *args, **kwargs)
        print("Po wywołaniu funkcji") # W kontekście metody: Po wywołaniu metody
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello!")
        return "Metoda wykonana"

obj = MyClass()
obj.say_hello()

# Oczekiwany wynik:
# Przed wywołaniem funkcji
# Hello!
# Po wywołaniu funkcji