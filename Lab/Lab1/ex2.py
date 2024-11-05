dict1 = {"Fname": "Jane", "Lname": "Doe", "Age": 23}
print(dict1["Lname"])

dict2 = dict1.copy()
dict2.update({"Age": 24})
print(dict2)

dict1["Occupation"] = "Student"
print(dict1)

dict3 = dict1.copy()
dict3.pop("Fname")
print(dict3)

print(dict1.items())

print(dict1.values())

hobby = dict1.setdefault("Hobby", "Chess")
print(hobby)

dict1.clear()
print(dict1)