class Task_03_01:
    def conversion(self,fi,n,m,state,cur): #функция перехода, для которой state - состояние, cur - текущее значение на входе
        state<<=1
        state=state|cur

        q=0
        for i in range(n):
            q=q*2
            q|=fi[i*m+state]

        return q

    def leave_f(self,psi,state,cur): return psi[cur|(state<<1)] #функция выхода, для которой state - состояние, cur - текущее значение на входе

    #рекурсивная функция проверяющая 2 состояния state 1 и state2 на эквивалентность (len - длина текущего эксперимента, maxlen - максимальная длина эксперимента)
    def check_if_equal(self,fi,psi,k,n,m,state1,state2,length,maxlength):
        if length>maxlength: return 1

        if self.leave_f(psi,state1,0)!=self.leave_f(psi,state2,0): return 0
        if self.leave_f(psi,state1,1)!=self.leave_f(psi,state2,1): return 0

        cur_state1=self.conversion(fi,n,m,state1,0)
        cur_state2=self.conversion(fi,n,m,state2,0)

        res=1
        if cur_state1!=cur_state2: res=self.check_if_equal(fi,psi,k,n,m,cur_state1,cur_state2,length+1,maxlength)
         
        if res==1:
            cur_state1=self.conversion(fi,n,m,state1,1)
            cur_state2=self.conversion(fi,n,m,state2,1)

            if cur_state1==cur_state2:  return 1

            res=self.check_if_equal(fi,psi,k,n,m,cur_state1,cur_state2,length+1,maxlength)

        return res
        
    def read(self,data):
        data=data.split('\n')
        n,n1=data[0].split()
        
        n=int(n)
        n1=int(n1)
        k=1<<n
        m=2*k
    
        fi=[]
        psi=[]
    
        for j in range(m*n): fi.append(0)
        for j in range(m): psi.append(0)

        for i in range(1,n+1):
            temp=data[i].split()
            n1=int(temp[0])
            n2=int(temp[1])
            for j in range(n1**n2):
                fi[(i-1)*m+j]=int(temp[2][j])

        n1,n2,data=data[n+1:][0].split()
        num=int(n1)**int(n2)

        for i in range(num): psi[i]=int(data[i])

        return fi,psi,k,n,m

        '''
		Теорема Мура.
		Если в автомате (А, B, Q, фи, пси) состояния qi и qj отличимы, то существует слово,
		отличающее qi и qj, длины l <= |Q| - 1
		
		A = B = {0, 1}
		|Q| = 2^n - множество всех состояний
	'''

    def main(self,data):
        fi,psi,k,n,m=self.read(data)
        length=k-1 # len - макс длина слов, которую необходимо проверить 
        for i in range(length):
            for j in range(i+1,k): # попарно сравниваем состояния, при этом всегда i<j
                if self.check_if_equal(fi,psi,k,n,m,i,j,1,length)==1: #рекурс ф-я, перебирающая все слова длины от 1 до len
                    for g in range(n-1,-1,-1):
                        if i & (1<<g):
                            print(1,end="") #напечатает меньшее из проверяемых эквив состояний
                        else:
                            print(0,end="")
                    print(" ",end="")
                    
                    for g in range(n-1,-1,-1): #напечатает большее из проверяемых эквив состояний
                        if j & (1<<g):
                            print(1,end="")
                        else:
                            print(0,end="")
                    print(" ",end="")
        

s='2 00\n2 3 10101010\n2 3 11010101\n2 3 01011010'
A=Task_03_01()
A.main(s)
