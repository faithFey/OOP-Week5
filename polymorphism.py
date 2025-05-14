class Animal:
    def move(self):
        print("This animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("The dog runs 🐕")

class Fish(Animal):
    def move(self):
        print("The fish swims 🐟")

class Bird(Animal):
    def move(self):
        print("The bird flies 🐦")

# List of animals
animals = [Dog(), Fish(), Bird()]

# Loop through and call their move() method
for animal in animals:
    animal.move()
