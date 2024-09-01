import backup_restore_file


def lent_book(book_list, book_lent_info):
    search_term = input("Enter book title to lent: ")
    found = False
    index_checklist = []

    for index, book in enumerate(book_list):
        if search_term.lower() in book["title"].lower() and book["quantity"] > 0:
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
        print("\nThe book is not available!")
        return

    while True:
        try:
            selected_index = int(input("\nEnter book ID to lent: "))
            if selected_index not in index_checklist:
                print("Invalid book ID! Please enter correct book ID.")
                continue
            break
        except ValueError:
            print("The book ID should be an integer.")

    borrower_name = input("Enter borrower's name: ")
    new_item = {
        "borrower": borrower_name,
        "title": book_list[selected_index - 1]["title"],
        "authors": book_list[selected_index - 1]["authors"],
        "isbn": book_list[selected_index - 1]["isbn"],
    }

    book_lent_info.append(new_item)
    book_list[selected_index - 1]["quantity"] -= 1
    backup_restore_file.backup_books(book_list)
    backup_restore_file.backup_lent_info(book_lent_info)

    print(f"\nThe book ({new_item['title']}) is lent to {borrower_name}!")
    return book_list, book_lent_info


def return_book(book_list, book_lent_info):
    search_borrower = input("Enter name of borrower: ")
    found = False
    index_checklist = []

    for index, book in enumerate(book_lent_info):
        if search_borrower.lower() in book["borrower"].lower():
            found = True
            print("_" * 40)
            print()
            print(
                f"Borrow ID: {index+1}",
                f"Borrower: {book['borrower']}",
                f"Book title: {book['title']}",
                f"Author(s): {book['authors']}",
                f"ISBN: {book['isbn']}",
                sep="\n",
            )
            index_checklist.append(index + 1)

    if not found:
        print("\nThe borrower is not found!")
        return

    while True:
        try:
            selected_index = int(input("\nEnter borrow ID of the book to return: "))
            if selected_index not in index_checklist:
                print("Invalid borrow ID! Please enter correct borrow ID.")
                continue
            break
        except ValueError:
            print("The borrow ID should be an integer.")

    returned_book = book_lent_info.pop(selected_index - 1)

    found = False
    for index, book in enumerate(book_list):
        if (
            returned_book["title"].lower() in book["title"].lower()
            and returned_book["isbn"].lower() in book["isbn"].lower()
        ):
            found = True
            book_list[index]["quantity"] += 1
            break

    if not found:
        print("\nThe book is not found in the book list!")

    backup_restore_file.backup_books(book_list)
    backup_restore_file.backup_lent_info(book_lent_info)

    print(f"\nThe book ({returned_book['title']}) is returned successfully!")
    return book_list, book_lent_info


def view_lent_books(book_lent_info):
    for book in book_lent_info:
        print("_" * 40)
        print()
        print(
            f"Borrower: {book['borrower']}",
            f"Book title: {book['title']}",
            f"Author(s): {book['authors']}",
            f"ISBN: {book['isbn']}",
            sep="\n",
        )
