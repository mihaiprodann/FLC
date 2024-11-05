def stateAex1(x):
    if x == '1':
        return 1
    else:
        return -1


def stateBex1(x):
    if x == '1':
        return 2
    else:
        return -1


def ex1(String):
    l = len(String)
    dfa = 0
    for i in range(l):
        if dfa == 0:
            dfa = stateAex1(String[i])
        elif dfa == 1:
            dfa = stateBex1(String[i])
        elif dfa == 2:
            dfa = stateAex1(String[i])
        else:
            return "The string doesn't belong to the language 1+"
    if dfa == 2:
        return "The string belongs to the language 1+"
    else:
        return "The string doesn't belong to the language 1+"


print("\nEX1")
test_strings = ["1", "11", "111"]
for test_string in test_strings:
    result = ex1(test_string)
    print(f"String {test_string}: {result}")


# Ex2: language is ((00)+1+)
def stateAex2(x):
    if x == '0':
        return 1
    return -1


def stateBex2(x):
    if x == '0':
        return 2
    return -1


def stateCex2(x):
    if x == '1':
        return 5
    if x == '0':
        return 3
    return -1


def stateDex2(x):
    if x == '0':
        return 4
    if x == '1':
        return 5
    return -1


def stateEex2(x):
    if x == '1':
        return 6
    return -1


def stateFex2(x):
    if x == '0':
        return 3
    if x == '1':
        return 5
    return -1


def stateGex2(x):
    if x == '1':
        return 6
    return -1


def ex2(String):
    l = len(String)
    dfa = 0
    for i in range(l):
        if dfa == 0:
            dfa = stateAex2(String[i])
        elif dfa == 1:
            dfa = stateBex2(String[i])
        elif dfa == 2:
            dfa = stateCex2(String[i])
        elif dfa == 3:
            dfa = stateDex2(String[i])
        elif dfa == 4:
            dfa = stateEex2(String[i])
        elif dfa == 5:
            dfa = stateFex2(String[i])
        elif dfa == 6:
            dfa = stateGex2(String[i])

        if dfa == -1:
            return "The string doesn't belong to the language ((00)+1+)"

    if dfa == 6:
        return "The string belongs to the language ((00)+1+)"
    else:
        return "The string doesn't belong to the language ((00)+1+)"


print("\nEX2")
test_strings = ["001", "0001", "0000"]
for test_string in test_strings:
    result = ex2(test_string)
    print(f"String {test_string}: {result}")


def start_state(char):
    if char.isalpha():
        return 1
    return -1


def middle_state(char):
    if char.isalpha():
        return 1
    return -1


def final_state(char, starting_char):
    if char == starting_char:
        return 3
    return -1


def check_word_dfa(word):
    if not word:
        return "The string does not belong to the language"

    starting_char = word[0]
    current_state = start_state(starting_char)

    if current_state == -1:
        return "The string does not belong to the language"

    for char in word[1:-1]:
        current_state = middle_state(char)
        if current_state == -1:
            return "The string does not belong to the language"

    current_state = final_state(word[-1], starting_char)
    if current_state == 3:
        return "The string belongs to the language"
    else:
        return "The string does not belong to the language"


print("\nEX3")
test_strings = ["radar", "hello", "ana", "world"]

for test_string in test_strings:
    result = check_word_dfa(test_string)
    print(f"String {test_string}: {result}")
