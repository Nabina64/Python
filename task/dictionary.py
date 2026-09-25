# # Dictionary - Key Value Pair

# # 1. Dictionary बनाउनु (Creating a Dictionary)
# student = {
#     "name": "Raj",
#     "age": 20,
#     "city": "Kathmandu",
#     "grade": "A"
# }

# print("=" * 50)
# print("1. पूरो Dictionary:")
# print(student)
# print()

# # 2. Specific Key को Value पाउनु
# print("=" * 50)
# print("2. Specific Key को Value पाउनु:")
# print(f"नाम: {student['name']}")
# print(f"शहर: {student['city']}")
# print()

# # 3. सबै Keys निकाल्नु
# print("=" * 50)
# print("3. सबै Keys निकाल्नु (.keys()):")
# keys = student.keys()
# print(f"Keys: {keys}")
# print(f"Keys को List: {list(keys)}")
# print()

# # 4. सबै Values निकाल्नु
# print("=" * 50)
# print("4. सबै Values निकाल्नु (.values()):")
# values = student.values()
# print(f"Values: {values}")
# print(f"Values को List: {list(values)}")
# print()

# # 5. Key + Value को जोडी निकाल्नु
# print("=" * 50)
# print("5. Key + Value को जोडी निकाल्नु (.items()):")
# items = student.items()
# print(f"Items: {items}")
# print()

# # 6. Key र Value लाई loop मा निकाल्नु
# print("=" * 50)
# print("6. Loop मा Key र Value निकाल्नु:")
# for key in student.keys():
#     print(f"Key: {key}, Value: {student[key]}")
# print()

# # 7. .items() को साथ loop
# print("=" * 50)
# print("7. .items() को साथ loop:")
# for key, value in student.items():
#     print(f"Key: {key}, Value: {value}")
# print()

# # 8. Key र Value लाई combine गर्नु (concatenate)
# print("=" * 50)
# print("8. Key र Value लाई combine गर्नु:")
# for key, value in student.items():
#     print(f"{key} = {value}")
#     # String को रूपमा combine गर्नु
#     combined = key + ": " + str(value)
#     print(f"  Combined: {combined}")
# print()

# # 9. अर्को Dictionary उदाहरण
# print("=" * 50)
# print("9. अर्को Dictionary उदाहरण:")
# marks = {
#     "Math": 85,
#     "English": 90,
#     "Science": 88,
#     "Social": 92
# }

# print("विषय र अंकहरु:")
# for subject, mark in marks.items():
#     print(f"  {subject}: {mark} अंक")
# print()

# # 10. Key र Value को सबै combinations
# print("=" * 50)
# print("10. सबै Keys र Values को सबै combinations:")
# print("Keys:", list(marks.keys()))
# print("Values:", list(marks.values()))
# print("Items (Key-Value Pairs):", list(marks.items()))



# student = {
#     "name": "Raj",
#     "age": 20,
#     "city": "Kathmandu"
# }

# keys = list(student.keys())
# values = list(student.values())
# items = list(student.items())

# print(keys[0])      # name
# print(values[0])    # Raj
# print(items[0])     # ('name', 'Raj')
# print(keys[1])      # age
# print(values[1])    # 20



# ----------------------
# List example
# ----------------------
# print("=" * 50)
# print("List Example")
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# print("List:", fruits)
# print("First item:", fruits[0])
# print("Second item:", fruits[1])
# print("Length:", len(fruits))

# fruits.append("Grapes")
# print("After append:", fruits)

# fruits.remove("Banana")
# print("After remove:", fruits)

# ----------------------
# Tuple example
# ----------------------
# print("=" * 50)
# print("Tuple Example")
# coordinates = (10, 20)
# print("Tuple:", coordinates)
# print("First value:", coordinates[0])
# print("Second value:", coordinates[1])
# print("Tuple length:", len(coordinates))

# # tuple with different data types
# person = ("Ram", 21, "Kathmandu")
# print("Person:", person)
# print("Name:", person[0])
# print("Age:", person[1])
# print("City:", person[2])

# ----------------------
# Simple comparison
# ----------------------
# print("=" * 50)
# print("List vs Tuple")
# print("List is mutable: can change values")
# print("Tuple is immutable: cannot change values after creation")

# ----------------------
# Set example
# # ----------------------
# print("=" * 50)
# print("Set Example")
# colors = {"Red", "Green", "Blue", "Red"}
# print("Set:", colors)
# print(len(colors))

# colors.add("Yellow")
# print("After add:", colors)

# colors.remove("Green")
# print("After remove:", colors)

# # set does not support indexing like list/tuple
# print("Set cannot access by index like colors[0]")

# ----------------------
# Set vs List vs Tuple summary
# ----------------------
# print("=" * 50)
# print("Collection Summary")
# print("List -> ordered, mutable, allows duplicates")
# print("Tuple -> ordered, immutable, allows duplicates")
# print("Set -> unordered, mutable, no duplicates")


my_dict = {
    "name" : "nabina",
    "age" : 18,
    "home" : "pyuthan"
    }

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict['name'])