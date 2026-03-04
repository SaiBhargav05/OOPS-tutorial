## how intitiate a classs
class Employee:
    # special function/dunder method - constructor
    def __init__(self):
        print(id(self))
        #print("Started executing the attributes/ data")
        self.id =123
        self.salary=25000
        self.designation="SDE"
        #print("attributes/data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Travelling to {destination}")



# creating an object of the class Employee     
sam = Employee()
sam.name = "sam kumar" ## we can add attributes even outside the constructor
print(sam.name) ## we can access the attributes even outside the constructor
#print(id(sam)) ## what we observe here is that the id of the object sam is same as the id printed in the constructor which means that the constructor is automatically called when we create an object of the class and it initializes the attributes of the class for that object.

# hero = Employee() 
# print(id(hero)) 
# printing attributes
#print(sam.id)
## calling a method
#sam.travel("New York")

print(type(sam))

