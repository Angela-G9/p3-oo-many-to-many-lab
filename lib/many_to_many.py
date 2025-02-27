class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        self._books = []

    def contracts(self):
        return self._contracts

    def books(self):
        return self._books

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)

    def __repr__(self):
        return f"<Author: {self.name}>"


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []

    def contracts(self):
        return self._contracts

    def authors(self):
        return list(set(contract.author for contract in self._contracts))

    def __repr__(self):
        return f"<Book: {self.title}>"


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of the Book class")
        if not isinstance(royalties, (int, float)):
            raise TypeError("Royalties must be a number")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add the contract to the author's and book's lists
        author._contracts.append(self)
        book._contracts.append(self)

        # Add the book to the author's list if not already present
        if book not in author._books:
            author._books.append(book)

        # Add the contract to the class-level list
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"<Contract: {self.author.name} - {self.book.title} - {self.date}>"