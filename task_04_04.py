class Task_04_04:
    def edge(self,table, d, f, res,res_size, m, n2, n):
        for i in range(m):
            for j in range(n2):
                for g in range(n):
                    if ((table[i][n - g - 1] == '1') and (j & (1 << g))):
                        d[j]=d[j]+1

                    if ((table[i][n - g - 1] == '0') and (not (j & (1 << g)))):
                        d[j]=d[j]+1

                for j in range(n2):
                    if int(d[j]/f[i]):
                        res[j][res_size[j]]=i
                        res_size[j]=res_size[j]+1

                    d[j]=0


    def main(self,data):
       data=data.split('\n')
       n,m=data[0].split(" ")
       n=int(n)
       m=int(m)
       table=[]
       f=[]
       for i in range(m):f.append(0)
       
       for i in range(m):
           temp=[]
           for j in range(n): temp.append("")
           table.append(temp)

       for i in range(1,m+1):
           for j in range(len(data[i])):
               table[i-1][j]=data[i][j]
               if table[i-1][j]=='1' or table[i-1][j]=='0':
                   f[i-1]=f[i-1]+1

       n2=1<<n
       d=[]
       res=[]
       res_size=[]
       for i in range(n2):
           d.append(0)
           res_size.append(0)
           temp=[]
           for j in range(n*n): temp.append(0)
           res.append(temp)

       self.edge(table, d, f, res,res_size,m,n2,n)
       
       count=0
       for i in range(n2):
           if res_size[i]==1:
               if d[res[i][0]]==0:
                   count=count+1
               d[res[i][0]]=d[res[i][0]]+1

       s=""
       s=s+str(count)+"\n"
       for i in range(m):
            if d[i]:
                for j in range(n):
                    s=s+str(table[i][j])

                s=s+"\n"
       return s
      


