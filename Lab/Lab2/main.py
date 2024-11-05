#ex 1

for i in range(40, 70):
    if i % 3 == 0:
        print(i)
print("----------")

#ex 2
name = input("Enter name: ")
print(name.split()[1], name.split()[0])


#ex 3
nr = int(input("enter nr: "))
s = (nr * (nr+1)) / 2
print(s)

#ex 4
for i in range(1, 10):
    if i >= 5:
        print("Success")

#ex 5
lab = "Welcome to the lab!"
print(lab.count("m"))
print(lab.count("l"))
print(lab.count("c"))
print(lab.count("a"))
print(lab.count("e"))

#ex 6
fact = int(input("Enter a number: "))
f = lambda x: 1 if x == 0 else x * f(x-1)
print(f(fact))

#ex 7
n = int(input("Enter a number: "))
if n > 100:
    print(n / 2 + 20)
else:
    print(n * 3 - 200)

#ex 8
nrs = input("Enter the numbers: ")
nrs = nrs.split(",")
print(nrs)
print(tuple(nrs))

#ex 9
nr = int(input("Enter the number: "))
for i in range(1, nr):
    print (i*i)