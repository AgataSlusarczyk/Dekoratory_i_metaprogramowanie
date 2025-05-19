def box_decorator(func):
    def wrapper(*args, **kwargs):
        print("📦 Otwieram pudełko...")
        func(*args, **kwargs)
        print("📦 Zamykam pudełko...")
    return wrapper

def give_gift(gift):
    print(f"🎁 Oto twój prezent: {gift}!")

d = box_decorator(give_gift)
d("książka")

# Oczekiwany wynik:
# 📦 Otwieram pudełko...
# 🎁 Oto twój prezent: książka!
# 📦 Zamykam pudełko...