import os

def readfile(path):
    with open(path) as f:
        return f.read()

def countchar(file):
    file = file.lower()
    chars = {}
    for i in file:
        if i in chars:
            chars[i] += 1
        elif i.isalpha():
            chars[i] = 1

    return dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))


def countwords(file):
    return len(file.split())


def main():
    file = readfile('books/frankenstein.txt') 
    chars = countchar(file)
    print(f"-- Begin report of 'books/frankenstein.txt' --\n ")
    print(f"Number of words: {countwords(file)}\n")
    for x, y in chars.items():
        print(f"The '{x}' character was found {y} time")
    print(f"\n-- End of report --")

main()
        
