'''
Задание 1. Напишите программу, которая запрашивает имя и возраст пользователя, 
и выводит приветствие и возраст пользователя в следующем году. 
Пример работы программы:
Как тебя зовут? Катя
Привет, Катя!
Сколько тебе лет? 14
Здорово! В следующем году тебе будет 15!


name = input(f"Как тебя зовут? ")
print(f"Привет, {name}!")

age = int(input(f"Сколько тебе лет? "))
print(f"Здорово! В следующем году тебе уже будет {age+1}!")



Задание 2. Напишите программу, которая запрашивает имя, фамилию и возраст пользователя, а затем выводит эти данные в столбик с помощью f-строки. Результат работы программы:

        
Имя: Евгения
Фамилия: Фролова
Возраст: 19


first_name = input("Ваше имя: ")
last_name = input("Ваша фамилия: ")
age = input("Ваш возраст: ")

print(f"Имя: {first_name}\nФамилия: {last_name}\nВозраст: {age}")
'''