# Es una funcion que recibe como parametro otra funcion.

from functools import reduce


list1 = [i for i in range(1,21)]

# Filter
def is_impar(x):
    return x%2 != 0

# print('Filter', list(filter(lambda x : x%2 != 0, list1)))
print('Filter', list(filter(is_impar, list1)))


# Map
def square(x):
    return x**2

# print('Map ', list(map(lambda x : x**2, list1)))
print('Map ', list(map(square, list1)))

# Reduce
def multiplication(a,b):
    return a*b

print('Reduce ', reduce(lambda a, b: a*b, list1))
# print('Reduce ', reduce(multiplication, list1))