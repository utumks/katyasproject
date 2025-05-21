from functions import *
from fr import *

tasks = ""

print("Привет, Я - органайзер. Могу помочь управлять твоими заданиями.")

while True:
    print("\nЧем могу помочь?")
    print("1. Добавить новое задание")
    print("2. Посмотреть список заданий")
    print("3. Отметить задание как выполненное")
    print("4. Удалить задание")
    print("5. Найти задание по ключевому слову")
    print("6. Закончить")

    choice = input("Ваш выбор: ")
    if choice == "1":
        tasks = new(tasks)
    elif choice == "2":
        tasks = tasklist(tasks)
    elif choice == "3":
        tasks = tick(tasks)
    elif choice == "4":
        tasks = delete(tasks)
    elif choice == "5":
        tasks = find(tasks)
    elif choice == "6":
        print("Спасибо за использование бота! Удачного дня!")
        break
    else:
        print("Некорректный ввод, попробуйте снова.")