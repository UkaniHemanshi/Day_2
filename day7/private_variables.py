class book:

    number_of_copies_available = 0

    def __init__(self,title1,author1,year1,available1):
        self.title = title1
        self.author = author1
        self.__year = year1
        self.available = available1
        book.number_of_copies_available += 1

    def display_details(self):
        print(f"book_title:{self.title}\nbook_author:{self.author}\npublish_year:{self.__year} \n ")

    def set_year(self, year):
        if year>2001:
            self.__year=year
        else:
            print('Invalid year')

if __name__ == '__main__':

    book1 = book("It Ends With Us","Collen Hoover",1990,False)

    book1.display_details()

    book1.set_year(1900)