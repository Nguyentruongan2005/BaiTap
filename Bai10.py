import math

# Lớp Point (Điểm)
class Point:
    def __init__(self, x=0, y=0):
        """Khởi tạo đối tượng điểm với tọa độ x và y."""
        self.x = x
        self.y = y

    def display(self):
        """In tọa độ điểm ra màn hình."""
        print(f"Điểm tọa độ: ({self.x}, {self.y})")

# Lớp Ellipse (Hình elip), kế thừa từ lớp Point
class Ellipse(Point):
    def __init__(self, x=0, y=0, a=0, b=0):
        """Khởi tạo đối tượng hình elip với tiêu điểm (x, y), trục lớn a và trục bé b."""
        super().__init__(x, y)
        self.a = a  # Trục lớn
        self.b = b  # Trục bé

    def input_attributes(self):
        """Nhập các thuộc tính cho hình elip."""
        self.x = float(input("Nhập tọa độ x của tâm elip: "))
        self.y = float(input("Nhập tọa độ y của tâm elip: "))
        self.a = float(input("Nhập độ dài trục lớn a: "))
        self.b = float(input("Nhập độ dài trục bé b: "))

    def area(self):
        """Tính diện tích của hình elip."""
        return math.pi * self.a * self.b

    def display(self):
        """In thông tin hình elip ra màn hình."""
        print(f"Tâm elip: ({self.x}, {self.y}), Trục lớn a: {self.a}, Trục bé b: {self.b}")
        print(f"Diện tích elip: {self.area():.2f}")

# Lớp Circle (Đường tròn), kế thừa từ lớp Ellipse
class Circle(Ellipse):
    def __init__(self, x=0, y=0, radius=0):
        """Khởi tạo đối tượng đường tròn với tâm (x, y) và bán kính radius."""
        super().__init__(x, y, radius, radius)  # Trục lớn và trục bé đều bằng bán kính
        self.radius = radius

    def input_attributes(self):
        """Nhập các thuộc tính cho đường tròn."""
        self.x = float(input("Nhập tọa độ x của tâm đường tròn: "))
        self.y = float(input("Nhập tọa độ y của tâm đường tròn: "))
        self.radius = float(input("Nhập bán kính của đường tròn: "))
        # Cập nhật trục lớn và trục bé bằng bán kính
        self.a = self.radius
        self.b = self.radius

    def area(self):
        """Tính diện tích của đường tròn."""
        return math.pi * self.radius ** 2

    def display(self):
        """In thông tin đường tròn ra màn hình."""
        print(f"Tâm đường tròn: ({self.x}, {self.y}), Bán kính: {self.radius}")
        print(f"Diện tích đường tròn: {self.area():.2f}")

# Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng elip và nhập thông tin
    print("Nhập thông tin cho hình elip:")
    ellipse = Ellipse()
    ellipse.input_attributes()
    ellipse.display()

    # Tạo đối tượng đường tròn và nhập thông tin
    print("\nNhập thông tin cho đường tròn:")
    circle = Circle()
    circle.input_attributes()