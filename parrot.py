class Parrot:
    
    species="bird"
    
    def __init__(self, name, age):
        self.name=name
        self.age=age

blu=Parrot("Blu",10) 
woo=Parrot("woo",15)

print(f"Blu is a {blu.species}")       
print(f"Woo is a {woo.species}")

print()

print(f"{blu.name} is {blu.age}")            
print(f"{woo.name} is {woo.age}")       