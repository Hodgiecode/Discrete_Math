import re

def sknf(f,table,var_list,n):
    res="( "
    s=""
    for i in range(n):
        if f[i]==0:
            for k in range(len(table[i])):
                if k<len(table[i])-1:
                    s=" v "
                else:
                    s=" ) & "

                if table[i][k]==0:
                    res=res+var_list[k]+s
                else:
                    res=res+"!"+var_list[k]+s

            res=res+"( "

    res=res[:-4]
    return res

def sdnf(f,table,var_list,n):
    res="( "
    s=""
    for i in range(n):
        if f[i]==1:
            for k in range(len(table[i])):
                if k<len(table[i])-1:
                    s=" & "
                else:
                    s=" ) v "

                if table[i][k]==1:
                    res=res+var_list[k]+s
                else:
                    res=res+"!"+var_list[k]+s

            res=res+"( "

    res=res[:-4]
    return res



def zhegalkin(f,table,variable_list,n):
    temp=[]
    triangle=[]
    diagonal=[]
    k=n-1
    res=""

    for j in range(n):
        diagonal.append(0)

    for i in range(n):
        temp=[]
        for j in range(n):
            temp.append(0)

        triangle.append(temp)

    for i in range(n):
        triangle[0][i]=f[i]

    for i in range(1,n):
        for j in range(k):
            triangle[i][j]=triangle[i-1][j]^triangle[i-1][j+1]

        k=k-1

    for i in range(n):
        diagonal[i]=triangle[i][0]

    for i in range(n):
        if diagonal[i]==1:
            mode=0
            for k in range(len(table[i])):
                if table[i][k]==1:
                    res=res+variable_list[k]+"&"
                    mode=1

            if mode==0:
                res=res+"1"

            if res[-1]=="&":
                res=res[:-1]+"+"
            else:
                res=res+"+"

    res=res[:-1]
    return res

def generateAllBinaryStrings(n):
   bools=[]
   for i in range(2**n):
       temp=[]
       for j in range(n):
           temp.append(0)

       bools.append(temp)

   for i in range(len(bools)):
        for j in range(len(bools[i])):
            val=(1 & (len(bools)*j+i >> j))
            bools[i][j]=int(val!=0)

   bools.sort()
   return bools
