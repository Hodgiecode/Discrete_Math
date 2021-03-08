class Task_04_02:
    def sort(self,td):
        ##отсортировка тднф лексикографически
        for i in range(len(td)):
            for j in range(i,len(td)):
                if len(td[i])<len(td[j]): #находим меньшую строку
                    a=len(td[i])
                else:
                    a=len(td[j])

                for l in range(a): #сравниваем посимвольно
                    if ( ((td[i][l] == '*') and (td[j][l] != '*')) or ((td[i][l] == '1') and (td[j][l] == '0')) ):
                        td[i],td[j]=td[j],td[i]

                    if ( ((td[i][l] == '0') and (td[j][l] != '0')) or ((td[i][l] == '1') and (td[j][l] == '*')) ):
                        break

        return td

    #Метод проверяет есть ли в массиве такая же коньюнкция   
    def equivalent_k(self,table,main_cnt,nw_kon,n):
        for i in range(main_cnt):
            isequil=1
            for j in range(n):
                if nw_kon[j]!=table[i][j]:
                    isequil=0
                    break
            if isequil==1:
                return 0
        return 1

    '''
    Метод, реализующий начало алгоритма Блейка
    Перебераем всевозможные пары коньюнкций, ссклеиваем пару, если возможно и проверяем нет ли такой же в массиве
    Если нет, то добавляем в массив.
    '''
    def bleyk(self,table,n,k):
        main_cnt=k
        for x in range(main_cnt):
            for y in range(main_cnt):
                if y!=x:
                    for m in range(n):
                        if table[x][m]!="*" and table[y][m]!="*" and int(table[x][m])==1-(int(table[y][m])):
                            nw_kon=[]
                            for i in range(n):
                                nw_kon.append("")
                            isnone=0
                            for h in range(n):
                                if h==m:
                                    nw_kon[h]='*'
                                else:
                                    if table[x][h]==table[y][h]:
                                        nw_kon[h]=table[x][h]
                                    else:
                                        if table[x][h]=="*" or table[y][h]=="*":
                                            if table[x][h]=="*":
                                                nw_kon[h]=table[y][h]
                                            else:
                                                nw_kon[h]=table[x][h]
                                        else:
                                            isnone=1 #Если 1, значит коньюнкция нулевая
                                            break
                                        
                            if not isnone: #Если не нулевая, то проверяем на наличие такоц же в массиве
                                if self.equivalent_k(table, main_cnt, nw_kon, n)==1:
                                    table[main_cnt]=nw_kon #добавляем в массив
                                    main_cnt=main_cnt+1
        return main_cnt
    
    def main(self,data):
       data=data.split('\n')
       n,m=data[0].split(" ")
       n=int(n)
       m=int(m)
       table=[]
       f=[]
       for i in range(m):f.append(0)
       
       for i in range(55*m):
           temp=[]
           for j in range(n): temp.append("")
           table.append(temp)

       for i in range(1,m+1):
           for j in range(len(data[i])):
               table[i-1][j]=data[i][j]
               

       head=self.bleyk(table,n,m)
       temp_table=[]
       for i in range(len(table)):
           if table[i][0]!="":
               temp_table.append(table[i])

       table=temp_table
       self.sort(table)

       print(n,len(table))
       for i in range(head):
           for j in range(n):
               print(table[i][j],end="")
           print()
      

f=open("in.txt","r",encoding="utf-8")
s=f.read()
f.close()

A=Task_04_02()
A.main(s)
