import json

person = {
    "name": "Nguyen A",
    "age": 20,
    "city": "Hanoi",
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "is_employed": True
}


person_json = json.dumps(person, indent=4, ensure_ascii=False)

print("Chuỗi JSON được tạo ra từ đối tượng Python:")
print(person_json)


print("\nTất cả các giá trị trong đối tượng Python:")
for key, value in person.items():
    print(f"{key}: {value}")