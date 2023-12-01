count = 0
f = input("Enter the filename : ")
with open(f,"r") as file:
    letter = input("Enter the letter : ")
    for i in file:
        words = i.split()
        for word in words:
            for char in word:
                if(char == letter):
                    count += 1
print(count)
