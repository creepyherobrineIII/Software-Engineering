# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behaviour of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    #String representation of the object
    def __str__(self): #Allows us to define what is returned when directly printing the instance
        return f"{self.title} by {self.author}"
    
    #Used for comparison operations (equals)
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    #Used for comparison operations (less than)
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    #Used for comparison operations (greater than)
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    #Custom magic method for math operations
    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"
    
    #Search operations
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    #Getting items
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch And The Wardrobe", "C.S. Lewis", 172)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 560)

print(book1) #__str__
print(book1 == book4) #__eq__
print(book1 < book4) #__lt__
print(book1 > book4) #__gt__
print(book2 + book3) #__add__
print("Lion" in book3) #__contains__
print(book1['title']) #__getitem__