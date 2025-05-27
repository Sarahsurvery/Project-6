# assign 11
# Class Method
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 4

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)
# Explanation:
#	Tracks shared data across all instances using class methods.
