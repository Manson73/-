
def CtoF():
    c = float(input('Введите температуру по цельсию: '))

    f = c * 9/5 + 32
    print('\nF° =', f)

def FtoC():
    f = float(input('Введите температуру по фарингейту: '))
    
    t = f - 32
    c = 5/9 * t
    print('\nC° =', c)

def main():
    a = input('\nВведите метод расчета (1)C->F (2)F->C:')

    if (a == '1'):
        CtoF()
    elif(a == '2'):
        FtoC()
    else:
        print('Error...')

    input('\nНажмите Enter для завершения программы...')

if __name__ == '__main__':
    main()