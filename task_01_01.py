class Task_01_01:
    def main(self,data):
        k,n,vectznac=data.split(' ')
        n=int(n)
        kol=1<<n
        vect=[]
        for i in range(kol):
            vect.append(int(vectznac[i]))
            
        flag=1
        step=kol>>1
        while step>0 and flag==1:
            i=0
            while i<kol:
                for j in range(i,step+i):
                    if vect[j]>vect[j+step]:
                        flag=0
                        break

                i=i+2*step

            step=step>>1

        return flag

