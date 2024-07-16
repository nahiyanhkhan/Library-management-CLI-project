def search_book_title_isbn(book_list):
    search_term = input("Enter title or ISBN to search: ")
    found = False

    for book in book_list:
        if (
            search_term.lower() in book["title"].lower()
            or search_term.lower() in book["isbn"].lower()
        ):
            found = True
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

    if not found:
        print("\nThe book is not found!")


def search_book_author(book_list):
    search_term = input("Enter author name to search: ")
    found = False

    for book in book_list:
        if search_term.lower() in book["authors"].lower():
            found = True
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

    if not found:
        print("\nThe information related to author is not found!")
