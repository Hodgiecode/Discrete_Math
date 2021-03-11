class Task_03_03:
    def __init__(self):
        self.A=[]
        self.B=[]

    def read_automata(self,data,n,m):
        D=[]
        for i in range(n+2):
            if i==0:
                temp=[]
                for j in range(n+1):
                    temp.append(0)
                D.append(0)
            else:
                temp=[]
                for j in range((1<<m)-1):
                    temp.append(0)

                D.append(temp)

        tmp=data[0].split()[1]
        D[0]=[n]
        for i in range(len(tmp)):
            D[0].append(int(tmp[i]))
       
        data=data[1:]
        for i in range(len(data)): data[i]=data[i].split()

        for i in range(1,n+2):
            m1=int(data[i-1][0])
            m2=int(data[i-1][1])
            D[i]=[m1]
            for k in range(len(data[i-1][2])):
                D[i].append(int(data[i-1][2][k]))

        return D
        

    def superposition(self):
        n=self.A[0][0]
        nn=self.B[0][0]
        rn=n+nn
        C=[]
    
        for i in range(rn+2):
            if i==0:
                temp=[]
                for j in range(rn+1): temp.append(0)
                C.append(0)
            else:
                temp=[]
                for j in range((1<<(rn+1))+1): temp.append(0)
                C.append(temp)

        C[0]=[rn]
        for i in range(1,n+1): C[0].append(self.A[0][i])

        for i in range(n+1,rn+1):C[0].append(self.B[0][i-n])

        for i in range(1,rn+2): C[i][0]=rn+1

        k=1
        for i in range(1,(1<<(n+1))+1,2):
            for j in range(1,(1<<(nn+1))+1,2):
                C[rn+1][k]=self.B[nn+1][j+self.A[n+1][i]]
                C[rn+1][k+1]=self.B[nn+1][j+self.A[n+1][i+1]]
                k=k+2

        
        ###функция переходов автомата C
        for ij in range(1,n+1):
            for j in range(1,(1<<(rn+1))+1):
                xt=(j-1)&1
                qt=(j-1)&(1<<(rn-ij+1))
                if qt!=0:qt=1
                l=qt*(1<<(n-ij+1))+xt

                C[ij][j]=self.A[ij][l+1]

        for ij in range(n+1,rn+1):
            for j in range(1,(1<<(rn+1))+1):
                xt=(j-1)&1
                l=0
                for ii in range(1,n+1):
                    qt=(j-1)&(1<<(rn-ii+1))
                    if qt!=0:qt=1
                    l=l+qt*(1<<(n-ii+1))

                l=l+xt
                xt=self.A[n+1][l+1]
                qt=(j-1)&(1<<(rn-ij+1))
                if qt!=0: qt=1
                l=qt*(1<<(nn-ij+1+n))+xt
                C[ij][j]=self.B[ij-n][l+1]

        s=""
        if C!=[]:
            for i in range(len(C)):
                for j in range(len(C[i])):
                    C[i][j]=str(C[i][j])
                    
            s=C[0][0]+" "+C[0][1]+C[0][2]+"\n"
            for i in range(1,len(C)):
                s=s+"2 "+C[i][0]+" "+"".join(C[i][1:])+"\n"

        return s
       
        
        
    def read(self):
        self.data=self.data.split('\n')
        n,m=self.data[0].split()
        n=int(n)
        m=int(m)
        self.A=self.read_automata(self.data[:n+2],n,m)

        n,m=self.data[n+2].split()
        n=int(n)
        m=int(m)
        self.B=self.read_automata(self.data[n+2:],n,m)
        
    def main(self,data):
        self.data=data
        self.read()
        s=self.superposition()
        return s


