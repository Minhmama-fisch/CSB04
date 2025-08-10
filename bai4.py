class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Tuổi không hợp lệ!")

class Student(Person):
    def __init__(self, name, age, student_id, classroom):
        super().__init__(name, age)
        self.__student_id = student_id  # Thuộc tính private
        self.classroom = classroom

    def get_student_id(self):
        return self.__student_id

    def get_classroom(self):
        return self.classroom
    class Student(Person):
     def __init__(self, name, age, student_id, classroom):
        super().__init__(name, age)
        self.__student_id = student_id  # Thuộc tính private
        self.classroom = classroom

    def get_student_id(self):
        return self.__student_id

    def get_classroom(self):
        return self.classroom

    def set_classroom(self, classroom):
        self.classroom = classroom

    def display_info(self):
        print(f"ID: {self.__student_id}, Họ tên: {self._name}, Tuổi: {self._age}, Lớp: {self.classroom}")

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Thêm học sinh thành công!")

    def update_student(self, student_id, name=None, age=None, classroom=None):
        for student in self.students:
            if student.get_student_id() == student_id:
                if name:
                    student.set_name(name)
                if age:
                    student.set_age(age)
                if classroom:
                    student.set_classroom(classroom)
                print("Cập nhật thông tin thành công!")
                return
        print("Không tìm thấy học sinh!")

    def delete_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                print("Xóa học sinh thành công!")
                return
        print("Không tìm thấy học sinh!")
        def delete_student(self, student_id):
         for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                print("Đã xóa học sinh!")
                return
        print("Không tìm thấy học sinh!")

    def display_all(self):
        if not self.students:
            print("Danh sách học sinh trống!")
        else:
            print("\nDanh sách học sinh:")
            for student in self.students:
                student.display_info()

# Ví dụ sử dụng:
manager = StudentManager()
s1 = Student("Nguyễn Văn A", 15, "HS001", "10A1")
s2 = Student("Trần Thị B", 14, "HS002", "9B")
manager.add_student(s1)
manager.add_student(s2)
manager.display_all()
manager.update_student("HS001", age=16, classroom="11A1")
manager.display_all()
manager.delete_student("HS002")
manager.display_all()
