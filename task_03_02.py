class Task_03_02:
    def read_automata(self,data,n,temp):
        s=0
        translate=[]
        printl=[]
        for i in range(n): s=s|int(temp[i])<<(n-i-1)
        for i in range(n):
            temp=[]
            for k in range(2**(n+1)): temp.append(0)
            translate.append(temp)

        for i in range(n+1):
            tmp=data[i].split(" ")
            n1=int(tmp[0])
            n2=int(tmp[1])
            if i<n:
                for k in range(n1**n2):
                    translate[i][k]=int(tmp[2][k])
            else:
                for k in range(n1**n2):
                    printl.append(int(tmp[2][k]))

        return [n,s,translate,printl]
            
           
    def main(self,data):
        data=data.split('\n')
        if len(data[0].split(" "))==2:
            n1,temp=data[0].split(" ")
            n1=int(n1)
            m1=self.read_automata(data[1:n1+2],n1,temp)
        else:
            m1=[0,0,[0],[0,1]]

        if len(data[n1+2].split(" "))==2:
            n2,temp=data[n1+2].split(" ")
            n2=int(n2)
            m2=self.read_automata(data[n1+3:],n2,temp)
        else:
            m2=[0,0,[0],[0,1]]

        res=True
        queue=[]
        used=[]
        for i in range(10000):
            queue.append([0,0])
            used.append(False)

        queue[0][0]=m1[1]
        queue[0][1]=m2[1]
        used[(m1[1]<<m1[0])|m2[1]]=True
        left=0
        right=1

        while left<right:
            now1=queue[left][0]
            now2=queue[left][1]

            left=left+1
            new11=0
            new12=0
            new21=0
            new22=0
            G11=0
            G12=0
            G21=0
            G22=0
            for i in range(m1[0]):
                new11 = new11 | m1[2][i][(now1<<1)]<<(m1[0]-i-1)
                new12 = new12 | m1[2][i][(now1<<1)+1]<<(m1[0]-i-1)

            G11=m1[3][now1<<1]
            G12=m1[3][(now1<<1)+1]

            for i in range(m2[0]):
                new21 = new21 | m2[2][i][(now2<<1)]<<(m2[0]-i-1)
                new22 = new22 | m2[2][i][(now2<<1)+1]<<(m2[0]-i-1)

            G21=m2[3][now2<<1]
            G22=m2[3][(now2<<1)+1]

            if (G11!=G21 or G12!=G22):
                res=False
                break
            
            if not used[(new11<<m1[0])|new21]:
                used[(new11<<m1[0])|new21]=True
                queue[right][0]=new11
                queue[right][1]=new21
                right=right+1
                
            if not used[(new12<<m1[0])|new22]:
                used[(new12<<m1[0])|new22]=True
                queue[right][0]=new12
                queue[right][1]=new22
                right=right+1
                
            
        res=int(res)
        print(res)

f=open("in.txt","r",encoding="utf-8")
s=f.read()
f.close()

A=Task_03_02()
A.main(s)

