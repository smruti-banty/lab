todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    match user_action.strip():
        case "add":
            todos.append(input("Enter a todo: "))

        case "show":
            for index, todo in enumerate(todos):
                print(f"{index}-{todo}")

        case "edit":
            user_selection = int(input("Number of todo you want to edit: "))
            todo_index = user_selection - 1
            todos[todo_index] = input("Enter the new todo: ")

        case "complete":
            user_selection = int(input("Number of todo you want to complete: "))
            todos.pop(user_selection - 1)
            print("🎉 Wohoo! Task successfully completed! 🚀")
        case "exit":
            break

        case _:
            print("Enter a valid choice!")

print("Bye!")