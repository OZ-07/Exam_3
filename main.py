

"""def greet(name):
    print("Hello, " + name + "!")


if __name__ == '__main__':
    alice = "Alice"
    greet(alice)
    print(alice)"""
"""
def conditional(x):
    if x > 5:
        print( "x is greater than 5" )
    else:
        print( "x is less than or equal to 5" )


if __name__ == '__main__':
    y = 10
    conditional(y)"""
"""
class YourClass:
    def greet(self):
        return "Hello"

class MyClass(YourClass):
    def __init__(self, name):
        self.name = name

    def get_your_name(self):
        print(f'{self.greet()} {self.name}')

if __name__ == '__main__':
    my_object = MyClass('Trevor')
    my_object.get_your_name()"""
my_tuple = 1,2,3,4
my_string = "Hello, World!"
my_dict = {"name": "Alice", "age": 30}
my_list = [1, 2, 3]
my_list.extend( [4, 5] )

def main():
    """    for i in "Python":
        print(i, end="")"""
    #print(my_tuple[2])
    #print(my_tuple(2))
    #print(my_string[7])
    #my_dict['age'] = 32
    #my_dict[32] = 'age' doesn't work
    #my_dict.age = 32 doesn't work
    print(my_dict["name"]) #no effect
    #my_dict.value("name") "error no value obj"
    print(my_dict.get("name"))
    #print(my_dict

    print(my_list)


if __name__ == '__main__':
        main()