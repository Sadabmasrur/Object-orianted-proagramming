class student:
    
    #class variable
    grade = 8
    
    
    #constructor
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        
liban =student("Liban PaUL",13)
sadab =student("SadabSi",15) 

print(liban.grade)
print(sadab.grade)

print(f"My name is {liban.name} and my age is {liban.age}")       
print(f"My name is {sadab.name} and my age is {sadab.age}")  