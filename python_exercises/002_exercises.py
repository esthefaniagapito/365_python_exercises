"""
Write a Python program to calculate the sum of all prime numbers in a given list of positive integers.

Sample Data:
([1, 3, 4, 7, 9]) -> 10
([]) -> Empty list!
([11, 37, 444]) -> 48

"""

lista = [1, 3, 4, 7, 9]
sum = 0

if len(lista) == 0:
    print('Empty list!')
else: 
    for i in lista:
        cont = 0
        for x in range(1, i+1):
            if i % x == 0:
                cont += 1
        if cont == 2:
            sum += i
print(f'The sum of primers numbers is {sum}.')







