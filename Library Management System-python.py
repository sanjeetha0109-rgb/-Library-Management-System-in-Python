books = []

while True:
    print("\n1.Add  2.Display  3.Issue  4.Return  5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Book Name: ")
        books.append(name)
        print("Book added")

    elif choice == "2":
        print("Books:", books)

    elif choice == "3":
        name = input("Enter Book Name to issue: ")
        if name in books:
            books.remove(name)
            print("Book issued")
        else:
            print("Book not found")

    elif choice == "4":
        name = input("Enter Book Name to return: ")
        books.append(name)
        print("Book returned")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
