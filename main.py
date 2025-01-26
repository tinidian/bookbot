
def open_file():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def print_book():
    file_contents = open_file()
    print(file_contents)

def print_word_count():
    file_contents = open_file()
    words = file_contents.split()
    print(len(words))

def count_characters():
    file_contents = open_file()
    file_contents = file_contents.lower()
    chars = {}

    for char in file_contents:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    print(chars)

def sort_on(dict):
    return dict["count"]

def print_report():
    file_contents = open_file()
    file_contents = file_contents.lower()
    chars = {}

    for char in file_contents:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    report_chars = []

    for char in chars:
        if char.isalpha():
            report_chars.append({"name":char, "count": chars[char]})
    
    report_chars.sort(reverse=True, key=sort_on)

    for report in report_chars:
        name = report["name"]
        count = report["count"]
        print(f"The \'{name}\' character was found {count} times")
  

# count_characters()
print_report()