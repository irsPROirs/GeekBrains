def my_func(name, surname, birth, city, email, phone):
    print(surname, name, city, birth, phone, email)


name, surname, birth, city, email, phone = input('введите данные через пробел: ').split()
my_func(name=name, surname=surname, birth=birth, city=city, email=email, phone=phone)
