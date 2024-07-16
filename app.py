import add_remove_view_book_file
import search_book
import backup_restore_file
import lent_return_view_book_file

book_list = []

book_lent_info = []


# ---------------------------------------------------------------------------

menu_text = (
    "\n"
    + "-" * 75
    + """

Welcome to NHK Library Management System!

Choose an option:
1. Add book
2. View all books
3. Search book by title or ISBN
4. Search book by author
5. Remove book searching by title
6. Lent book
7. View Lent books
8. Return book
0. Exit
"""
)

book_list = backup_restore_file.restore_books(book_list)
book_lent_info = backup_restore_file.restore_lent_info(book_lent_info)

while True:
    print(menu_text)

    try:
        choice = int(input("Enter your option: "))
        options = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        if choice not in options:
            print("\nIncorrect option! Please choose a correct option.")
            continue

        if choice == 0:
            break
        elif choice == 1:
            book_list = add_remove_view_book_file.add_book(book_list)
        elif choice == 2:
            add_remove_view_book_file.view_all_books(book_list)
        elif choice == 3:
            search_book.search_book_title_isbn(book_list)
        elif choice == 4:
            search_book.search_book_author(book_list)
        elif choice == 5:
            book_list = add_remove_view_book_file.remove_book(book_list)
        elif choice == 6:
            book_list, book_lent_info = lent_return_view_book_file.lent_book(
                book_list, book_lent_info
            )
        elif choice == 7:
            lent_return_view_book_file.view_lent_books(book_lent_info)
        elif choice == 8:
            book_list, book_lent_info = lent_return_view_book_file.return_book(
                book_list, book_lent_info
            )

    except ValueError:
        print("\nOption number should be an integer!!!")
