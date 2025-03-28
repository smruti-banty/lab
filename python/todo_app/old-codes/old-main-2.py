todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    match user_action.strip():
        case "add":
            todos.append(input("Enter a todo: "))

        case "show":
            for todo in todos:
                print(todo.title())

        case "edit":
            user_selection = int(input("Number of todo you want to edit: "))
            todo_index = user_selection - 1
            todos[todo_index] = input("Enter the new todo: ")

        case "exit":
            break

        case _:
            print("Enter a valid choice!")

print("Bye!")