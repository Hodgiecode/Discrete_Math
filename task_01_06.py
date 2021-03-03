class Task_01_06:
    def main(self,n,vectznac):
        kol=1<<n
        ans=0
        vect=[]
        for i in range(kol):
            vect.append(int(vectznac[i]))
            
        count = 0;
        for i in range(kol):
            for j in range(i):
                if i&j==j:
                    vect[i]=vect[i]^vect[j]

            if vect[i]==1:
                count=count+1

        print(2,n,count)
        for i in range(kol):
            if vect[i]>0:
                for j in range(n-1,-1,-1):
                    print((i>>j)&1,end="")
                    
                print("",vect[i])
               
        return 0

n=3
vect="00000001"
A=Task_01_06()
A.main(n,vect)
