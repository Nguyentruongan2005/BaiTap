class Date:
    def __init__(self, day=1, month=1, year=2000):
        """Khởi tạo đối tượng ngày với các giá trị mặc định: ngày 1, tháng 1, năm 2000."""
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin ngày ra màn hình theo định dạng dd/mm/yyyy."""
        print(f"Ngày {self.day:02d}/{self.month:02d}/{self.year}")

    def is_leap_year(self):
        """Kiểm tra năm nhuận."""
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            return True
        return False

    def days_in_month(self):
        """Trả về số ngày trong tháng tương ứng."""
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        elif self.month == 2:
            return 29 if self.is_leap_year() else 28
        return 0

    def next_day(self):
        """Tính ngày tiếp theo."""
        self.day += 1
        if self.day > self.days_in_month():
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

# Chương trình chính
if __name__ == "__main__":
   
    date = Date()
    date.display()  

   
    date = Date(28, 2, 2024)
    date.display()  
    date.next_day()  
    date.display()  

 
    date = Date(31, 12, 2023)
    date.display()  
    date.next_day() 
    date.display()  