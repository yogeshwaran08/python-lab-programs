num_of_words = 0
num_of_lines = 0
num_of_chars = 0

with open("sample.txt",'r') as file:
    for i in file:
        num_of_lines += 1
        num_of_words += len(i.split())
        num_of_chars += len(i)
    print(num_of_chars)
    print(num_of_lines)
    print(num_of_words)
