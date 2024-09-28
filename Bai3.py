from math import gcd

class PS:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify() 

    def is_valid(self):
        """Kiểm tra tính hợp lệ của phân số."""
        return self.denominator != 0

    def input_fraction(self):
        """Nhập phân số từ người dùng."""
        while True:
            try:
                self.numerator = int(input("Nhập tử số: "))
                self.denominator = int(input("Nhập mẫu số: "))
                if self.is_valid():
                    self.simplify()
                    break
                else:
                    print("Mẫu số không thể bằng 0. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ.")

    def simplify(self):
        """Rút gọn phân số."""
        if self.denominator < 0:
            
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        divisor = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator //= divisor
        self.denominator //= divisor

    def display_fraction(self):
        """In phân số ra màn hình."""
        if self.denominator == 1:
            print(f"Phân số: {self.numerator}")
        elif self.numerator == 0:
            print("Phân số: 0")
        else:
            print(f"Phân số: {self.numerator}/{self.denominator}")

# Chương trình chính
if __name__ == "__main__":
    ps = PS()
    ps.input_fraction()
    ps.display_fraction()