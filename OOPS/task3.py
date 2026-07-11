class Book:
    category = "Programming"

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Category: ",self.category)

book1 = Book("Python","Dr.Proloy Bose")
book2 = Book("Java","Dr.Pranjali Dutta")
book3 = Book("C++","Dr.Sougata Guha")

book1.display()
book2.display()
book3.display()



    
        