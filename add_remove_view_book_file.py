import backup_restore_file


def add_book(book_list):
    title = input("Enter book title: ")
    authors = input("Enter author(s), separate with comma: ")
    isbn = input("Enter ISBN: ")
    while True:
        try:
            publishing_year = int(input("Enter publishing year: "))
            break
        except ValueError:
            print("The publishing year should be an integer.")
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("The price should be a float.")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("The quantity should be an integer.")

    new_book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "publishing year": publishing_year,
        "price": price,
        "quantity": quantity,
    }

    book_list.append(new_book)
    backup_restore_file.backup_books(book_list)

    print(f"\nBook ({title}) added successfully!")
    return book_list


def remove_book(book_list):
    search_term = input("Enter book title to remove: ")
    found = False
    index_checklist = []

    for index, book in enumerate(book_list):
        if search_term.lower() in book["title"].lower():
            found = True
            print("_" * 40)
            print()
            print(
                f"Book ID: {index+1}",
                f"Book title: {book['title']}",
                f"Author(s): {book['authors']}",
                f"ISBN: {book['isbn']}",
                f"Publishing year: {book['publishing year']}",
                f"Price: {book['price']}",
                f"Quantity: {book['quantity']}",
                sep="\n",
            )
            index_checklist.append(index + 1)

    if not found:
        print("\nThe book is not found!")
        return

    while True:
        try:
            selected_index = int(input("\nEnter book ID to remove: "))
            if selected_index not in index_checklist:
                print("Invalid book ID! Please enter correct book ID.")
                continue
            break
        except ValueError:
            print("The book ID should be an integer.")

    removed_book = book_list.pop(selected_index - 1)
    backup_restore_file.backup_books(book_list)

    print(f"\nThe book ({removed_book['title']}) is removed successfully!")
    return book_list


def view_all_books(book_list):
    for book in book_list:
        print("_" * 40)
        print()
        print(
            f"Book title: {book['title']}",
            f"Author(s): {book['authors']}",
            f"ISBN: {book['isbn']}",
            f"Publishing year: {book['publishing year']}",
            f"Price: {book['price']}",
            f"Quantity: {book['quantity']}",
            sep="\n",
        )
