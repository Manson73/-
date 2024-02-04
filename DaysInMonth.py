import calendar

year = int(input('\nВведите год:'))
month = int(input('Введите месяц(1 - 12):'))

def monthdays():
    days = calendar.monthrange(year, month)[1]
    print('\nЧисло дней в этом месяце:', days)

def main():
    monthdays()
    input('\nНажмите Enter для завершения программы...')
    
if __name__ == '__main__':
    main()