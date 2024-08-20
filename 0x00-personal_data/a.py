import functools


def storage(fn):
    funct_name = f"_{fn.__name__}"

    @functools.wraps(fn)
    def wrapper(self):
        if not hasattr(self, funct_name):
            setattr(self, funct_name, fn(self))
        return getattr(self, funct_name)
    return wrapper


class Library:
    def __init__(self) -> None:
        self.storage = []

    def add_data(self, title, author):
        book = {
            'title': title,
            'author': author
        }
        self.storage.append(book)

    @storage
    def get_books(self):
        print("function called")
        return self.storage


my_lib = Library()
my_lib.add_data('Mastery', 'Robert grene')
my_lib.add_data('7 habits of highly effective people', 'Robert grene')
my_lib.add_data('Healing your innerself', 'Benjamin Zule')
my_lib.add_data('How to win friends and influence people', 'Dale Carnegie')
print(my_lib.get_books())
print(my_lib.get_books())
print(*my_lib.get_books(), sep='\n')

