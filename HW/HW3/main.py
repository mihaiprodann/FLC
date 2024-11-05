import re


# Ex1
print("\nEx1")
def contains_specific_no1(str):
    pattern = re.compile(r'^[a-z0-9*]+$')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} contains only lowercase letters, digits and *.")
    else:
        print(f"{str} does not contain only lowercase letters, digits and *.")

contains_specific_no1("asdasd123*")
contains_specific_no1("asdasd123*#")


# Ex2
print("\nEx2")
def contains_specific_no2(str):
    pattern = re.compile(r'^[A-Z]+_[a-z]+$')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} has the pattern: word containing only uppercase letters _ word containing only lowercase letters.")
    else:
        print(f"{str} does not have the pattern: word containing only uppercase letters _ word containing only lowercase letters.")

contains_specific_no2("FILS_student")
contains_specific_no2("FILS_Student")


# Ex3
print("\nEx3")
hw4 = "rectangle square sphere triangle cone cube cylinder"
pattern = re.compile(r'\b\w+(le|re)\b')
matches = re.findall(pattern, hw4)
print(matches)


# Ex4
print("\nEx4")
ex4 = "able cable table stable structure lecture future culture"
pattern = re.compile(r'\b\w+(le|re)\b')
matches = re.findall(pattern, ex4)
print(matches)
for match in matches:
    print(match)

# Ex5
print("\nEx5")
def change_date_format(date):
    year_pattern = re.compile(r'\d{4}-')
    month_pattern = re.compile(r'\b-\d{2}-')
    day_patters = re.compile(r'-\d{2}\Z')
    year = re.findall(year_pattern, date)
    month = re.findall(month_pattern, date)
    day = re.findall(day_patters, date)
    date_str = f"{day[0].replace('-', '')}-{month[0].replace('-', '')}-{year[0].replace('-', '')}"
    print(date_str)

change_date_format("2003-01-26")
change_date_format("2003-11-07")

# Ex6
print("\nEx6")
def match_m_n(str):
    pattern = re.compile(r'^m[a-z]{3}n$')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} matches the pattern.")
    else:
        print(f"{str} does not match the pattern.")

match_m_n("mabcn")
match_m_n("mabcn1")
match_m_n("mabscn")

# Ex7
print("\nEx7")
def match_h_i(str):
    pattern = re.compile(r'^hii{2,3}$')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} matches the pattern.")
    else:
        print(f"{str} does not match the pattern.")

match_h_i("hii")
match_h_i("hiii")
match_h_i("hiiii")

# Ex8
print("\nEx8")
def match_q(str):
    pattern = re.compile(r'\b\w*q\w*\b')
    matches = re.findall(pattern, str)
    if len(matches) > 0:
        print(f"{str} matches the pattern.")
    else:
        print(f"{str} does not match the pattern.")

match_q("qweqwe")
match_q("qweqweq")

# Ex9
print("\nEx9")
def replace_a_i(str):
    new_str = str.replace('a', 'u').replace('i', 'e')
    print(new_str)

replace_a_i("asdasd")
replace_a_i("isdisd")