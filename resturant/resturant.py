# JSON data is represented as key-value pairs. In Python, JSON data is most commonly represented using dictionaries (for objects) and lists (for arrays).
"""{
    "name": "John",
    "age": 30,
    "is_student": false,
    "courses": ["Math", "Science"],
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
You can convert Python objects (like dictionaries) into JSON strings using the json.dumps() method.
json_data = json.dumps(data)
print(json_data)

You can convert JSON strings back into Python objects using the json.loads() method.
The json.load(file) function reads the JSON data from the file and converts it back into a Python dictionary.
data = json.loads(json_data)
print(data)


You can also read from and write to JSON files using json.load() and json.dump() methods.
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
    
    In the context of the json.dump() function in Python, the indent parameter is used to specify the indentation level for the output JSON file. This makes the JSON file more readable by adding whitespace (indentation) to the nested structures.
"""
import json
with open("menu.json","r")as f:
  data=json.load(f)



print("-"*30)
print("""
  welcome to Laltin Resturant🌸
      1. To show menu
      2. To Order items
      3. To Update Menu
      4. To Add review
      5. To exit 
      """
      )
print("-"*30)


