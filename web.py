import streamlit as st
import function


todos = function.get_todos()
def add_todo():
    inner_todo = st.session_state["new_todo"] + "\n"
    todos.append(inner_todo)
    function.update_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.pop(index)
        function.update_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo..", key="new_todo", on_change=add_todo)
st.session_state