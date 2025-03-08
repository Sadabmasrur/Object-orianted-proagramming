class Dog:
    
    species = "Dog"
    
    def __init__(self, name, age, breed, anger_level, color, weight):
        self.name = name
        self.age = age
        self.breed = breed
        self.anger_level = anger_level
        self.color = color
        self.weight = weight


d1 = Dog("Budy", 5, "Golden Retriever", "Low", "Golden", 30)
d2 = Dog("Maxxy", 3, "Bulldog", "High", "Brown", 25)
d3 = Dog("Rocky", 7, "German Shepherd", "Medium", "Black & Tan", 35)
d4 = Dog("Charcoal", 4, "Labrador", "Low", "Yellow", 32)
d5 = Dog("Mad", 2, "Beagle", "Medium", "Tri-color", 12)
d6 = Dog("Lafda", 6, "Husky", "High", "White & Gray", 28)

print(f"{d1.name} is a {d1.species}")  
print(f"{d2.name} is a {d2.species}")  
print(f"{d3.name} is a {d3.species}")  
print(f"{d4.name} is a {d4.species}")  
print(f"{d5.name} is a {d5.species}\n\n")

print(f"Name: {d1.name}, Age: {d1.age}, Breed: {d1.breed}, Anger Level: {d1.anger_level}, Color: {d1.color}, Weight: {d1.weight} kg\n")
print(f"Name: {d2.name}, Age: {d2.age}, Breed: {d2.breed}, Anger Level: {d2.anger_level}, Color: {d2.color}, Weight: {d2.weight} kg\n")
print(f"Name: {d3.name}, Age: {d3.age}, Breed: {d3.breed}, Anger Level: {d3.anger_level}, Color: {d3.color}, Weight: {d3.weight} kg\n")
print(f"Name: {d4.name}, Age: {d4.age}, Breed: {d4.breed}, Anger Level: {d4.anger_level}, Color: {d4.color}, Weight: {d4.weight} kg\n")
print(f"Name: {d5.name}, Age: {d5.age}, Breed: {d5.breed}, Anger Level: {d5.anger_level}, Color: {d5.color}, Weight: {d5.weight} kg\n")