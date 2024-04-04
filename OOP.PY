#Create a Python class named Person.
#The Person class should have the following attributes:
#name: representing the person's name.
#age: representing the person's age.
#gender: representing the person's gender.
#Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
#Create an instance of the Person class and call the introduce method to display the person's information.


class Person:
    def __init__(mtu, name, age, gender):
        mtu.name = name
        mtu.age = age
        mtu.gender = gender
    
    def calling(mtu):
        print(f" My name is {mtu.name}. and I am {mtu.age} years and Am also a  {mtu.gender}.")

# An instance of the Person class
PERSON = Person("John", 30, "male")

# To the introduce method to display the person's information
PERSON.calling()
