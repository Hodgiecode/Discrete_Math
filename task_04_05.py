class Task_04_05:
    def __init__(self):
        self.mm=[] #массив, который хранит конъюнкции
        
    def tablize(self,k, truths=[]):
        if not k:
            str0=""
            for i in range(len(truths)):
                str0=str0+str(truths[i])
            self.mm.append(str0)
        else:
            for i in [0,1]:
                self.tablize(k-1, truths+[i])

    def tdnf_cout(self,table, p, t, n, m,td):
        s=0
        spp=0
        pp=[]##массив для запоминания не ядровых конъюнкций

        for i in range(t): pp.append(-1)

        #поиск ядровых и неядровых конъюнкций по таблице покрытий
        for i in range(t-1,-1,-1):
            if p[i]!=0:
                s=0
                for j in range(1<<n):
                    if table[i][j]==1:
                        s=0
                        for k in range(t-1,-1,-1):
                            if k!=i and p[k]!=0:
                                if table[k][j]==1:
                                    s=1
                                    break

                        if s==0:
                            break #если конъюнкция ядровая
                
                if s==1: #если конъюнкция не ядровая, ее можно убрать
                        pp[spp]=i
                        spp=spp+1 #количество не ядровых конъюнкций

        
        if spp>0:
            s=1
            for i in range(spp): #убираем неядровые конъюнкции и проверяем оставшуюся мини-таблицу на тндф
                p[pp[i]]=0
                self.tdnf_cout(table,p,t,n,m,td)
                p[pp[i]]=1
                
                
        str1=""
        if s==0:#все конъюнкции ядровые
            for i in range(t): #собираем тднф в строку
                if p[i]==1:
                    str1=str1+m[i]
                    
            l=0
            while ((str1!=td[l]) and (td[l]!="")):
                l=l+1

            td[l]=str1 #добавляем ее в массив тднф, если такой не было
          
    def main(self,data):
        data=data.split("\n")
        n,t=data[0].split(" ")
        n=int(n)
        t=int(t)

        if t==1: #сокращенная днф=тднф
            print(n,t)
            print(data[1])
            
        if t==0: #сокращенная днф=0
            print(n," 0")
            
        self.tablize(n)

        table=[] #двумерный массив для таблицы покрытий
        for i in range(t):
            tmp=[]
            for j in range(1<<n): tmp.append(0)
            table.append(tmp)

        data=data[1:]
        m=[] #массив для таблицы истинности
        for i in range(t): m.append("")
        for i in range(t): m[i]=data[i]

        for i in range(t): #заполняем таблицу покрытий
            for j in range(1<<n):
                a = 1
                for l in range(n):
                    if(m[i][l] == '*'):
                        continue
                    if(m[i][l] == self.mm[j][l]):
                        continue
                    else:
                        a = 0
                        break

                table[i][j] = a;

        p=[]
        td=[]
        for i in range(t): #создаем проверочный массив по конъюнкциям, которые не ядровые
            p.append(1)

        for i in range(t): #массив, который хранит тднф
            td.append("")

        self.tdnf_cout(table, p, t, n, m,td)
        
        ##отсортировка тднф лексикографически
        for i in range(t):
            for j in range(i,t):
                if len(td[i])<len(td[j]): #находим меньшую строку
                    a=len(td[i])
                else:
                    a=len(td[j])

                for l in range(a): #сравниваем посимвольно
                    if ( ((td[i][l] == '*') and (td[j][l] != '*')) or ((td[i][l] == '1') and (td[j][l] == '0')) ):
                        td[i],td[j]=td[j],td[i]

                    if ( ((td[i][l] == '0') and (td[j][l] != '0')) or ((td[i][l] == '1') and (td[j][l] == '*')) ):
                        break;		

        for i in range(t):
            if td[i]!="":
                print(n,int(float(len(td[i]))/n))
                for j in range(len(td[i])):
                    print(td[i][j],end="")
                    if((j + 1) % n == 0):
                        print()
       
f=open("in.txt","r",encoding="utf-8")
s=f.read()
f.close()

A=Task_04_05()
A.main(s)
