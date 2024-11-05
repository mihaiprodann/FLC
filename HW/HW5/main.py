import re
import openpyxl
import pandas as pd

# Excercise 1

ex1 = open(r"ex1.html", "r").read()
ex2 = open(r"ex2.txt", "r")


## a)
def display_links():
    pattern = re.compile(r'<a href="(.*)">')
    matches = re.findall(pattern, ex1)
    for match in matches:
        print(match)


## b)
def display_labels():
    pattern = re.compile(r'<label for="(.*)">(.*)(</label>)')
    matches = re.findall(pattern, ex1)
    for match in matches:
        print(match[1])


## c)
def display_attributes():
    pattern = re.compile(r'<input\s+[^>]*type=["\']([^"\']+)["\']')
    matches = re.findall(pattern, ex1)
    for match in matches:
        print(match)


## d)
def display_options():
    pattern = re.compile(r'<option\s+[^>]*value=["\']([^"\']+)["\']')
    matches = re.findall(pattern, ex1)
    for match in matches:
        print(match)


## e)
def display_ids():
    pattern = re.compile(r'id=["\']([^"\']+)["\']')
    matches = re.findall(pattern, ex1)
    for match in matches:
        print(match)


display_links()
display_labels()
display_attributes()
display_options()
display_ids()


# Excercise 2

def create_xslx():
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for i, line in enumerate(ex2):
        line = line.split(',')
        for j, word in enumerate(line):
            sheet.cell(row=i + 1, column=j + 1).value = word

    workbook.save("ex2.xlsx")


create_xslx()

print()


# Excercise 3
def check_correctness(text):
    pattern = re.compile(r'<[a-zA-Z][a-zA-Z0-9]*(\s+[a-zA-Z-]+=(["\'])[^\2]*?\2)*\s*/?>')
    match = re.fullmatch(pattern, text)
    if match:
        print(f"'{text}' : The tag is correct.")
    else:
        print(f"'{text}' : The tag is incorrect.")


check_correctness("<a href='https://www.google.com'>")
check_correctness("<img src='image.png' />")
check_correctness("<div class='container'>")
check_correctness("<br>")
check_correctness("<input type='text' />")
check_correctness("<p")
check_correctness("p>")
