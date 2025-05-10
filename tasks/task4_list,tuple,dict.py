#task (list):
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.remove(2)
print(numbers)

sum=0
for j in numbers:
    sum+=j
print("total sum:", sum)



#task (tuple):
cities = ("milan", "dhaka", "warsaw", "constantinople", "canbera")
print(cities[2])
cityList = list(cities)
cityList.append("paris")
newCities = tuple(cityList)
print(newCities)



#task (dictionary):
subjects = {
    "dsd": 89,
    "mnm": 56,
    "dbms": 67
}
subjects["math2"] = 78
subjects["dbms"] = 90
print(subjects)