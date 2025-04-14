#Первое дз

c = input("Введите текст: ")
print(c.upper())
print(c.lower())
print(''.join(reversed(c)))

#2 дз

username = input("Введите имя").strip()
password = input("Введите пароль").strip()
email = input("Введите почту").strip()

if not username.isalpha():
    print("Имя должно содержать только буквы")
elif not username.istitle():
    print("Имя должно начинаться с заглавной буквы")
else:
    print("Имя принято")

if not email.endswith("@gmail.com"):
    print("Некорректный email")
elif not email.startswith("."):
    print("Некорректный email")
else:
    print("Email принят")

if len(password) < 8:
    print("Пароль слишком короткий")
elif not any(c.lower() for c in password) or any(c.upper() for c in password) or any(c.isdigit() for c in password):
    print("Пароль должен содержать заглавные, строчные буквы и цифры.")
else:
    print("Пароль принят.")