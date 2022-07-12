class Library:
    def __init__(self,listofbooks):
        self.books = listofbooks
    def displayAvailableBooks(self):
        for book in self.books:
            print(" *"+book)

    def borrowBook(self, booktoborrow):
        if booktoborrow in self.books:
            print(f"{booktoborrow} is issued to you.")
            self.books.remove(booktoborrow)
        else:
            print(f"{booktoborrow} is not available")
    def returnBook(self, booktoreturn):
        print("Thank you for returning the book!")
        self.books.append(booktoreturn)

class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django", "Clrs", "Python Notes"])
    student = Student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")