class Book:
    def __init__(self, title, author, published):
        self.title = title
        self.author = author
        self.published = published
        self.rating = None
    
    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Published: {self.published}")
    
    def rate_book(self, rating):
        self.rating = rating
        print(f"Rating for {self.title}: {self.rating}")

class Novel(Book):
    def __init__(self, title, author, published, genre):
        super().__init__(title, author, published)
        self.genre = genre



minecraft_book = Novel("Minecraft: The Island", "Max Brooks", 2017, "Adventure")
minecraft_book.display_details()



# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which
# uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.