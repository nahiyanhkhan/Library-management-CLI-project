def backup_books(book_list):
    with open("book_list.csv", "w") as file_pointer:
        for book in book_list:
            line = f"{book['title']}|{book['authors']}|{book['isbn']}|{book['publishing year']}|{book['price']}|{book['quantity']}\n"
            file_pointer.write(line)


def restore_books(book_list):
    try:
        with open("book_list.csv", "r") as file_pointer:
            for line in file_pointer.readlines():
                line = line.strip().split("|")
                new_book = {
                    "title": line[0],
                    "authors": line[1],
                    "isbn": line[2],
                    "publishing year": int(line[3]),
                    "price": float(line[4]),
                    "quantity": int(line[5]),
                }
                book_list.append(new_book)
        return book_list

    except FileNotFoundError:
        print("The file is not found.")


def backup_lent_info(book_lent_info):
    with open("lent_info.csv", "w") as file_pointer:
        for book in book_lent_info:
            line = (
                f"{book['borrower']}|{book['title']}|{book['authors']}|{book['isbn']}\n"
            )
            file_pointer.write(line)


def restore_lent_info(book_lent_info):
    try:
        with open("lent_info.csv", "r") as file_pointer:
            for line in file_pointer.readlines():
                line = line.strip().split("|")
                new_book = {
                    "borrower": line[0],
                    "title": line[1],
                    "authors": line[2],
                    "isbn": line[3],
                }
                book_lent_info.append(new_book)
        return book_lent_info

    except FileNotFoundError:
        print("The file is not found.")
