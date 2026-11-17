#pets = {}
#inputting = True
#while inputting:
#    name = input("What is your pets name (press enter to stop inputting)? ")
#    try:
#        if name != "":
#            age = int(input("What is "+name+"'s age? "))
#            pets[name] = age
#        else:
#            inputting = False
#    except:
#        print("please enter an integer")
#print(pets)


class Dog():
    counter = 0

    def __init__(self, name, age, bark_sound):
        self.name = name
        self.age = age
        self.bark_sound = bark_sound
        Dog.counter += 1

    def bark(self):
        print(self.name+": "+self.bark_sound)

def read_dogs_csv(filename):
    f = open(filename, 'r')
    dogs = []
    for line in f:
        if not line.startswith("NAME"):
            s = line.split(',')
            dog = Dog(s[0], s[1], s[2])
            dogs.append(dog)
    f.close()
    return dogs



Joe = Dog("Joe", 23, "woof woof")
#print(Joe.age)
#Joe.bark()
#print(Dog.counter)

dogs = read_dogs_csv("dogs.csv")
print(dogs)
for dog in dogs:
    print(dog.name, dog.age, dog.bark_sound)