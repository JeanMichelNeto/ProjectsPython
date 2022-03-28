
# print(list_cars.read())
# print(list_cars.readline())
# print(list_cars.readline())

# print(list_cars.readlines()[0])  # prints only the first item
def cars_number():
    list_cars = open('cars.txt')
    name_car = list_cars.readlines()[0]
    # print(name_car[3:18])
    list_cars.close()  # close this file
    list_customers = open('customers.txt')

    for customers in list_customers:
        print('Hello', customers,
              'The best selling car was yours in 2021', name_car[3:18], 'congratulations')


cars_number()
