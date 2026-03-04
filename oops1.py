## how intitiate a classs
class Employee:
    # special function/dunder method - constructor
    def __init__(self):
        print("Started executing the attributes/ data")
        self.id =123
        self.salary=25000
        self.designation="SDE"
        print("attributes/data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Travelling to {destination}")



# creating an object of the class Employee     
sam = Employee()
# printing attributes
#print(sam.id)
## calling a method
#sam.travel("New York")

print(type(sam))

