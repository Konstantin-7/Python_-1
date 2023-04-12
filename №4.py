# Задача 4.
# Напишите программу, которая на вход
# принимает число(N), а на выходе показывает все чётные
# числа от 1 до N.

# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

N = int(input('Введите любое положительное число N : '))
count = int(1)
print(f'{N} -> ', end='')

if 0 < count <= N:
    while count <= N:
        if count % 2 == 0 and count != N:
            print(f'{count}, ', end='')
            count += 1
        elif count == N:
            print(f'{count} ', end='')
            count += 1
        else:
            count += 1
else:
    print(f'Такой число не подходит: {N}')
