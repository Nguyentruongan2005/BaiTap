
class Date:
    def __init__(self, day=1, month=1, year=2000):
        """Khởi tạo đối tượng ngày với các giá trị mặc định: ngày 1, tháng 1, năm 2000."""
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin ngày ra màn hình theo định dạng dd/mm/yyyy."""
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def next_day(self):
        """Tính ngày tiếp theo."""
        self.day += 1
        if self.day > self.days_in_month():
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        """Kiểm tra năm nhuận."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def days_in_month(self):
        """Trả về số ngày trong tháng tương ứng."""
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        return 0



class Employee:
    def __init__(self, name, birth_date, join_date):
        """Khởi tạo đối tượng nhân viên với họ tên, ngày sinh và ngày vào công ty."""
        self.name = name
        self.birth_date = birth_date  
        self.join_date = join_date    

    def display(self):
        """In thông tin nhân viên ra màn hình."""
        print(f"Họ tên: {self.name}")
        print(f"Ngày sinh: {self.birth_date.display()}")
        print(f"Ngày vào công ty: {self.join_date.display()}")


# Chương trình chính
if __name__ == "__main__":

    employees = []

  
    employees.append(Employee("Nguyễn  A", Date(15, 5, 1990), Date(1, 6, 2020)))
    employees.append(Employee("Trần  B", Date(22, 7, 1992), Date(15, 8, 2019)))
    employees.append(Employee("Lê  C", Date(30, 10, 1985), Date(5, 1, 2021)))

    print("Danh sách nhân viên trong công ty:")
    for employee in employees:
        employee.display()
        print("-" * 30)