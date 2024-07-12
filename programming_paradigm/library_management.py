class Test:
    def __init__(self):
        pass

    def return_book(self):
        return True
        
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:     
    def __init__(self, books = {}, checkouts = {}):
        self.books = books
        self.checkouts = checkouts

    def add_book(self,title_and_book):
        title_book_dict = {title_and_book.title: title_and_book.author}
        self.books.update(title_book_dict)

    def check_out_book(self, title):
        if title in self.books:
            title_book_dict = {title: self.books[title]}
            self.checkouts.update(title_book_dict)
            self.books.pop(title)
    
    def return_book(self, title):
        if title in self.checkouts:
            title_book_dict = {title : self.checkouts[title] }
            self.books.update(title_book_dict)
            self.checkouts.pop(title)

    def list_available_books(self):
        for i in self.books:
            checker_text = f"{i} by {self.books[i]}"
            print(checker_text)