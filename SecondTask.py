first_num=int(input('Введите первое значение: '))
print('Введите один из символов: \n\'+ - сложение\' \n\'- - вычитание\' \n\'* - умножение\' \n\'/ - деление\' \n\'// - целочисленное деление\' \n\'% - остаток от деления\' \n\'** - возведение в степень\' \n\'== - равно\' \n\'!= - не равно\' \n\'> - больше\' \n\'< - меньше\' \n\'>= - больше или равно\' \n\'<= - меньше или равно\'')
znack=input()
second_num=int(input('Введите второе число: '))
if(znack is ''):
    print('Вы не вписали знак')
else:
    if(znack =='+'):
        print(first_num+second_num)
    elif(znack =='-'):
        print(first_num+second_num)
    elif(znack=='*'):
        print(first_num*second_num)
    elif('/' in znack or znack=='%'):
        if(second_num==0):
            print('На 0 делить нельзя')
        else:
            if('%' not in znack):
                if(znack=='/'):
                    print(first_num/second_num)
                elif(znack=='//'):
                    print(first_num//second_num)
                else:
                    print('Неизвестный знак')
            elif(znack=='%'):
                print(first_num%second_num)
            
    elif(znack=='**'):
        print(first_num%second_num)
    elif('=' in znack):
        if(znack=='=='):
            print(first_num is second_num)
        elif('!' in znack):
            print(first_num is not second_num)
        elif('>' in znack):
            print(first_num>=second_num)
        elif('<' in znack):
            print(first_num<=second_num)
    elif(znack=='>'):
        print(first_num>second_num)
    elif(znack=='<'):
        print(first_num<second_num)
    else:
        print('Символ не найден')
        
