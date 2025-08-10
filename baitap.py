from abc import ABC, abstractmethod
class book(ABC):
    def __init__(self, book_id,title , author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
    def get_book_id(self):
        return self.book_id
    def get_title(self):
        return ().__gettitle()
    def get_author(self):
        return self.author
    def get_year(self):
        return self.year
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def get_year(self, year):
        return self.__year
    def se_title(self, title):
        self.__title = title   
    def set_author(self, author):
        self.__author = author
    def set_year(self, year):
        self.__year = year
    @abstractmethod
    def display_info(self):
        pass
class Physical_Book(book):  # Sử dụng đúng tên class Book
    def __init__(self, book_id, title, author, year, quality, location):
        super().__init__(book_id, title, author, year)
        self.quality = quality
        self.location = location
    def get_quality(self):
        return self.quality
    def get_location(self):
        return self.location
    def set_quality(self, quality):
        self.quality = quality
    def set_location(self, location):
        self.location = location
    def display_info(self):
        print(f"[sách giấy] mã: {self.book_id()}, tên: {self.get_title}")
        print f"tác giả: {self.get_author()}, năm: {self.get_year()}")
        print (f"số lượng: {self.get_quality}, vị trí: {self.get_location}")
class E_Book(book):  # Sử dụng đúng tên class Book
    def __init__(self, book_id, title, author, year, file_size, file_format):
        super().__init__(book_id, title, author, year)
        self.__file_size = file_size
        self.__file_format = file_format
    def get_file_size(self):
        return self.__file_size
    def get_file_format(self, fmt):
        self.__file_format = fmt
    def set_file_size(self, size):
        self.__file_size = size
    def display_info(self):
        print(f"[E-BOOK]" Mã: {self.get_book_id()}, Tên: {self.get_title()}")
        