class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.grade = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grade.append(grade)
        else:
            print("Điểm không hợp lệ! Điểm phải trong khoảng từ 0 đến 10.")
    def calculate_average(self):
        if self.grade:
            return sum(self.grade) / len(self.grade)
        else:
            return 0
        return sum(self.grade) /len(self,grade) if self.grade else 0
class GradeManager:
    def __innit__(self):
        self.students = []
    def add_student(self, name):
        student = student(name)
        self.students.append(student)
        return student
    def record_grade(self, name, grade):
        student = self.find_student(name)
        if student:
            student.grade.append(grade)
        else:
            print("Học viên không tồn tại!")
    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None
    
    def caulate_average_all(self,):
        if not self.students:
            return 0
        total_average = sum(student.calculate_average() for student in self.students)
        return total_average / len(self.students)
    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for student in self.students:
                file.write(f"học viên: {student.name}\n")
                file.write(f"Điểm: {', '.join(map(str, student.grade))}\n")
                file.write(f"Điểm trung bình: {student.calculate_average()}\n\n")
                file.write("-" * 20 + "\n")
def main():
    manager = GradeManager()
    while True:
        print("\nMenu:")
        print("1. Thêm học viên")
        print("2. Ghi điểm cho học viên")
        print("3. Tính điểm trung bình của tất cả học viên")
        print("4. Lưu thông tin học viên vào file")
        print("5. Thoát")
        choice = input("Chọn chức năng (1-5): ")

        if choice == "1":
            name = input("nhập tên học viên: ")
            manager.add_student(name)
        
        

        

        
