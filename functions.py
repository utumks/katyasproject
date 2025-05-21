def new(tasks):
    task_name = input("Введите название задания: ")
    deadline = input("Введите крайний срок (например, 10.12.2024): ")
    priority = input("Введите важность (! - обычное, !! - выполнить поскорее, !!! - срочное): ")

    if len(tasks) == 0:
        tasks = "[ ] " + task_name + " (до " + deadline + ") " + priority
    else:
        tasks += "\n[ ] " + task_name + " (до " + deadline + ") " + priority
    print("Задание добавлено")
    return tasks

def tasklist(tasks):
    if len(tasks) == 0:
        print("Ваш список заданий пуст")
    else:
        index = 0
        current_task = ""
        while index < len(tasks):
            if tasks[index] == "\n" or index == len(tasks) - 1:
                if index == len(tasks) - 1:
                    current_task += tasks[index]
                print(current_task)
                current_task = ""
            else:
                current_task += tasks[index]
            index += 1
    return tasks

def tick(tasks):
    if len(tasks) == 0:
        print("Ваш список заданий пуст!")
    else:
        index = 0
        task_number = 1
        print("Вот список ваших заданий:")
        while index < len(tasks):
            current_task = ""
            while index < len(tasks) and tasks[index] != "\n":
                current_task += tasks[index]
                index += 1
            print(str(task_number) + ". " + current_task)
            task_number += 1
            index += 1

        task_num = int(input("Введите номер задания для отметки как выполненное: ")) - 1
        index = 0
        current_task = ""
        task_count = 0
        updated_tasks = ""
        while index < len(tasks):
            if tasks[index] == "\n" or index == len(tasks) - 1:
                if index == len(tasks) - 1:
                    current_task += tasks[index]
                if task_count == task_num:
                    current_task = current_task.replace("[ ]", "[x]")
                updated_tasks += current_task + "\n"
                current_task = ""
                task_count += 1
            else:
                current_task += tasks[index]
            index += 1
        tasks = updated_tasks
        print("Задание отмечено как выполненное!")
    return tasks