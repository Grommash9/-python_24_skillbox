from circle import Circle

first_circle = Circle(0, 0)
second_circle = Circle(1, 1)
third_circle = Circle(5, 5)
fourth_circle = Circle(0, 0, 20)

print('Сравнение первого и второго круга: ', first_circle.is_crossing(second_circle))
print('Сравнение третьего и четвертого круга: ', third_circle.is_crossing(fourth_circle))
print('Сравнение первого и третьего круга до увеличения первого: ', first_circle.is_crossing(third_circle))

print(first_circle.info())
first_circle.increase(10)
print(first_circle.info())

print('Сравнение первого и третьего круга после увеличения первого: ', first_circle.is_crossing(third_circle))
