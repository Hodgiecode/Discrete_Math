class Task_02_02:
    def __init__(self):
        self.k=0
        self.n=0
        self.vals=[]
        self.sets=[]
        self.var_sets=[]
        self.result=[]
        self.answer=[]

    def sort(self):
        length=self.result[0][0]
        for i in range(1,length):
            for j in range(i,length):
                if self.result[i][self.k-1]>self.result[j][self.k-1]:
                    self.result[i],self.result[j]=self.result[j],self.result[i]

        s=""
        
        for i in range(1,length):
            l=self.result[i][self.k-1]
            for j in range(l):
                s=s+str(self.result[i][j])

            self.answer.append(s)
            s="" 
                
    def keeping_sets(self):
        a=1<<self.k
        for i in range(a):
            temp=[]
            for j in range(self.k): temp.append(0) 
            self.sets.append(temp)
            
        self.get_all_set(a)

        b=k**self.n
        for i in range(b):
            temp=[]
            for j in range(self.n): temp.append(0) 
            self.var_sets.append(temp)
        
        self.var_set()

        for i in range(1<<k):
            temp=[]
            for j in range(self.k-1): temp.append(0)
            self.result.append(temp)

        f=1
        for i in range(1,a-1):
            if self.check_keeping_set(self.sets[i],self.sets[i][self.k-1])==1:
                self.result[f]=self.sets[i]
                f=f+1

        self.result[0][0]=f
        self.sort()
      

    def check_keeping_set(self,set_,l):
        a=self.k**self.n
        g=0
        for i in range(a):
            f=0
            for j in range(self.n):
                for h in range(l):
                    if self.var_sets[i][j]==set_[h]:
                        f=f+1

            if f==self.n:
                for h in range(l):
                    if int(self.vals[i])==set_[h]:
                           g=g+1
                           break

        if g==l**n:
            return 1
        return 0
    

    def get_all_set(self,a):
        for i in range(a-1):
            f=0
            for j in range(self.k):
                if self.getbit(i,j)==1:
                    self.sets[i][f]=j
                    f=f+1
                  
            self.sets[i][k-1]=f

    def var_set(self):
        a=self.k**self.n
        var_set=[]
        for i in range(self.n): var_set.append(0)
        
        for i in range(a):
            for j in range(self.n): self.var_sets[i][j]=var_set[j]

            var_set[self.n-1]=var_set[self.n-1]+1
            if var_set[self.n-1]==self.k:
                var_set[self.n-1]=0
                f=self.n-2
                while var_set[f]==self.k-1:
                    var_set[f]=0
                    f=f-1
                var_set[f]=var_set[f]+1

        
    def getbit(self,i,j):
        if (i & (1<<j)):
            return 1
        else:
            return 0

    def main(self,k,n,vals):
        self.k=k
        self.n=n
        a=self.k**self.n

        for i in range(a): self.vals.append(vals[i])
        
        self.keeping_sets()
        return self.answer

k=3
n=2
vals="000000000"
A=Task_02_02()
r=A.main(k,n,vals)
print(r)
