from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, book_id, title, author, year):
        # ENCAPSULATION - thuộc tính private
        self._book_id = book_id
        self._title = title
        self._author = author
        self._year = year

    def get_book_id(self):
        return self._book_id

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_year(self):
        return self._year

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_year(self, year):
        self._year = year

    @abstractmethod
    def display_info(self):
        pass

class PhysicalBook(Book):
    def __init__(self, book_id, title, author, year, quantity, location):
        super().__init__(book_id, title, author, year)
        self._quantity = quantity
        self._location = location

    def get_quantity(self):
        return self._quantity

    def get_location(self):
        return self._location

    def set_quantity(self, quantity):
        self._quantity = quantity

    def set_location(self, location):
        self._location = location

    def display_info(self):
        print(f"[Sách Giấy] Mã: {self.get_book_id()}, Tên: {self.get_title()}, "
              f"Tác giả: {self.get_author()}, Năm: {self.get_year()}, "
              f"Số lượng: {self._quantity}, Vị trí: {self._location}")

class EBook(Book):
    def __init__(self, book_id, title, author, year, file_size, file_format):
        super().__init__(book_id, title, author, year)
        self._file_size = file_size
        self._file_format = file_format

    def get_file_size(self):
        return self._file_size

    def get_file_format(self):
        return self._file_format

    def set_file_size(self, file_size):
        self._file_size = file_size

    def set_file_format(self, file_format):
        self._file_format = file_format

    def display_info(self):
        print(f"[EBook] Mã: {self.get_book_id()}, Tên: {self.get_title()}, "
              f"Tác giả: {self.get_author()}, Năm: {self.get_year()}, "
              f"Dung lượng: {self._file_size}MB, Định dạng: {self._file_format}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Thêm sách thành công!")

    def display_all_books(self):
        if not self.books:
            print("Thư viện trống")
        else:
            for book in self.books:
                book.display_info()

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.get_book_id() == book_id:
                return book
        return None

    def remove_book(self, book_id):
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            print("Xóa sách thành công!")
        else:
            print("Không tìm thấy sách!")

def main():
    library = Library()
    while True:
        print("\n=== QUẢN LÝ THƯ VIỆN ===")
        print("1. Thêm sách mới")
        print("2. Hiển thị tất cả sách")
        print("3. Tìm kiếm sách theo mã")
        print("4. Xóa sách")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == "1":
            book_type = input("Chọn loại sách (1: Sách giấy, 2: E-Book): ")
            book_id = input("Nhập mã sách: ")
            title = input("Nhập tên sách: ")
            author = input("Nhập tác giả: ")
            year = input("Nhập năm xuất bản: ")
            if book_type == "1":
                quantity = int(input("Nhập số lượng: "))
                location = input("Nhập vị trí: ")
                book = PhysicalBook(book_id, title, author, year, quantity, location)
            else:
                file_size = float(input("Nhập dung lượng (MB): "))
                file_format = input("Nhập định dạng: ")
                book = EBook(book_id, title, author, year, file_size, file_format)
            library.add_book(book)
        elif choice == "2":
            library.display_all_books()
        elif choice == "3":
            book_id = input("Nhập mã sách cần tìm: ")
            book = library.find_book_by_id(book_id)
            if book:
                book.display_info()
            else:
                print("Không tìm thấy sách!")
        elif choice == "4":
            book_id = input("Nhập mã sách cần xóa: ")
            library.remove_book(book_id)
        elif choice == "0":
            print("Thoát chương trình.")
            break
        else:
            print("Chức năng không hợp lệ!")

if __name__ == "__main__":
    main()