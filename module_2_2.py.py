first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and first == third and second == third:
    print(3)
elif first == second and second == first:
    print(2)
elif first == third and third == first:
    print(2)
elif second == third and third == second:
    print(2)
else:
    print(0)
