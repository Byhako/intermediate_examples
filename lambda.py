def run(string):
    return string == string[::-1]

palindrome = lambda string: string == string[::-1]


if __name__ == '__main__':
    print(run('ana'))
    print(palindrome('ana'))