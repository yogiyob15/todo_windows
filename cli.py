# from function import get_todos, update_todos

import function
import time

while True:
    user_action = input("Type add,show,edit,complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close() #

        todos = function.get_todos()

        todos.append(todo + '\n')

        # file = open("todos.txt",'w')
        # file.writelines(todos)
        # file.close()

        function.update_todos(todos)

    elif user_action.startswith("show"):
        todos = function.get_todos()

        # for_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            out = f"{index+1}-{item}"
            print(out)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = function.get_todos()

            new_todos = input("Enter updated todo: ")
            todos[number] = new_todos+ '\n'

            function.update_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = function.get_todos()

            todo_remove = todos[number].strip('\n')
            todos.pop(number)

            function.update_todos(todos)

            message = f"Todos {todo_remove} was successfully completed"
            print(message)
        except IndexError:
            print("No item found")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Please try again! ")

print("Bye")


