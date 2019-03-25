class User(object):
    # constructor for user class.  name and email as params
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {} # empty dicitionary to hold books
    
    # returns email
    def get_email(self):
        return self.email
    
    # updates email and prints confirmation
    def change_email(self, address):
        self.email = address
        print("Email address has been updated to {email}".format(email=self.email))
    
    # displays string representation of a user object. 
    def __repr__(self):
        return "User {name}, email {email} books read:  {books}".format(name=self.name, email=self.email,books=self.get_books_read())

    # override for equality.  Returns true if email equals another email
    def __eq__(self, other):
        if (self.email == other.email):
            return True
        else:
            return False
    
    # updates book dictionary with a read book and rating 
    def read_book(self, book, rating=None):
        self.books[book] = rating

    # returns average rating.  rating calculated by iterting through book dictionary for ratings values. Values are summed and divided by total books. Average is returned
    def get_average_rating(self):
        ratings_sum = 0
        total_books_read = self.get_books_read()
        for book in self.books.keys():
            if self.books[book] != None:
                ratings_sum += self.books[book]
        return ratings_sum / total_books_read

    # returns total number of books read by the length of the books dicitionary
    def get_books_read(self):
        return len(self.books)

class Book(object):
    # constructor for book class, inherits from object.  takes in title, and isbn as params
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    # returns title
    def get_title(self):
        return self.title
    
    # returns isbn
    def get_isbn(self):
        return self.isbn

    # sets isbn and prints confirmation
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Book has been updated to {isbn}".format(isbn=self.isbn))

    # adds a rating. validates that rating is in a correct range.
    def add_rating(self, rating):
        if ((rating >= 0) and (rating <= 4)):
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    # equality check if two books have the same title and isbn.  returns true if title and isbn equal on both books.
    def __eq__(self, other):
        if ((self.title == other.title) and (self.isbn == other.isbn)):
            return True
        else:
            return False

    # returns average rating
    def get_average_rating(self):
        sum = 0
        for rating in self.ratings:
            sum += rating
        return sum/len(self.ratings)
    
    # prints all ratings
    def get_ratings(self):
        for rating in self.ratings:
            print(rating)
    
    # requried has method
    def __hash__(self):
        return hash((self.title, self.isbn))

# Fiction class.   Inherits from Book.
class Fiction(Book):
    # consturctor for Fiction class.   
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    # returns author of book
    def get_author(self):
        return self.author

    # returns string representation of a Fiction object
    def __repr__(self):
        return "{title} by {arthor}".format(title=self.title, arthor=self.author)

# Non Fiction Class.  Inherits from Book
class Non_Fiction(Book):
    # constructor for Non_Fiction
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    # returns subject of book
    def get_subject(self):
        return self.subject

    # returns level of book 
    def get_level(self):
        return self.level

    # returns string representation of a book object
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)

# Main class.
class TomeRater():
    # TomeRater constructor.  Takes no parameters
    def __init__(self):
        self.users = {} #Users dictionary
        self.books = {} # Books dictionary

    # returns Book object
    def create_book(self, title, isbn):
        return Book(title,isbn)

    # returns Fiction object
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    # returns Non_Fiction object
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    # adds a book to a user.  Validates email is in users dictionary. If a rating, adds rating.  if no rating, adds default rating of None 
    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("User {email} is not in the system".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] +=1
            else:
                self.books[book] = 1
 
    # adds user.  validates email has not already been used. Adds books to user.
    def add_user(self, name, email,user_books=None):
        
        if (email.find("@") > 0) and email.find(".com") > 0 or email.find(".edu") > 0 or email.find(".org") > 0:
            if email not in self.users:
                self.users[email] = User(name, email)
                if user_books is not None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
            else:
                print("User is already in the system.")
            
    # prints catalog of books in books dictionary. 
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    # prints list of users.
    def print_users(self):
        for user in self.users.values():
            print(user)

    # returns most read books
    def most_read_books(self):
        return max(self.books, keys=self.books.get)

    # returns highest rated books in string format. 
    def highest_rated_book(self):
        top_rated = max(rating.get_average_rating() for rating in self.books.keys())
        return str([book for book in self.books.keys() if book.get_average_rating() == top_rated])

    # calculates most positive user by getting each users's higest rating.  Each high rating is compared to the next rating.  Highest rating is tracked and then returned.
    def most_positive_user(self):
        most_positive = None
        high_rating = 0
        for user in self.users.values():
            average_user_rating = user.get_average_rating()
            if average_user_rating > high_rating:
                most_positive = user
                high_rating = average_user_rating
        return most_positive
