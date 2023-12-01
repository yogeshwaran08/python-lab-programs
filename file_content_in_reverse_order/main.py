with open("sample.txt","r") as my_file:
    lines = my_file.readlines()
    for i in lines:
        print(i[::-1])