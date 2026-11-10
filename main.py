def parse_line(line):
    isbn, title, author, quantity, price = line.strip().split("|")
    return [isbn, title, author, int(quantity), float(price)]


def get_books(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    return list(map(parse_line, lines[1:]))


def filtered_books(books, word):
    found = filter(lambda b: word.lower() in b[1].lower(), books)
    return list(map(lambda b: [b[0], b[1] + ", " + b[2], b[3], b[4]], found))


def get_totals(books):
    return list(map(lambda b: (b[0], round(b[2] * b[3], 2)), books))


if __name__ == "__main__":
    books = get_books("books.csv")
    print(books)
    python_books = filtered_books(books, "python")
    print(python_books)
    print(get_totals(python_books))
