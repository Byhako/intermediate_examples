def divisors(num):
    divisor = []
    for i in range(1, num+1):
        if num%i == 0:
            divisor.append(i)

    return divisor

def run():
    try:
        num = int(input('Ingresa un numero: '))
        if num<1:
            raise ValueError
        print(divisors(num))
    except ValueError:
        print('Debes ingresar un numero entero mayor a cero.')

    print('-- end --')


def run2():
    num = input('Ingresa un numero: ')
    assert num.isnumeric() and int(num)>0, 'Debes ingresar un numero entero mayor a cero.'
    print(divisors(int(num)))
    print('-- end --')

if __name__ == '__main__':
    run2()