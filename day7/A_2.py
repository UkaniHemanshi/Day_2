class book:
    title = ""
    author = ""
    year = ""
    available = ""

    def __init__(self,title1,author1,year1,available1):
        self.title = title1
        self.author = author1
        self.year = year1
        self.available = available1


    def display_details(self):
        print(f"book_title:{self.title}\nbook_author:{self.author}\npublish_year:{self.year} \n ")

    def borrow_book(self):
        if self.available == True:
            print(f"The book {self.title} is available")
        else:
            self.available = False

    def return_book(self):
        if self.available == True:
            print(f"Book {self.title} has been returned")
        else:
            self.available = False


if __name__ == '__main__':

    book1 = book("ThePower","Joseph Murphy",2001,True)
    book2 = book("It Ends With Us","Sachin",2014,False)


    book1.display_details()
    book2.display_details()

    book1.borrow_book()
    book2.borrow_book()

    book1.return_book()
    book2.return_book()