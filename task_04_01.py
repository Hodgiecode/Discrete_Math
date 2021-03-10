class Task_04_01:
    def flatten(self,l,a):
        for i in l:
            if isinstance(i,list):
                self.flatten(i,a)
            else:
                a.append(i)
        return a

    def sort(self,td):
        ##отсортировка тднф лексикографически
        for i in range(len(td)):
            for j in range(i,len(td)):
                if len(td[i])<len(td[j]): #находим меньшую строку
                    a=len(td[i])
                else:
                    a=len(td[j])

                for l in range(a): #сравниваем посимвольно
                    if ( ((td[i][l] == '*') and (td[j][l] != '*')) or ((td[i][l] == '1') and (td[j][l] == '0')) ):
                        td[i],td[j]=td[j],td[i]

                    if ( ((td[i][l] == '0') and (td[j][l] != '0')) or ((td[i][l] == '1') and (td[j][l] == '*')) ):
                        break

        return td
    
    def __init__(self):
        self.table=[]
       
    def check(self,a,b):
        diff=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                diff=diff+1
   
        if diff==1:
            s="" 
            for i in range(len(a)):
                if a[i]==b[i]:
                    s=s+str(a[i])
                else:
                    s=s+"*"
            return s
        else:
            return ""
        
    def tablize(self,n,truths=[]):
        if not n:
            self.table.append(truths)
        else:
            for i in [0,1]:
                self.tablize(n-1, truths+[i])
            
    def sort_by_group(self,n,terms,terms_index):
        tmp=[]
        index=[]
        for k in range(n):
            tmp.append([])
            index.append([])
        
        for i in range(len(terms)):
            count=0
            for j in range(len(terms[i])):
                if terms[i][j]=="1": count=count+1
        
            tmp[count-1].append(terms[i])
            index[count-1].append(terms_index[i])

        a,b=[],[]
    
        for i in range(len(tmp)):
            if tmp[i]!=[]:
                a.append(tmp[i])
                b.append(index[i])
        
        return a,b
       
    def return_implicants(self,stage,minterm,minterm_index):
        implicants,index_list,tmp=[],[],[]
    
        if stage==1:
           for i in range(len(minterm)):
                temp=[]
                for j in range(len(minterm[i])): temp.append(0)
                tmp.append(temp)
  
        for i in range(len(minterm)):
            for j in range(i+1,len(minterm)):
                a=minterm[i]
                b=minterm[j]
           
                for k1 in range(len(a)):
                    for k2 in range(len(b)):
                        s=self.check(a[k1],b[k2])
                        if s!="":
                            if stage==1:
                                tmp[i][k1]=1
                                tmp[j][k2]=1
                            
                            index_list.append([minterm_index[i][k1],minterm_index[j][k2]])
                            implicants.append(s)
                       
        if stage==1:
            for i in range(len(tmp)):
                for j in range(len(tmp[i])):
                    if tmp[i][j]==0: ##уникальный минтерм
                        implicants.append(minterm[i][j])
                        index_list.append([minterm_index[i][j]])            
               
        return implicants,index_list
            
    def main(self,data):
        k,n,vect=data.split(" ")
        k=int(k)
        n=int(n)
    
        self.tablize(n) #генерируем таблицу истинности
        minterm,index,implicants=[],[],[]

        for i in range(n): 
            minterm.append([])
            index.append([])
    
        for i in range(len(self.table)):
            if vect[i]=="1":
                count=0
                for j in range(len(self.table[i])):
                    if self.table[i][j]==1: count=count+1
                
                minterm[count-1].append(self.table[i])
                index[count-1].append(i)

        implicants,index=self.return_implicants(0,minterm,index)

        while True:
            implicants_save=implicants
            minterm_save=index
        
            implicants,index=self.sort_by_group(n,implicants,index) ##сортируем по количеству единиц
            implicants,index=self.return_implicants(1,implicants,index)

            if implicants==implicants_save: break #если не получили никаких изменений, то закончили

        implicants_uniq_list=[]
        index_uniq_list=[]
        
        for i in range(len(implicants)):
            if not implicants[i] in implicants_uniq_list: #выбираем уникальные импликанты
                implicants_uniq_list.append(implicants[i])
                index_uniq_list.append(index[i])

        for i in range(len(index_uniq_list)): #костыль, так как номера содержатся во вложенных списках упрощаем эти списки
            index_uniq_list[i]=self.flatten(index_uniq_list[i],[])

        for i in range(len(index_uniq_list)):
            counter=0
            for j in range(len(index_uniq_list[i])):
                for k1 in range(len(index_uniq_list)):
                    if i!=k1:
                        if index_uniq_list[i][j] in index_uniq_list[k1]:
                            counter=counter+1
                            break
                
            if counter==len(index_uniq_list):
                index_uniq_list[i]=[]
                implicants_uniq_list[i]=[]
            
        for i in range(len(implicants_uniq_list)-1,-1,-1):
            if implicants_uniq_list[i]==[]:
                del implicants_uniq_list[i]

        implicants_uniq_list=self.sort(implicants_uniq_list)
        s=""
        s=str(n)+" "+str(len(implicants_uniq_list))+"\n"
        for i in range(len(implicants_uniq_list)):
            s=s+implicants_uniq_list[i]+"\n"

        return s
   

