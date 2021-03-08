from converter import main_converter
from tasklogic import *
from post_classes import *
from minim import *

import re

'''
возвращает строку: набор - значение на наборе
'''
def printer(powerset,table_vector):
    s=""
    for i in range(len(powerset)):
        for j in range(len(powerset[i])):
            s=s+str(powerset[i][j])+" "

        s=s+"| "+str(table_vector[i])+"\n"

    return s

def create_vectors(task,a,n):
    powerset=generateAllBinaryStrings(n) #генерируем все наборы для n переменных
    table_vector=[]

    for i in range(len(powerset)):
        my_dict = {}
        for k in range(len(powerset[i])):
            my_dict[a[k]]=bool(powerset[i][k])

        table_vector.append(int(eval(task,my_dict))) #использование eval - плохая идея

    return powerset,table_vector ##вернули наборы и значения

def extract_var(task):
    a=re.findall('[_a-z][_a-z0-9]*', task, re.I) # ищем переменные.
    c=[]
    for i in range(len(a)): #среди переменных могут встретится not,or, and - исключаем их из числа переменных
        if a[i]!="not" and a[i]!="or" and a[i]!="and" and not a[i] in c:
            c.append(a[i])

    n=len(c)
    return c,n



def main_post(powerset,table_vector,s2,n):
    s5=""
    a=['T0','T1','M','L','S']
    s=post_classes_main(powerset,table_vector,s2,n)

    for i in range(len(s)):
        s5=s5+a[i]+":"+s[i]+"\n"

    return s5


def sub_block(task):
    mode=0 #0 - работаем непосредственно с вектором значением функции, 1 - иначе его предварительно найдем
    for i in range(len(task)):
        if task[i]!="0" and task[i]!="1":
            mode=1
            break

    if mode==0:
        a=2
        r=2
        n=1
        k=len(task)

        while (r!=k and r<k):
            r=r*2
            n=n+1

        table_vector=[]
        var_list=[]
        powerset=generateAllBinaryStrings(n)

        for i in range(len(task)):
            table_vector.append(int(task[i]))

        for i in range(n):
            var_list.append("x_"+str(i+1))

    if mode==1:
        b=main_converter(task)#адаптируем входные данные
        var_list,n=extract_var(b)
        powerset,table_vector=create_vectors(b,var_list,n) #получаем все наборы и значения функции на этих наборах

    s1=printer(powerset,table_vector) #получаем строку с наборами и значениями функций для печати
    s2=zhegalkin(table_vector,powerset,var_list,2**n) #построили полином Жегалкина
    s3=sknf(table_vector,powerset,var_list,2**n) #по таблице истинности построили КНФ
    s4=sdnf(table_vector,powerset,var_list,2**n) #по таблице истинности построили ДНФ
    s5=main_post(powerset,table_vector,s2,n)
    #s6=try_to_minim(powerset,table_vector,var_list)
    return [s1,s2,s3,s4,s5]


def basic():
    s1="& (*) - конъюнкция\nv - дизъюнкция\n! - отрицание ставиться перед переменной или выражением\n+ (^) - xor,сложение по модулю 2\n"
    s2=" | - Штрих Шеффера\n> - импликация\n/ - Стрелка Пирса\n~ - эквивалентность"
    a=['&','v','^','|','>','/','~']
    s=""

    powerset=generateAllBinaryStrings(2)

    s=" ".join([" "," "," "]+a)+"\n"

    for i in range(len(powerset)):
        x1=bool(powerset[i][0])
        x2=bool(powerset[i][1])
        s=s+str(powerset[i][0])+" "+str(powerset[i][1])+" | "
        for i in range(len(a)):
            if a[i]=="|":
                s=s+str(int(eval("not ( "+str(x1)+" & "+str(x2)+" )")))+" "
            elif a[i]==">":
                s=s+str(int(eval("not ( "+str(x1)+") or "+str(x2))))+" "
            elif a[i]=="~":
                s=s+str(int(eval(str(x1)+"=="+str(x2))))+" "
            elif a[i]=="v":
                s=s+str(int(eval(str(x1)+"|"+str(x2))))+" "
            elif a[i]=="/":
                s=s+str(int(eval("not ("+str(x1)+"|"+str(x2)+")")))+" "
            else:
                s=s+str(int(eval(str(x1)+a[i]+str(x2))))+" "

        s=s+"\n"

    return s

def helpf():
    print('Приоритет операций выбирает пользователь при помощи скобок')
    print('Баги: значок дизъюнкции v надо отделять пробелами с обеих сторон\nЗнаки конъюнкции нужно ставить.')

#str1="!x+(!u&!z)"
#a=sub_block(str1)
#print(a)
#print(basic())
