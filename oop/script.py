# name = 'abdullah';
# age = '38';
# print(name, age);
# print(type(name), type(age));

# # declare create a class


# class Person:
#     def __init__(self, name, age):  # Correct attribute names
#         self.name = name  
#         self.age = age  

#     def speak(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # Correct way to create an object
# dogs = Person('abdullah', 38)  # Separate name and age


# # Printing attributes
# print(dogs.name, dogs.age)  # This will print: abdullah 38

# # Calling the method
# dogs.speak()  # Output: Hello, my name is abdullah and I am 38 years old.


# class Person:
#     def __init__(self,name,age):
#         self.nam = name;
#         self.ag = age;
      

#     def bark(self):
#         print('whoof whoof');

# dogs = Person('abdullah, 38');
# print(dogs.name,dogs.age);
# dogsas = Person('kawser, 80');
# print(dogsas.name,dogsas.age);
# # dog.bark();


# Combining objects
class Dogs:
    def __init__(self, name, age, color, owner):
        self.name = name #storing value
        self.age = age
        self.color = color
        self.owner = owner  # Correctly assign the owner object

    def bark(self): # defining methon
        print('whoof whoof')

class Owner:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

# Correct variable name and instantiation
owner = Owner('Abdullah', 'Dhaka', 847755)

# Pass the 'owner' object without parentheses
person = Dogs('Kawser', 30, 'black', owner)
print(person.owner.name)

# Print details
print(person.name, person.age, person.color)
person.bark()
