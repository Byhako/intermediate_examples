def run():
    dict1 = {i:i**3 for i in range(1,21) if i%3 != 0}
    print(dict1)

if __name__ == '__main__':
    run()
