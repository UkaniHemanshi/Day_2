class book:

    title = ""
    author = ""
    year = ""
    available = ""

    def display_details(self):
        print(f"book_title:{self.title}\nbook_author:{self.author}\npublish_year:{self.year} \n ")

    def borrow_book(self):
        if self.available==True:
            print("The book is available")
        else:
            self.available = False

    def return_book(self):
        if self.available == True:
            print("Book has been returned")
        else:
            self.available = False



if __name__ == '__main__':
    book1 = book()
    book1.title = "THE POWER"
    book1.author = "Joseph Murphy"
    book1.year = 2001
    book1.available = False


    book2 = book()
    book2.title = "Zerp"
    book2.author = "Hemanshi"
    book2.year = 2024
    book2.available = True

    book1.display_details()
    book2.display_details()

    book1.borrow_book()
    book2.borrow_book()

    book1.return_book()
    book2.return_book()