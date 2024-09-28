import math

# Lớp Triangle (Tam giác)
class Triangle:
    def __init__(self, a=0, b=0, c=0):
        """Khởi tạo đối tượng tam giác với độ dài ba cạnh a, b, c."""
        self.a = a  # Cạnh thứ nhất
        self.b = b  # Cạnh thứ hai
        self.c = c  # Cạnh thứ ba

    def input_sides(self):
        """Nhập độ dài các cạnh của tam giác."""
        self.a = float(input("Nhập độ dài cạnh a: "))
        self.b = float(input("Nhập độ dài cạnh b: "))
        self.c = float(input("Nhập độ dài cạnh c: "))

    def area(self):
        """Tính diện tích của tam giác theo công thức Heron."""
        s = (self.a + self.b + self.c) / 2  # Bán chu vi
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def display(self):
        """In thông tin tam giác ra màn hình."""
        print(f"Cạnh a: {self.a}, Cạnh b: {self.b}, Cạnh c: {self.c}")
        print(f"Diện tích tam giác: {self.area():.2f}")


# Lớp RightTriangle (Tam giác vuông), kế thừa từ lớp Triangle
class RightTriangle(Triangle):
    def __init__(self, base=0, height=0):
        """Khởi tạo đối tượng tam giác vuông với đáy và chiều cao."""
        super().__init__(base, height, math.sqrt(base ** 2 + height ** 2))  # Cạnh huyền tính toán

    def input_sides(self):
        """Nhập đáy và chiều cao cho tam giác vuông."""
        base = float(input("Nhập độ dài đáy: "))
        height = float(input("Nhập chiều cao: "))
        self.a = base
        self.b = height
        self.c = math.sqrt(base ** 2 + height ** 2)  # Tính cạnh huyền

    def area(self):
        """Tính diện tích của tam giác vuông."""
        return 0.5 * self.a * self.b


# Lớp IsoscelesTriangle (Tam giác cân), kế thừa từ lớp Triangle
class IsoscelesTriangle(Triangle):
    def __init__(self, equal_side=0, base=0):
        """Khởi tạo đối tượng tam giác cân với hai cạnh bằng nhau và một cạnh đáy."""
        super().__init__(equal_side, equal_side, base)

    def input_sides(self):
        """Nhập độ dài cạnh bằng nhau và cạnh đáy cho tam giác cân."""
        equal_side = float(input("Nhập độ dài cạnh bằng nhau: "))
        base = float(input("Nhập độ dài cạnh đáy: "))
        self.a = equal_side
        self.b = equal_side
        self.c = base

    def area(self):
        """Tính diện tích của tam giác cân."""
        height = math.sqrt(self.a ** 2 - (self.c / 2) ** 2)  # Tính chiều cao
        return 0.5 * self.c * height


# Lớp EquilateralTriangle (Tam giác đều), kế thừa từ lớp IsoscelesTriangle
class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, side=0):
        """Khởi tạo đối tượng tam giác đều với độ dài cạnh."""
        super().__init__(side, side)

    def input_sides(self):
        """Nhập độ dài cạnh cho tam giác đều."""
        self.a = float(input("Nhập độ dài cạnh: "))
        self.b = self.a
        self.c = self.a

    def area(self):
        """Tính diện tích của tam giác đều."""
        return (math.sqrt(3) / 4) * self.a ** 2  # Công thức diện tích tam giác đều

# Chương trình chính
if __name__ == "__main__":
    print("Nhập thông tin cho tam giác:")
    triangle = Triangle()
    triangle.input_sides()
    triangle.display()

    print("\nNhập thông tin cho tam giác vuông:")
    right_triangle = RightTriangle()
    right_triangle.input_sides()
    right_triangle.display()

    print("\nNhập thông tin cho tam giác cân:")
    isosceles_triangle = IsoscelesTriangle()
    isosceles_triangle.input_sides()
    isosceles_triangle.display()

    print("\nNhập thông tin cho tam giác đều:")
    equilateral_triangle = EquilateralTriangle()
    equilateral_triangle.input_sides()
    equilateral_triangle.display()