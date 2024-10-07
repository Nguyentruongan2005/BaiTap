import json
from collections import OrderedDict

person = OrderedDict([
    ("name", " A"),
    ("age", 25),
    ("city", "Ha Noi"),
    ("skills", ["Python", "B", "c"]),
    ("is_employed", False)
])

person_json = json.dumps(person, indent=4, ensure_ascii=False)

print("Chuỗi JSON được tạo ra từ đối tượng từ điển Python:")
print(person_json)