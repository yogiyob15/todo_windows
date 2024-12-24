import function
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")
label_clock = sg.Text("", key="clock")
label = sg.Text("Enter your to-do")
textbox = sg.InputText(tooltip="Enter to-do", key="todo")
addbutton = sg.Button(key="Add",
                      mouseover_colors="LightBlue2",
                      size=3, button_text="Add",
                      tooltip="Add Todo")

listbox = sg.Listbox(values=function.get_todos(),
                     key='todos',
                     enable_events=True,
                     size=[45, 10])
edit = sg.Button("Edit", key="Edit")

complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do APP",
                   layout=[[label_clock],
                           [label],
                           [textbox, addbutton],
                           [listbox , edit, complete_button],
                           [exit_button]],
                   font=("Helvetica",20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            function.update_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                todo_to_update = values['todo'] + '\n'

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = todo_to_update
                function.update_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first", font=("Helvetica",20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_complete)
                function.update_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value= "")
            except IndexError:
                sg.popup("Please select a todo first", font=("Helvetica",20))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

