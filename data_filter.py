from data import DATA

def run():
    all_python = [item['name'] for item in DATA if item['language'] == 'python']
    print(all_python)
    adults = list(filter(lambda item: item['age'] > 18, DATA))
    adults = list(map(lambda item: item['name'], adults))
    print('Adultos: ', adults)

    #Agregamos nueva key adult boolean
    is_adult = list(map(lambda item: {**item, 'adult': item['age']>18}, DATA))
    print(is_adult)
if __name__ == '__main__':
    run()