class Book:
    def __init__(self, title, author, published):
        self.title = title
        self.author = author
        self.published = published
    
    def display_details(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.published}"
    
    def rate_book(self, rating):
        return f"Rating for {self.title}: {self.rating}"
    
    def review_book(self, review):
        return f"Review for {self.title}: {review}"

class Novel(Book):
    def __init__(self, title, author, published, genre, num_chapters):
        super().__init__(title, author, published)
        self.genre = genre
        self.num_chapters = num_chapters
    
    def calcReadTime(self, chaptersPerHour):
        return self.num_chapters / chaptersPerHour

class Magazine(Book):
    def __init__(self, title, author, published, issue_number):
        super().__init__(title, author, published)
        self.issue_number = issue_number
        self.num_articles = 0
    
    def get_article_by_title(self, title):
        return f"Article: {title} in {self.title}" # this doesnt really do anything but oh well it was in the instructions

software_textbook = Novel("Software Textbook", "John Software", 1986, "Horror", 12)
print(software_textbook.calcReadTime(2))
print(software_textbook.display_details())
lucas_book = Novel("Lucastitle", "Lucasauthor", 2023, "Adventure", 999)
print(lucas_book.display_details())
print(lucas_book.calcReadTime(2))

software_magazine = Magazine("Software Magazine", "John Software", 1986, 1)
print(software_magazine.display_details())
lucas_magazine = Magazine("Lucas Magazine", "Lucasauthor", 2023, 2)
print(lucas_magazine.display_details())


# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which
# uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.