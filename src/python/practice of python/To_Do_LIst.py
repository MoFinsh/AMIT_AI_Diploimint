to_do_list = {}      # a dictionary of tasks and the key is the rtask number

def load_tasks():
    try:
        with open("tasks.txt", "r",encoding="utf-8") as file:
            to_do_list.clear()
            for i, line in enumerate(file, start=1):
                line = line.strip()
                to_do_list[i] = line
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w",encoding="utf-8") as file:
        for task_num, task in to_do_list.items():
            file.write(f"{task_num} : {task}\n")

def add_task():           # function add tasks for my dictionary
    task_number = len(to_do_list)+1
    try:
        total_tasks = int(input('how many tasks do you want to add? '))
        if total_tasks <= 0:
            print("please enter a positive number")
        else:
            for task in range(1, total_tasks+1):
                add = input('add your task')

                while task_number in to_do_list:
                    task_number += 1
                to_do_list[task_number] = add
                task_number += 1
    except ValueError:
        print("please enter a valid number")

    print("-"*10)
    print('your tasks is ')
    for task_num , task in to_do_list.items():
        print(f"{task_num} : {task}")
    print("-"*10)

def show_all_tasks():             # function show my tasks in dictionary
    if not to_do_list:
        print("no tasks were added")
    for task_num , task in to_do_list.items():
        print(f"{task_num} : {task}")

def delete_task():                   # function delete a task from my dictionary
    print("-" * 10)
    print('your tasks is ')
    for task_num, task in to_do_list.items():
        print(f"{task_num} : {task}")
    choice = int(input('Enter task number you want to delete: '))
    if 1<= choice <= len(to_do_list):
        print('your task is ')
        print(f"{choice} : {to_do_list[choice]}")
        check = input("you realy want to delete the task (yes/no): )")
        if check == 'yes':
            del to_do_list[choice]

            new_dict = {}
            new_key = 1
            for task in to_do_list.values():
                new_dict[new_key] = task
                new_key += 1
            to_do_list.clear()
            to_do_list.update(new_dict)

            print("your tasks deleted successfully")
        else:
            print("canceled")
    else:
        print("no task has this number")


load_tasks()
while True:
    save_tasks()
    print('To Do list menu\n 1. add a task\n 2. delete a task\n 3. show all tasks\n 4. quiet')
    order = input('Enter your choice: ')
    print('-'*10)

    if order ==  '1':
        add_task()
    elif order == '2':
        delete_task()
    elif order == '3':
        show_all_tasks()
    if order == '4':
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice, please enter 1, 2, 3, or 4.")