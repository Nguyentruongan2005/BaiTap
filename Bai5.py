class Stack:
    def __init__(self, capacity=10):
        """Khởi tạo ngăn xếp với dung lượng tối đa mặc định là 10."""
        self.capacity = capacity
        self.stack = []  
        self.top = -1  

    def __del__(self):
        """Hàm hủy ngăn xếp."""
        del self.stack

    def push(self, value):
        """Đưa một phần tử vào ngăn xếp."""
        if not self.isFull():
            self.stack.append(value)
            self.top += 1
            print(f"Đã đưa phần tử {value} vào ngăn xếp.")
        else:
            print("Ngăn xếp đã đầy, không thể đưa thêm phần tử.")

    def pop(self):
        """Lấy một phần tử ra từ đỉnh ngăn xếp."""
        if not self.isEmpty():
            value = self.stack.pop()
            self.top -= 1
            print(f"Đã lấy phần tử {value} ra khỏi ngăn xếp.")
            return value
        else:
            print("Ngăn xếp trống, không có phần tử nào để lấy ra.")
            return None

    def isEmpty(self):
        """Kiểm tra ngăn xếp có trống hay không."""
        return self.top == -1

    def isFull(self):
        """Kiểm tra ngăn xếp có đầy không."""
        return self.top + 1 == self.capacity

    def count(self):
        """Trả về số phần tử hiện có trong ngăn xếp."""
        return self.top + 1

    def display(self):
        """In ra các phần tử hiện có trong ngăn xếp."""
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Các phần tử trong ngăn xếp:", self.stack)

# Chương trình chính
if __name__ == "__main__":
   
    stack = Stack(5)
    
   
    stack.push(1.5)
    stack.push(2.5)
    stack.push(3.5)
    stack.push(4.5)
    stack.push(5.5)
    stack.push(6.5) 
    
   
    stack.display()
    
    print(f"Số phần tử hiện có trong ngăn xếp: {stack.count()}")
    
 
    stack.pop()
    stack.pop()
    
   
    print("Ngăn xếp trống:", stack.isEmpty())
    
   
    stack.display()
    

    print(f"Số phần tử hiện có trong ngăn xếp: {stack.count()}")
    
    del stack