def delete(tasks):
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
        return tasks

        task_num = int(input("Введите номер задания для удаления: ")) - 1
        index = 0
        current_task = ""
        task_count = 0
        updated_tasks = ""
        while index < len(tasks):
            if tasks[index] == "\n" or index == len(tasks) - 1:
                if index == len(tasks) - 1:
                    current_task += tasks[index]
                if task_count != task_num:
                    updated_tasks += current_task + "\n"
                current_task = ""
                task_count += 1
            else:
                current_task += tasks[index]
            index += 1
        tasks = updated_tasks
        print("Задание удалено!")
    return tasks

def find(tasks):
    if len(tasks) == 0:
        print("Ваш список заданий пуст!")
    else:
        keyword = input("Введите ключевое слово для поиска: ").lower()
        index = 0
        current_task = ""
        found_tasks = ""
        while index < len(tasks):
            if tasks[index] == "\n" or index == len(tasks) - 1:
                if index == len(tasks) - 1:
                    current_task += tasks[index]
                if current_task.lower().find(keyword) != -1:
                    found_tasks += current_task + "\n"
                current_task = ""
            else:
                current_task += tasks[index]
            index += 1
        if len(found_tasks) > 0:
            print("Найденные задания:")
            print(found_tasks)
        else:
            print("Заданий с таким ключевым словом не найдено.")
    return tasks