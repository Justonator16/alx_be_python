class Test:
    def return_book(self):
        return True
        
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:     
    def __init__(self):
        self._books = []
        self._books = {}
        self.checkouts = {}

    def add_book(self,title_and_book):
        title_book_dict = {title_and_book.title: title_and_book.author}
        self._books.update(title_book_dict)

    def check_out_book(self, title):
        if title in self._books:
            title_book_dict = {title: self._books[title]}
            self.checkouts.update(title_book_dict)
            self._books.pop(title)
    
    def return_book(self, title):
        if title in self.checkouts:
            title_book_dict = {title : self.checkouts[title] }
            self._books.update(title_book_dict)
            self.checkouts.pop(title)

    def list_available_books(self):
        for i in self._books:
            checker_text = f"{i} by {self._books[i]}"
            print(checker_text)