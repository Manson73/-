
def numbercount():
    number = int(input('\nВведите любое число:'))
    str_number = str(number)
    sum = 0

    for i in str_number:
        sum += int(i)
    print('\nСумма введенных чисел:', sum)

def main():
    numbercount()
    print('\nНажмите Enter для завершения программы...')

if __name__ == '__main__':
    main()