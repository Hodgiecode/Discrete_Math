class Task_01_07:
    def main(self,data):
        data=data.split()
        k=int(data[0])
        n=int(data[1])
        vectznac=data[2]
        cnt=100
        kol=1<<n
        vect=[]
        for i in range(len(vectznac)):
            vect.append(int(vectznac[i]))

        all_=[]
        add_=[]
        for i in range(cnt):
            tmp=[]
            for j in range(k):
                tmp.append(0)
                
            all_.append(tmp)
            add_.append(tmp)

        temp=[]
        for i in range(k):
            temp.append(0)
            
        cnt=0
        is_=1
        for i in range(k):
            if i!=vect[i*k+i]: is_=0

        if is_==1:
            cnt=1
            for i in range(k): all_[0][i]=i
        else:
            cnt=2
            for i in range(k):
                all_[0][i]=i
                all_[1][i]=vect[i*k+i]

        l=0
        r=0
        while True:
            for i in range(cnt):
                for j in range(cnt):
                    addcan=1
                    for i1 in range(k):
                        temp[i1]=vect[all_[i][i1]*k+all_[j][i1]]

                    for i1 in range(cnt):
                        isok=1
                        if addcan!=1:
                            break
                        for i2 in range(k):
                            if temp[i2]!=all_[i1][i2]:
                                isok=0

                        if isok: addcan=0


                    for i1 in range(1,r):
                        isok=1
                        if addcan!=1:
                            break
                        for i2 in range(k):
                            if temp[i2]!=add_[i1][i2]:
                                isok=0

                        if isok: addcan=0


                    if addcan:
                        for j in range(k):
                            add_[r][j]=temp[j]

                        r=r+1

            if l==r:
                break
            else:
                for i in range(1,r):
                    for j in range(k):
                        all_[cnt][j]=add_[i][j]
                    cnt=cnt+1

                r=r+1
                l=r

        for i in range(cnt):
            for j in range(i+1,cnt):
                shouldswap=0
                for i1 in range(k):
                    if all_[i][i1]<all_[j][i1]:
                        break
                    else:
                        if all_[i][i1]>all_[j][i1]:
                            shouldswap=1
                            break

                if shouldswap:
                    for i1 in range(k):
                        all_[i][i1],all_[j][i1]=all_[j][i1],all_[i][i1]


        temp=[]
        res=[]
        s=""
        for i in range(cnt):
            s=""
            for j in range(k):
                s=s+str(all_[i][j])

            temp.append(s)

        for i in range(len(temp)):
            if not temp[i] in res:
                res.append(temp[i])

        s=""
        for i in range(len(res)):
            s=s+str(k)+" "+str(1)+" "+str(res[i])+"\n"

        return s

