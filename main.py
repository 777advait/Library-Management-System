"""Library Management System In Python
Prerequisites => PyInquirer==1.0.3(run *pip install PyInquirer==1.0.3* on command line)"""

from PyInquirer import prompt # for CLI and making the code robust

Exit = False # to quit the program

class Library():
    def __init__(self, book_list):
        self.book_list = book_list # holds the books of library
        self.lend_dict = {} # holds the data of books lend
        print(
            """      Library Management System
        Made By Advait Jadhav
        """
            )

    def addBook(self, book_name): # adds book to self.book_list
        self.book_list.append(book_name)
        print(f"Book {book_name} added successfully\nAvailable books:{self.book_list}")

    def lendBook(self, book_name, reader): # lends book to reader
        self.lend_dict.update({reader:book_name})
        print(f"Book lend data update\nLend Data : {self.lend_dict}")

    def displayBook(self): # displays available books
        print("Books available at our store\n")
        for books in self.book_list:
            print("[ ]" + books)
    
    def returnBook(self, reader, book):
        self.lend_dict.pop(reader, book)
        print(f"Book returned successfully!")


def main():
    global Exit

    print("\n")
    questions = [
        {
            "type":"list",
            "name":"choice",
            "message":"What would you like to do?",
            "choices":[
                "Display Books",
                "Add Book",
                "Lend Book",
                "Return Book",
                "Exit"
            ]
        }
    ]
    answer = prompt(questions)

    if answer["choice"] == "Display Books":
        my_lib.displayBook()

    elif answer["choice"] == "Add Book":
        book_name = input("Enter the name of book to be added: ")
        my_lib.addBook(book_name)

    elif answer["choice"] == "Lend Book":
        reader = input("Enter your name: ")
        
        print("\n")

        _book = [
            {
                "type":"list",
                "name":"book",
                "message":"Which book do you want?",
                "choices":my_lib.book_list
            }
        ]

        answer = prompt(_book)

        my_lib.lendBook(answer["book"], reader)

    elif answer["choice"] == "Return Book":
        print("\n")

        reader_data = [
            {
                "type":"list",
                "name":"reader_name",
                "message":"Select your name",
                "choices":my_lib.lend_dict
            }
        ]

        answer = prompt(reader_data)

        reader = answer["reader_name"]
        book = my_lib.lend_dict[answer["reader_name"]]
        
        my_lib.returnBook(reader, book)

    else:
        Exit = True

my_lib = Library(
    [
        "A Light in the Attic",
        "Tipping the Velvet",
        "Soumission",
        "Sharp Objects",
        "Sapiens: A Brief History of Humankind",
        "The Requiem Red",
        "The Dirty Little Secrets of Getting Your Dream Job",
        "The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull",
        "The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics",
        "The Black Maria",
        "Starving Hearts (Triangular Trade Trilogy, #1)",
        "Shakespeare's Sonnets",
        "Set Me Free",
        "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)",
        "Rip it Up and Start Again",
        "Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991",
        "Olio",
        "Mesaerion: The Best Science Fiction Stories 1800-1849",
        "Libertarianism for Beginners",
        "It's Only the Himalayas"
    ]
)

while Exit is not True:
    main()