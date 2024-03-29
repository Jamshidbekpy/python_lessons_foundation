import re

def password_tekshir(parol):
    # Parol uchun quyidagi talablar:
    # 1. Kamida 8 ta belgi
    # 2. Kamida bitta katta harf
    # 3. Kamida bitta kichik harf
    # 4. Kamida bitta raqam
    # 5. Maxfiy belgilar (masalan, !, @, #, $, %, ^, &, *)

    if len(parol) < 8:
        return False

    # Katta harfni tekshirish
    if not re.search("[A-Z]", parol):
        return False

    # Kichik harfni tekshirish
    if not re.search("[a-z]", parol):
        return False

    # Raqamni tekshirish
    if not re.search("[0-9]", parol):
        return False

    # Maxfiy belgilarni tekshirish
    if not re.search("[!@#$%^&*]", parol):
        return False

    return True

# Test qilish
parol1 = "Abcdefg1@"
parol2 = "password"
parol3 = "Abcd1234"
parol4 = "Abcdefg1" # Maxfiy belgi yo'q
parol5 = "ABCDEFG1@" # Kichik harf yo'q
parol6 = "abcdefg1@" # Katta harf yo'q
parol7 = "Abcdefg123" # Maxfiy belgi yo'q

print(password_tekshir(parol1))  # True
print(password_tekshir(parol2))  # False
print(password_tekshir(parol3))  # False
print(password_tekshir(parol4))  # False
print(password_tekshir(parol5))  # False
print(password_tekshir(parol6))  # False
print(password_tekshir(parol7))  # False
"""
    # 8600 6800 0000 0000
    # 
    # 8600680000000000
"""
reg_card = r'^(\d{4}[\s]?){3}\d{4}$'  
card = input('Enter card number: ')
print(re.match(reg_card,card))
reg = r'^\w'
print(re.match(reg,'&'))
