class Magia:
    def __getattr__(self, name):
        print(f"Próba odczytu: {name}")
        return f"Wartość domyślna dla '{name}'"

    def __setattr__(self, name, value):
        print(f"Ustawianie: {name} = {value}")
        super().__setattr__(name, value)

m = Magia()
print(m.nie_istnieje)  # Próba odczytu: nie_istnieje
m.nowy = 123           # Ustawianie: nowy = 123
