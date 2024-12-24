def get_todos(filename="todos.txt"):
    """ Return a list of to do from
     a file"""
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def update_todos(todos_arg, filename="todos.txt"):
    """ Write a new to do in todo file"""
    with open(filename , 'w') as file_local:
        file_local.writelines(todos_arg)


print(__name__)

if __name__ == "__main__":
    print("Hello from functions")

