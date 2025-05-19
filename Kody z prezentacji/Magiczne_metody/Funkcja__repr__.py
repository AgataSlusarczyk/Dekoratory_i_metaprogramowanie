# Tworzymy klasę Film, która będzie przechowywała informacje o tytule filmu oraz reżyserze
# usage
class Film:
    # Inicjalizator, który ustawia tytuł i reżysera
    def __init__(self, tytul, rezyser):
        self.tytul = tytul # Przechowuje tytuł filmu
        self.rezyser = rezyser # Przechowuje reżysera filmu

    # Reprezentacja tekstowa obiektu - pozwala na ładne wyświetlanie obiektu
    def __repr__(self):
        return f"Film('{self.tytul}', '{self.rezyser}')"

# Tworzymy instancję klasy Film, przypisując tytuł filmu i reżysera
film = Film(tytul="Inception", rezyser="Christopher Nolan")

# Wyświetlamy tekstową reprezentację obiektu 'film'
print(repr(film)) # Wyświetli: Film('Inception', 'Christopher Nolan')