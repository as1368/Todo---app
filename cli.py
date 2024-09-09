import functions
import time

now=time.strftime("%b %d, %Y %H:%M:%S")
print("it is ",now)
while True:
    user_in = input("enter add or show or exit or edit or complete")
    user_in = user_in.strip()

    if user_in.startswith('add'):
        todo = user_in[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)


    elif user_in.startswith('edit'):
        try:
            number = int(user_in[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("enter the new todo")
            todos[number] = new_todo + '\n'

            functions.write_todos( todos)
        except ValueError:
            print("your command is not valid")
            continue


    elif user_in.startswith('show'):
        todos = functions.get_todos()

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            index = index + 1
            row = f"{index}-{item}"
            print(row)
    elif user_in.startswith('complete'):
        try:
            num = int(user_in[9:])

            todos = functions.get_todos()
            index = num - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            functions.write_todos( todos)

            message = f"The todo {todo_to_remove} was removed from list"
            print(message)
        except IndexError:
            print("there is no item as such")
            continue

    elif user_in.startswith('exit'):
        break
    else:
        print("command is not valid")

print("bye")
