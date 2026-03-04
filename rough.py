# lst = [1,2,3]
# mystr = "Mlops playlist"
# my_int = 125


# print(type(lst))
# print(type(mystr))
# print(type(my_int)) 

from oops_project import chatbook
user1 = chatbook()
print(user1.id)

chatbook.set_id(100)

user2 = chatbook()
print(user2.id)

# getter and setter methods are shown in the below code snippet
# print(user1.get_name())
# user1.set_name("Hero")
# print(user1.get_name())


# function vs method is shown in the below code snippet

# lst = [1,2,3]


# # function 
# a1 = len(lst)
# print(a1)   

# #method
# user1 = chatbook()
# user1.send_message()


