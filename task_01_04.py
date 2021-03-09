class Task_01_04:
    def t0(self,fst):
        if fst==0:
            return 1
        return 0

    def t1(self,pos):
        if pos==1:
            return 1
        return 0

    def selfdual(self,kol,vect):
        for i in range(kol>>1):
            if vect[i]==vect[kol-i-1]:
                return 0

        return 1
    
    def main(self):
        k,n,vectznac=data.split(' ')
        n=int(n)
        kol=1<<n
        ans=0
        vect=[]
        for i in range(kol):
            vect.append(int(vectznac[i]))
            
        ans=ans+self.t0(vect[0])
        ans=ans+self.t1(vect[kol-1])
        ans=ans+self.selfdual(kol,vect)

        if ans>0:
            ans=0
        else:
            ans=1

        return ans

