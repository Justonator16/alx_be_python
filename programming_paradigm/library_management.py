class Test:
    def __init__(self):
        pass
        
class Book:
    def __init__(self, title = "", author = ""):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class Library:     
    def __init__(self, books = [], checkouts = []):
        self.books = list(books)
        self.checkouts = list(checkouts)

    def add_book(self,title_and_book):
        self.books.append(title_and_book)

    def check_out_book(self, title):
        # for i in range(len(self.books)):
        #     if title in self.books[i]:
        #         book = self.books[i]
        #         self.checkouts.append(book)
        #         self.books.pop(i)
        self.checkouts.append(self.books[1])
        self.books.pop(1) 

    
    def return_book(self):
        # for i in range(len(self.checkouts)):
        #     if title in self.checkouts[i]:
        #         book = self.checkouts[i]

        #         self.books.append(book)
        #         self.checkouts.pop(i)
        if self.books == True:
            self.books.append(self.checkouts[0])
            self.checkouts.pop(0)

    def list_available_books(self):
        for i in self.books:
            print(i)