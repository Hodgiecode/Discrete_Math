def combine(m, n):
    a = len(m)
    c = ''
    count = 0
    for i in range(a): 
        if(m[i] == n[i]):
            c += m[i]
        elif(m[i] != n[i]):
            c += '-'
            count += 1

    if(count > 1): 
        return None
    else:            
        return c


'''
не полноценный алгоритм. взят отсюда
https://coderoad.ru/7537125/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D0%9A%D1%83%D0%B0%D0%B9%D0%BD%D0%B0-McCluskey-%D0%B2-Python
'''
def find_prime_implicants(data):
    newList = list(data)
    size = len(newList)
    IM = []
    im = []
    im2 = []
    mark = [0]*size
    m = 0
    for i in range(size):
        for j in range(i+1, size):
            c = combine( str(newList[i]), str(newList[j]) )
            if c != None:
                im.append(str(c))
                mark[i] = 1
                mark[j] = 1
            else:
                continue

    mark2 = [0]*len(im)
    for p in range(len(im)):
        for n in range(p+1, len(im)):
            if( p != n and mark2[n] == 0):
                if( im[p] == im[n]):
                    mark2[n] = 1


    for r in range(len(im)):
        if(mark2[r] == 0):
            im2.append(im[r])

    for q in range(size):
        if( mark[q] == 0 ):
            IM.append( str(newList[q]) )
            m = m+1

    if(m == size or size == 1):
        return IM
    else:
        return IM + find_prime_implicants(im2)
