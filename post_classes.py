def invert(vector):
    res=[]
    for i in range(len(vector)):
        if vector[i]==1:
            res.append(0)

        if vector[i]==0:
            res.append(1)

    return res
        
            
def post_classes_main(powerset,table_vector,zhegalkin_polynom,n):
    res=[]
    '''
    T0 - предполагаем, что он всегда первый из наборов
    '''
    if table_vector[0]==0:
        res.append("+")
    else:
        res.append("-")

    '''
    T1 - предполагаем, что он всегда последний из наборов
    '''
    if table_vector[len(table_vector)-1]==1:
         res.append("+")
    else:
        res.append("-")

    '''
    M
    '''
    flag=1
    step=(1<<n)>>1

    while (step>0 and flag==1):
        i=0
        while (i<(1<<n)):
            for j in range(i,step+i):
                if table_vector[j]>table_vector[j+step]:
                    flag=0
                    break

            i=i+2*step

        step=step>>1

    if flag==1:
         res.append("+")
    else:
        res.append("-")


    '''
    L
    '''
    flag=1
    if zhegalkin_polynom.count('*')>0 or zhegalkin_polynom.count('&')>0:
        flag=0

    if flag==1:
         res.append("+")
    else:
        res.append("-")
    
    '''
    S
    '''
    flag=1
    for i in range(int(0.5*len(powerset))):
        a=powerset[i]
        b=invert(powerset[i])
        for j in range(len(powerset)-1,int(0.5*len(powerset))-1,-1):
            if powerset[j]==b:
                if table_vector[i]==table_vector[j]:
                    flag=0
                    
                break

    if flag==1:
         res.append("+")
    else:
        res.append("-")

    return res

    
