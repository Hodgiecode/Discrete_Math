class Task_01_02:
    def main(self,data):
        k,n,vectznac=data.split(' ')
        n=int(n)
        kol=1<<n
        flag=1
        vect=[]
        for i in range(kol): vect.append(int(vectznac[i]))

        trijeg=[]

        tmp = kol+1
        for i in range(kol):
            tmp = tmp - 1
            temp_list=[]
            temp_list.append(vect[i])
            for j in range(1,tmp):
               temp_list.append(0)

            trijeg.append(temp_list)

        tmp=kol
        for i in range(1,kol):
            tmp=tmp-1
            for j in range(tmp): trijeg[j][i]=(trijeg[j][i-1]+trijeg[j+1][i-1]) % 2

        i=kol
        while i!=0:
            i=int(i/2)
            trijeg[0][i]=0

        for i in range(kol):
            if trijeg[0][i]==1:
                flag=0
                break

        return flag
