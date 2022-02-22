def read():
    numbers = []
    with open('./numeros.txt', 'r', encoding='utf-8') as file:
        for line in file:
            numbers.append(int(line))

    print(numbers)


def write():
    names = ['Toto', 'Lala', 'Nala', 'Rino']
    with open('./nombres.txt', 'w', encoding='utf-8') as file:
        for n in names:
            file.write(f'{n}\n')


def run():
    read()
    write()


if __name__ == '__main__':
    run()