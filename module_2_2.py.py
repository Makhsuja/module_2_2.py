first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first == second and second == first and first == third and third == first and second == first and first == second:
    print(3)
elif first == second and second == first:
    print(2)
elif first == third and third == first:
    print(2)
elif second == third and third == second:
    print(2)
elif first == second:
    print(1)
elif second == third:
    print(1)
elif third == first:
    print(1)
else:
    print(0)