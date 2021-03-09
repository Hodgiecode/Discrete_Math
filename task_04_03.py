class Task_04_03:
    def numOfDigInEk(self,ek):
        quantityOfDigInEk = 0
        for i in range(ek[3]):
            if ek[0][i]=='1' or ek[0][i]=='0':
                quantityOfDigInEk=quantityOfDigInEk+1

        ek[1]=quantityOfDigInEk
        return ek

    def sortnumofdigits(self,dnf):
        for i in range(len(dnf)):
            for j in range(len(dnf)):
                a=dnf[i][1]-dnf[j][1]
                if a<0:
                    dnf[i],dnf[j]=dnf[j],dnf[i]
        return dnf

    def absorption(self,n,m,dnf):
        for i in range(m-1):
           if dnf[i][2]==1:
               for j in range(i+1,m):
                   absorbEk=1
                   for k in range(n):
                       if dnf[i][0][k]=='*':
                           continue
                       if dnf[i][0][k]!=dnf[j][0][k]:
                           absorbEk=0
                           break

                   if absorbEk==1: dnf[j][2]=0

        return dnf

    def finalSort(self,n,m,dnf):
        quantityOfEkInMinimizedDNF=m
        for i in range(m):
            if dnf[i][2]==0:
                 dnf[i][1]=n+1
                 quantityOfEkInMinimizedDNF=quantityOfEkInMinimizedDNF-1

        return dnf,quantityOfEkInMinimizedDNF
        
            
    def main(self,data):
        data=data.split('\n')
        n,m=data[0].split(" ")
        n=int(n)
        m=int(m)
        dnf=[]
        data=data[1:]
       
        for i in range(m):
            ek=[]
            numOfDigits = 0
            usedInDNF = 1
            sizeOfEk = n

            for j in range(n): ek.append(data[i][j])
            dnf.append([ek,numOfDigits,usedInDNF,sizeOfEk])

            dnf[i]=self.numOfDigInEk(dnf[i])

        dnf=self.sortnumofdigits(dnf)
        dnf=self.absorption(n,m,dnf)

        dnf,quantityOfEkInMinimizedDNF=self.finalSort(n,m,dnf)

        s=""
        s=s+str(n)+" "+str(quantityOfEkInMinimizedDNF)+"\n"

        for i in range(quantityOfEkInMinimizedDNF):
            s=s+"".join(dnf[i][0])+"\n"

        return s
            


