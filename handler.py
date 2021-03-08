def handler_task_list(value):
    a1=['Монотонность','Линейность','Самодвойственность','Шефферовость','Базис','Полином Жегалкина','Оболочка']
    a2=['Монотонность','Сохранение','Сохранение 2','Сохранение 3','Шефферовость','Оболочка']
    a3=['Состояния','Эквивалентность','Суперпозиция']
    a4=['Алгоритм Квайна-МакКласки','Алгоритм Блейка','Алгоритм Блейка 2','Ядро','Тупиковые ДНФ']

    for i in range(len(a1)): a1[i]=str(i+1)+"."+a1[i]
    for i in range(len(a2)): a2[i]=str(i+1)+"."+a2[i]
    for i in range(len(a3)): a3[i]=str(i+1)+"."+a3[i]
    for i in range(len(a4)): a4[i]=str(i+1)+"."+a4[i]

    if value=="Выберите раздел":return "Выберите раздел"
    if value=="Алгебра логики":return "\n\n".join(a1)
    if value=="K-значная логика": return "\n\n".join(a2)
    if value=="Автоматы": return "\n\n".join(a3)
    if value=="Миним.булевых функций": return "\n\n".join(a4)


def generate_test(value1,value2):
    if value1=="Алгебра логики":
        if value2=="Монотонность":
            t=[['2 4 0000000000000001','1'],['2 4 0110100110010110','0']]
            return t

        if value2=="Линейность":
            t=[['2 4 0110100110010110','1'],['2 4 0000000000000001','0']]
            return t

        if value=="Самодвойственность":
            t=[]
            return t
        
    if value1=="K-значная логика":
        if value2=="Монотонность":
            t=[['5 2 0000001111012220123301234','1'],['5 2 0123412340234013401240123','0'],
            ['2 4 0000000000000001','1'],['2 4 0110100110010110','0']]
            return t
        if value2=="Сохранение":
            t=[['3 2 000011012','0\n01\n02\n1\n12\n2'],['3 2 000000000','0\n01\n02']]
            return t
        if value2=="Сохранение 2":
            t=[['5 3 1\n111 1','0\n1\n4'],['5 3 3\n001 1\n010 1\n100 1','0']]
            return t
        if value2=="Сохранение 3":
            t=[['3 2 000012021','0 12'],['3 2 012012012','0 12\n01 2\n02 1']]
            return t
        if value2=="Шефферовость":
            t=[['5 2 1234022340333404444000000','1'],['5 2 0123412340234013401240123','0']]
            return t
        if value2=="Оболочка":
            t=[['3 2 120220000'],
               ['3 1 000\n3 1 001\n3 1 002\n3 1 010\n3 1 011\n3 1 012\n3 1 020\n3 1 021\n3 1 022\n3 1 1003 1 101\n3 1 102\n3 1 110\n3 1 111\n3 1 112\n3 1 120\n3 1 121\n3 1 122\n3 1 200\n3 1 201\n3 1 202\n3 1 210\n3 1 211\n3 1 212\n3 1 220\n3 1 221\n3 1 222']]

    if value1=="Автоматы":
        if value2=="Состояния":
            t=[['2 00\n2 3 01100001\n2 3 00111011\n2 3 10010011',''],
               ['1 0\n2 2 1111\n2 2 0110',''],
               ['1 0\n2 2 1111\n2 2 1010','0 1'],
               ['1 0\n2 2 0101\n2 2 0011',''],
               ['2 10\n2 3 00011011\n2 3 01010110\n2 3 00110001','00 10'],
               ['5 00000\n2 6 0000000000000000000000000000001010111111111111111111111111111111\n2 6 0000000000000010101111111111110101000000000000101011111111111111\n2 6 0000001010111101010000101011110101000010101111010100001010111111\n2 6 0010100101101001011010010110100101101001011010010110100101101011\n2 6 1000110011001100110011001100110011001100110011001100110011001110\n2 6 0000000000000000000000000000000000000000000000000000000000000011',''],
               ['5 00000\n2 6 0000000000000000000000000000001010111111111111111111111111111111\n2 6 0000000000000010101111111111110101000000000000101011111111111111\n2 6 0000001010111101010000101011110101000010101111010100001010111111\n2 6 1010100101101001011010010110100101101001011010010110100101101011\n2 6 1010110011001100110011001100110011001100110011001100110011001110\n2 6 0000000000000000000000000000000000000000000000000000000000000011',
                '00000 00001 00000 00010 00001 00010'],
                ['2 00\n2 3 10101010\n2 3 11010101\n2 3 01011010','00 01 10 11']]
            return t

               




        

            
    
