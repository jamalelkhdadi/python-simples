list = [
    {"name": "x", "number": "0652"},
    {"name": "y", "number": "0644"},
    {"name": "z", "number": "0658"},
]

name = input("Name: ")

for person in list:
   if person["name"] == name:
       number = person["number"]
       print(f"found: {number}")
       break
else:
    print("Not found")
