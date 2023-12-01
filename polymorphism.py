class dog:
    def sound():
        print("boww bow")
class cat():
    def sound():
        print("Meow meow")
     
def makeSound(obj):
    obj.sound()   
catObj = cat
dogObj = dog
makeSound(catObj)
makeSound(dogObj)
