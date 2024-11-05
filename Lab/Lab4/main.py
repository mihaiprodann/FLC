import re

# Ex 1
shapes = ["rectangle", "square", "sphere", "triangle", "code", "cube", "cylinder"]
pattern = re.compile(r'[cs].+e')
for shape in shapes:
    if pattern.match(shape):
        print(shape)

# Ex 2
words = "car, cat, dog, pool, bath, cone, cube, ring, int"
pattern = re.compile(r'\b\w{4}\b')
for word in words.split(", "):
    if pattern.match(word):
        print(word)

# Ex 3
list = ["square", "triangle", "cube", "sphere", "circle", "pentagon", "hexagon", "rectangle", "parallelogram",
        "trapezoid"]
pattern = re.compile(r'\b\w+re\b')
for word in list:
    if pattern.match(word):
        print(word)

# Ex 4
geo = "A square has 4 sides, a triangle has 3, a pentagon has 5, a hexagon has 6. While a square has 4 equal sides, a triangle can have 0, 2 or 3 equal sides."
pattern = re.compile(r'\b\w+re\b')
for word in list:
    if pattern.match(word):
        print(word)
print(re.findall(r'\d', geo))
print(re.findall(r'\D', geo))

# Ex 5
link = "https://www.newyorker.com/magazine/2021/11/01/the-book-of-form-and-emptiness-thewar-for-gloria-read-until-you-understand-and-the-end-of-bias"
pattern = re.compile(r'(\d{4})/(\d{2})/(\d{2})')
print(re.findall(pattern, link))

# Ex 6
date = "2021-11-02"
year_pattern = re.compile(r'\d{4}-')
month_pattern = re.compile(r'\b-\d{2}-')
day_patters = re.compile(r'-\d{2}\Z')
year = re.findall(year_pattern, date)
month = re.findall(month_pattern, date)
day = re.findall(day_patters, date)
date_str = f"{day[0].replace('-', '')}-{month[0].replace('-', '')}-{year[0].replace('-', '')}"
print(date_str)


# Ex 7
def starts_with_digit(str):
    pattern = re.compile(r'\b\d')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} starts with a digit.")
    else:
        print(f"{str} does not start with a digit.")


starts_with_digit("12asdas")
starts_with_digit("adasdasd")


# Ex 8
def ends_with_digit(str):
    pattern = re.compile(r'\d\b')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} ends with a digit.")
    else:
        print(f"{str} does not end with a digit.")


ends_with_digit("asdasda")
ends_with_digit("sdasda12")

# Ex 9
def contains_digits(str):
    pattern = re.compile(r'\d')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} contains a digit.")
    else:
        print(f"{str} does not contain a digit.")

contains_digits("asdsa1sads")
contains_digits("Adasdas")