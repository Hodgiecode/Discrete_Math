'''
Задача: во входном файле задана ф-ия от 2-х переменных. Яв-ся ли она шефферевой?
Решение: шефферовость ф-ии я проверяю по критерию Слупецкого: 1) Ф-ия должна принимать k значений(от 0 до k-1 включ-но);
2) функция должна содержать хотя бы две существенные переменные(в данной задаче не должно быть фиктивных переменных, т.к. задана 
ф-ия от 2-х переменных; 3) Из данной ф-ии от двух переменных нужно получить все одноместные ф-ии(их кол-во k^k)
'''
class Task_02_05():
    def check_symbol(self,c):#проверка символа
        if (c>='A' and c<='Z'): #если взятый из файла символ - буква, то...
            return ord(c)-ord('A')+10; #записываем в i-тую позицию число,соответствующее этой букве
        else:
            if(c>='0' and c<='9'):#(если сканируемый символ - цифра, то...)
                return int(c);#переводим символ в цифру и записываем её в i-ую позицию массива
            else:
                return -1;

    def check_number_of_func_results(self, kolvo,kolvoznac,vect,k): #проверка принимает ли ф-ия к зн-ий
        for i in range(kolvo):
            kolvoznac[vect[i]]=kolvoznac[vect[i]]+1
            #в массиве колвозначений всего к ячеек, и мы увеличиваем одну из этих ячеек, соответсвующих числу,
            #стоящему на i - той позиции в массиве векторзначени

        for i in range(k):
            if(kolvoznac[i]==0): #если хоть одна из ячеек от 0 до к-1 позиции равна нулю, значит ф-ия не принимает это значение=>она не шефферова
                return 0 #если не принимает к - значений
  
        return 1 #если принимает к значений

    def main(self,data):
        data=data.split(" ")
        k=int(data[0]) #значность логики
        n=int(data[1]) #количество переменных
        vect=[]
        kolvoznac=[]
        for i in range(k**n):
            if (self.check_symbol(data[2][i]))!=-1:
                vect.append(self.check_symbol(data[2][i]))
                
        for i in range(k): kolvoznac.append(0) #нужен для определения принимает ли ф-ия к-значений

        peremennie=[]
        for i in range(k**n):
            tmp=[]
            for j in range(n): tmp.append(0)
            peremennie.append(tmp)

        ###проверка, принимает ли функция все к значений
        res = self.check_number_of_func_results(k**n,kolvoznac,vect,k)
        
        if res==0:
            return "0"
        
        ###конец проверки(если принимает к значений, то начнём получать все одноместные ф-ии)
        for i in range(k**n): #заполнение переменных, перебираем все значения переменных
            integer_part=i #изначально целая часть = i
            for j in range(n): #получаем переменные,то есть производится перевод каждого числа от 0 до k**n в k-тую систему счисления
                mod_part=integer_part%k #находим остаток от деления на значность логики
                integer_part=float(integer_part)/k
                peremennie[i][n-j-1]=int(mod_part)

        #проверка кол-ва одноместных ф-ий
        super_position_func=[] # вектор значений, получившейся одноместной ф-ии,этот массив нужен для сравнения с другими уже имеющемися
        for i in range(k): super_position_func.append(0)
        kolvo_odnomest=k**k #всего одноместных ф-ий - k в степени k
        vse_odnomest_func=[]

        for i in range(kolvo_odnomest+1):
            tmp=[]
            for j in range(k): tmp.append(0)
            vse_odnomest_func.append(tmp)

        for i in range(k):
            vse_odnomest_func[0][i]=i #занесём в первую строку значения от 0 до k-1,это селекторные ф-ии,они всегда порождены

        counter=1 #счётчик увеличиватся, если мы не получали какую-ту одноместную ф-ию в рез-те ср-ния i той с j-тыми.если j=счётчику,то начинаем получать ф-ии из (i+1)ой и j-тыми

        for i in range(kolvo_odnomest): #начало построения одноместных ф-ий
            for j in range(kolvo_odnomest):
                for g in range(k):
                    super_position_func[g]=vect[vse_odnomest_func[j][g]+(vse_odnomest_func[i][g]*k)]; # суперпозиция функций
                    
                for h in range(counter):
                    local_counter=0 #изначально счетчик равен 0
                    for v in range(k):
                        if(super_position_func[v]==vse_odnomest_func[h][v]):
                            local_counter=local_counter+1 #счетчик значений

                    if (local_counter==k):#если мы уже получали эту одноместную ф-ию
                        break;

                if(local_counter!=k): #если получены не все значения, то продолжаем суперпозицию
                    for s in range(k):
                        vse_odnomest_func[counter][s]=super_position_func[s] #запоминаем в двумерном массиве вектор значений какой-то одноместной ф-ии

                    counter=counter+1 #считает кол-во одноместных ф-ий

            if counter==kolvo_odnomest:
                break
              
        if counter==kolvo_odnomest:
            return "1"
        else:
            return "0"
        


