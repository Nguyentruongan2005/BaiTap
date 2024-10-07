import json

json_data = '{"name": "A", "age": 20, "city": "Ha Noi"}'

python_obj = json.loads(json_data)

print(python_obj)
print(type(python_obj))  