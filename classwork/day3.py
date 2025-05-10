data = [1 , 4, 5, 6]    #list, mutable
data.append(3)
data.remove(5)
print(data)




data1 = (1 , 4, 5, 6)    #tuple, immutable
#data1.append(3)   error dey
print(data1)
xData1 = list(data1)
xData1.append(3)
print(xData1)





dict = {                     #dictionary, mutable
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

print(dict)
dict["age"] = 31
print(dict)
dict["country"] = "USA"
print(dict)
del dict["age"]
print(dict)




cities = {
    ("paris", "monaco") : "france",
    ("berlin", "munich") : "germany",
    ("madrid", "barcelona") : "spain"
}

print(cities)
print(cities[("paris", "monaco")])



#############################



def func(x,y):
    return x + y

print(func(2,3))



#############################


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print("moving")

person1 = Person("oblak", 30)
person1.move()
print(person1.name)
print(person1.age)