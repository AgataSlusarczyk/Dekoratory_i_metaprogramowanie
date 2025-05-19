def box_decorator(func):
    def wrapper(*args, **kwargs):
        print("📦 Otwieram pudełko...")
        result = func(*args, **kwargs)
        print("📦 Zamykam pudełko...")
        return result
    return wrapper

@box_decorator
def give_gift(gift):
    print(f"🎁 Oto twój prezent: {gift}!")
    return f"Prezent '{gift}' został wręczony."

give_gift("książka")

# Oczekiwany wynik:
# 📦 Otwieram pudełko...
# 🎁 Oto twój prezent: książka!
# 📦 Zamykam pudełko...