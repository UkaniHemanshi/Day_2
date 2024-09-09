class book:

    number_of_copies_available = 0

    def __init__(self,title1,author1,year1,available1):
        self.title = title1
        self.author = author1
        self.year = year1
        self.available = available1
        book.number_of_copies_available += 1

    @staticmethod
    def message():
        print("Books are man and women bestfriend")

    @classmethod
    def get_number_of_copies(cls):
        print(f"total number of copies of {cls.number_of_copies_available}")

if __name__ == '__main__':

    book1 = book("ThePower","Joseph Murphy",2001,True)
    # book2 = book("It Ends With Us","Sachin",2014,False)

    book1.get_number_of_copies()

    book.message()