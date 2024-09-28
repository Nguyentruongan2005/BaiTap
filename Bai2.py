class TS:
    def __init__(self, name="", math=0, physics=0, chemistry=0):
        self.name = name
        self.math = math
        self.physics = physics
        self.chemistry = chemistry

    def input_info(self):
        self.name = input("Nhập họ tên thí sinh: ")
        self.math = float(input("Nhập điểm Toán: "))
        self.physics = float(input("Nhập điểm Lý: "))
        self.chemistry = float(input("Nhập điểm Hoá: "))

    def total_score(self):
        return self.math + self.physics + self.chemistry

    def display_info(self):
        print(f"Họ tên: {self.name}")
        print(f"Điểm Toán: {self.math}")
        print(f"Điểm Lý: {self.physics}")
        print(f"Điểm Hoá: {self.chemistry}")
        print(f"Tổng điểm: {self.total_score()}")

# Chương trình chính
if __name__ == "__main__":

    candidates = []
    num_candidates = int(input("Nhập số lượng thí sinh: "))

    for _ in range(num_candidates):
        candidate = TS()
        candidate.input_info()
        candidates.append(candidate)


    pass_score = 20
    passed_candidates = [candidate for candidate in candidates if candidate.total_score() >= pass_score]


    passed_candidates.sort(key=lambda x: x.total_score(), reverse=True)

    print("\nDanh sách thí sinh trúng tuyển:")
    for candidate in passed_candidates:
        candidate.display_info()
        print("-" * 30)  