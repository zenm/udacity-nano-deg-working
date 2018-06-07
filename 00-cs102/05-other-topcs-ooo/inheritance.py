class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

# darth_vadar = Parent("Skywalker", "black")
# print(darth_vadar.last_name)

luke_skywalker = Child("Skywalker", "hope", 1)
print(luke_skywalker.last_name)
print(luke_skywalker.number_of_toys)
