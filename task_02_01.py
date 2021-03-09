class Task_02_01:
    def main(self,data):
        data=data.split(" ")
        t=0
        k=data[0]
        k=int(k)
        n=data[1]
        n=int(n)

        vect=[]
        length=k**n
        for i in range(length): vect.append(data[2][i])

        while(length>0):
            length=length/k
            for i in range(int(length)):
                if int(vect[i])>int(vect[i+int(length)]):
                    t=1
                    break

            if t==1: rtn=0
            if length==1: rtn=1

        return rtn


