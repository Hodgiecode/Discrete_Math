class Task_01_05:
    def __init__(self):
        self.table=[]
        
   
    def main(self,data):
        data=data.split('\n')
        funcquan=int(data[0])
        task=[]
        data=data[1:]
        for i in range(funcquan):
            tmp=data[i].split(" ")
            task.append([int(tmp[0]),int(tmp[1]),tmp[2]])
        table=[]

        #двумерный массив для таблицы
        for i in range(funcquan):
            temp=[]
            for j in range(5):
                temp.append(0)
            table.append(temp)

        for i in range(funcquan):
            length=1<<task[i][1]
            vect=task[i][2]
            
            #проверка на принадлежность функции классу T0
            if vect[0]=='0': table[i][0]=1
            #проверка на принадлежность функции классу T1
            if vect[length-1]=='1': table[i][1]=1

            p=0
            c=0
            l=0
            while (length>1):
                length=length/2 #делим вектор значений пополам и проверяем на совпадение либо отрицание, то есть фиктивность переменной либо линейную зависимость функции от нее
                for j in range(int(length)):
                    if vect[j]==vect[j+int(length)]: p=p+1
                if p==length:
                    l=l+1 #количество фиктивных переменных
                    p=0
                else:
                    p=0
                    for j in range(int(length)):
                        if vect[j]!=vect[j+int(length)]: p=p+1
                    if p==length:
                        c=c+1
                        p=0
                    else:
                        c=0 #нелинейная
                        break

            #проверка на принадлежность функции классу L
            if ((l==task[i][1]) or (c!=0)): table[i][2]=1 

            length=1<<task[i][1]
            for j in range(int(length/2)):
                if vect[j]=='0' and vect[length-1-j]=='1' or vect[j]=='1' and vect[length-1-j]=='0':
                    continue
                else:
                    break

            if j==length/2: table[i][3]=1 #проверка на принадлежность функции классу S

            p=0
            while (length>0):
                length=length/2
                for j in range(int(length)):
                    if int(vect[j])>int(vect[j+int(length)]): #проверка на немонотонность по соседним наборам
                        p=1
                        break #немонотонна
                if p==1:
                    break
                if length==1:
                    table[i][4]=1 #проверка на принадлежность функции классу M 

        for i in range(-1,funcquan): #без какой ф-ии проверяем систему на полноту, при i = -1  - проверяем всю таблицу на полноту
            rtn=1
            for j in range(5):#в каком столбце считаем количество +
                kp=0 #количество +
                for l in range(funcquan): #какую ячейку в столбце j проверяем на наличие +
                    if l!=i: #не проверяем строку с номером i
                        if table[l][j]==1:
                            kp=kp+1

                if i!=(-1) and kp==funcquan-1: break #система перестает быть полной, если убрать одну функцию

                #Если даже с выкинутой ф-ией система полна, то эта система не базис. Или если вся система не полна, то она тоже не базис*/
                if ((i!=(-1) and kp!=funcquan-1 and j==4) or (i==(-1) and kp==funcquan)):
                    rtn=0 #не базис
                    break

            if rtn==0: break #не базис
                
        return rtn    

