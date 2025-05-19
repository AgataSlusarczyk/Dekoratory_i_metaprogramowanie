# Dekorator klasy
def track_instances(cls):
    # Inicjujemy atrybut klasy, w którym będziemy przechowywać instancje
    cls._instances = []
    orig_init = cls.__init__ # Zapisujemy oryginalny konstruktor

    # Definiujemy nowy konstruktor
    def new_init(self, *args, **kwargs):
        # Wywołanie oryginalnego konstruktora
        orig_init(self, *args, **kwargs)
        # Rejestracja instancji w liście
        cls._instances.append(self)

    # Podmieniamy oryginalny konstruktor klasy
    cls.__init__ = new_init
    return cls # Zwracamy zmodyfikowaną klasę

@track_instances # Zastosowanie dekoratora klasy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Przykładowe użycie:
p1 = Person("Alice", age=30)
p2 = Person("Bob", age=25)
p3 = Person("Charlie", age=35)

# Wyświetlenie wszystkich zarejestrowanych instancji
print("Zarejestrowane instancje klasy Person:")
for instance in Person._instances:
    print(f"{instance.name}, {instance.age} lat")

# Oczekiwany wynik:
# Zarejestrowane instancje klasy Person:
# Alice, 30 lat
# Bob, 25 lat
# Charlie, 35 lat