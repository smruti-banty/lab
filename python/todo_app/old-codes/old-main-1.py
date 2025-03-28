# Section 4
todos = []

while True:
    user_action = input("Type add, show or exit: ")
    match user_action.strip():
        case "add" | "insert":
            todos.append(input("Enter a todo: "))
        case "show":
            print(todos)
        case "exit":
            break
        case _: # We can use any variable instead of _ like whatever
            print("Enter a valid choice")
print("Bye!")


# Section 3
# todos = []
#
# while True:
#     todos.append(input("Enter a todo"))

# Section 2
# user_prompt = "Enter a todo: "
# todo1 = input(user_prompt)
# todo2 = input(user_prompt)
# todo3 = input(user_prompt)
#
# todos = [todo1, todo2, todo3]
# print(todos)
# print(type(todos))


# Section 1
# user_prompt = "Enter a todo: "
# todo = input(user_prompt)
# print(todo)