import webbrowser


user_term = input("Enter key to search: ")
webbrowser.open("https://google.com/search?q=" + user_term)