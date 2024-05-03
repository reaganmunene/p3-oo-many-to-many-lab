class Author:

    members = []

    def __init__(self, name):
        self.name = name
        self.__class__.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class")
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    pass


class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.__class__.members.append(self)

    pass


class Contract:

    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("The author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise Exception("The book must be an instance of the Book class")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.__class__.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.members if contract.date == date]
    pass
