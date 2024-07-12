class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def return_book(self):
        return True

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
        book_in_checkouts = title in self.checkouts
        if book_in_checkouts == True:
            title_book_dict = {title : self.checkouts[title] }
            self._books.update(title_book_dict)
            self.checkouts.pop(title)

    def list_available_books(self):
        for book_title in self._books:
            output_text = []
            output_text.append(book_title + " by "+ self._books[book_title])
            print("".join(output_text))