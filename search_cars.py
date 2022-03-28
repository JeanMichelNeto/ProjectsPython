list_cars = open('cars.txt')
# print(list_cars.read())
# print(list_cars.readline())
# print(list_cars.readline())

# print(list_cars.readlines()[0])  # prints only the first item

name_car = list_cars.readlines()[5]
print(name_car[3:18])
