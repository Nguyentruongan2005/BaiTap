class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def input_sides(self):
        self.width = float(input("Nhập độ dài cạnh thứ nhất: "))
        self.height = float(input("Nhập độ dài cạnh thứ hai: "))

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def display_info(self):
        print(f"Hình chữ nhật có:")
        print(f"Độ dài cạnh thứ nhất: {self.width}")
        print(f"Độ dài cạnh thứ hai: {self.height}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")

# Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng hình chữ nhật
    rect = Rectangle()
    
    # Nhập dữ liệu cho hình chữ nhật
    rect.input_sides()
    
    # In thông tin của hình chữ nhật
    rect.display_info()