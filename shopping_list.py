shopping_list = []

while True:
    print("add / remove / show / done")
    action = input("Choose an action: ")

    if action == "add":
        item = input("Enter an item to add: ")
        shopping_list.append(item)
    elif action == "remove":
        item = input("Enter an item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("That item is not on your list.")
    elif action == "show":
        for item in shopping_list:
            print(item)
    elif action == "done":
        print("Goodbye!")
        break