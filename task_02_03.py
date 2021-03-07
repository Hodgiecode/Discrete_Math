class Task_02_03:
    def main(self,data):
        s="0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ"
        s_l=[]
        for i in range(len(s)): s_l.append(s[i])

        data=data.split('\n')
        k,n,m=data[0].split(" ")
        k=int(k)
        n=int(n)
        m=int(m)

        koef=[] #массив для коэффицентов размерностью m, т.е. у каждого слагаемого есть свой коэффициент
        power=[] # одномерный массив для степеней переменных, m на n.
        #Каждое слагаемое состоит из умножения n переменных и у каждой переменной есть степень.
	#на степень j-й переменной i-го слагаемого можем обратиться как power[i*n + j]*/

        for i in range(m*n): power.append(0)

        data=data[1:]
        for i in range(m):
            tmp=data[i].split(" ")
            for j in range(n):
                power[i*n+j]=int(tmp[0][j])
            for j in range(len(tmp[1])):
                koef.append(int(tmp[1][j]))
        '''
        По условию надо найти одноэлементные множества, которые данный полином сохраняет.
	одноэлементными множествами являются множества вида: {0}, {1}, ..., {k - 1}
	если при подставлении 0 в ф-цию f(x1, x2, ..., xn) ответ получится 0, то f(x1,...,xn) сохраняет 0
	f(x,x,...,x) = x, сохраняет {x}
	f(x1,x2, ...,xn) - данный полином
	'''
        for i in range(k): # для каждого мн. {0}, {1}, ..., {k - 1}
            summ=0
            for j in range(m):
                ch=koef[j] #от 0 до m - кол. слаг., не включительно
                for ij in range(n):
                    ch=ch*(i**power[j*n+ij]) #подставляем i (где i=0,m) вычисляем соответствующую степень, умножаем на ch
                summ=summ+ch%k #вычисляем сумму слагаемых, но от слагаемых берем остаток от деления на k т.к. у нас k-значная логика

            if summ%k==i: #если остаток от деления суммы на k == i (т.е. f(i,i,...i) == i
                print(s_l[i]) # выводим i-й символ из алфавита (если i = 0,9 => sym[i] = 0,9; если i = 10,... => sym[i] = A,B,C...)
       


f=open("in.txt","r",encoding="utf-8")
s=f.read()
f.close()

A=Task_02_03()
A.main(s)
