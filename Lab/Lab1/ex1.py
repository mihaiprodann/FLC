list1 = ["Math", "English", "History", "Chemistry", "Biology"]

print(list1[1])
print(len(list1))
print(list1[1:3])
print(list1[-4])

list2 = list1.copy()
list2.remove("Chemistry")
print(list2)

list3 = list1.copy()
list3.insert(2, "Geography")
print(list3)

list4 = list1.copy()
list4[1] = "Romanian"
print(list4)
