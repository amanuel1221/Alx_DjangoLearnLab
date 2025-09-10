import django
import os

# Setup Django environment (adjust path if needed)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


# 2. List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3. Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)


if __name__ == "__main__":
    print("Books by Author John Doe:")
    for book in books_by_author("John Doe"):
        print(book.title)

    print("\nBooks in Central Library:")
    for book in books_in_library("Central Library"):
        print(book.title)

    print("\nLibrarian of Central Library:")
    librarian = librarian_of_library("Central Library")
    if librarian:
        print(librarian.name)


