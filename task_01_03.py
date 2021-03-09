class Task_01_03:
    def main(self,data):
        k,n,vectznac=data.split(' ')
        n=int(n)
        kol=1<<n
        flag=0
        vect=[]
        count=0
        for i in range(kol): vect.append(vectznac[i])

        length = 1 << n
        for j in range(int(length / 2)):
            if (vect[j] == '0' and vect[length - 1 - j] == 1) or (vect[j] == '1' and vect[length - 1 - j] == '0'):
                count=count+1
                continue
            else:
                break

        if count == length / 2:
            flag = 1

        return flag
