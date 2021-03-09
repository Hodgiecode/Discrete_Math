class Task_01_06:
    def main(self,data):
        data=data.split(" ")
        n=int(data[1])
        vectznac=data[2]
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

        s=""
        s="2 "+str(n)+" "+str(count)+"\n"
        for i in range(kol):
            if vect[i]>0:
                for j in range(n-1,-1,-1):
                    s=s+str(((i>>j)&1))
                    
                s=s+" "+str(vect[i])+"\n"

        return s
