''' Индекс строки
индексы:     1 2 3 4 5 6 7 8 9 10 11
         s = H e l l o   w o r l d                   даже пробел имеет свой индекс
            -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 -11

 s = "Hello World"
 Если написать s[2]
 то нам выдаст символ под номером 2
 e
  s = "Hello World"
  строка [start:stop]
 s[2:]
тогда будут указаны все символы от 4 до последнего, можно сделать и наоборот
 s[:5]

 строка [start:stop:step]

s = "Hello World"
Методы строк:
s.upper() - Делает капсом

s.lower() - Делает маленькими

String.count(sub[,start[,end]])
start - индекс, с которого начинается поиск
end - индекс, которым заканчивается поиск

s.count("llo", 4, 2) - посчитает количество в заданых границах

s.find("llo", 4, 2) - найдет где находиться (слева направо)

s.rfind("llo, 4, 2") - найдет где находиться (справа налево)

s.index(llo) - если искаемого символа не будет - выбьет ошибку

s.replace(old, new, count=1), count - макс колв. замен (-1 - бе ограничений) Команда меняет символы на другие

s.isalpha() Если строка состоит только из символов то True, если иначе то False

s.isdigit() Проверяет состоит ли строка полностью из цифр

s.rjust(width[,fillchar = '']) - Увеличивает строку на нужное количество символов , fillchar = тут пишем символ которым будем заполнять'

| Метод | Описание | Пример | Вывод |
|-------|----------|--------|-------|
| isalpha() | Только буквы? | print("abc".isalpha()) | True |
| isdigit() | Только цифры? | print("123".isdigit()) | True |
| isalnum() | Буквы и цифры? | print("abc123".isalnum()) | True |
| isspace() | Только пробелы? | print("  ".isspace()) | True |
| islower() | В нижнем регистре? | print("hello".islower()) | True |
| isupper() | В верхнем регистре? | print("HELLO".isupper()) | True |
| startswith("py") | Начинается с "py"? | print("python".startswith("py")) | True |
| endswith("on") | Заканчивается на "on"? | print("python".endswith("on")) | True |
| lower() | В нижний регистр | print("HeLLo".lower()) | hello |
| upper() | В верхний регистр | print("HeLLo".upper()) | HELLO |
| capitalize() | Первая заглавная | print("hello".capitalize()) | Hello |
| title() | Каждое слово с заглавной | print("hello world".title()) | Hello World |
| swapcase() | Меняет регистр | print("HeLLo".swapcase()) | hEllO |
| strip() | Удаляет пробелы по краям | print(" hello ".strip()) | hello |
| lstrip() | Удаляет слева | print(" hello".lstrip()) | hello |
| rstrip() | Удаляет справа | print("hello ".rstrip()) | hello |
| find("l") | Индекс подстроки | print("hello".find("l")) | 2 |
| replace("p", "*") | Заменяет | print("apple".replace("p", "*")) | a**le |
| split(",") | Делит по запятой | print("a,b,c".split(",")) | ['a', 'b', 'c'] |
| join() | Объединение | print(",".join(['a','b'])) | a,b |
| partition("=") | Делит на 3 части | print("key=value".partition("=")) | ('key', '=', 'value') |
| splitlines() | Делит по строкам | print("a\nb".splitlines()) | ['a', 'b'] |
| center(10) | По центру | print("hi".center(10)) | "    hi    " |
| ljust(10) | Влево | print("hi".ljust(10)) | "hi        " |
| rjust(10) | Вправо | print("hi".rjust(10)) | "        hi" |
| zfill(5) | Заполнение нулями | print("42".zfill(5)) | 00042 |

'''
username = input("Введите имя пользователя: ").strip()
email = input("Введите email: ").strip()
password = input("Введите пароль: ").strip()

# Проверка имени
if not username.isalpha():
    print("Имя должно содержать только буквы.")
elif not username.istitle():
    print("Имя должно начинаться с заглавной буквы.")
else:
    print("Имя принято.")

# Проверка email
if "@" not in email or not email.endswith(".com"):
    print("Некорректный email.")
else:
    print("Email принят.")

# Проверка пароля
if len(password) < 6:
    print("Пароль слишком короткий.")
elif password.islower() or password.isupper() or password.isdigit():
    print("Пароль должен содержать буквы и цифры в разном регистре.")
else:
    print("Пароль принят.")
