import json
import tatsu
import re

grammar='''@@grammar::CALC


start
    =
    expression $
    ;

expression
    =
    | expression
    | expression '+' ~ term
    | expression '-' ~ term
    | term
    ;

negation
    =
    '!' ~ factor
    ;

implication
    =
    term '>' ~ factor
    ;

xor
    =
    term '+' ~ factor
    ;

con
    =
    term '&' ~ factor
    ;

dis
    =
    term 'v' ~ factor
    ;

equiv
    =
    term '~' ~ factor
    ;

brackets
    =
   '(' ~ expression ')'
    ;


term
    =
    | con
    | dis
    | implication
    | equiv
    | nand
    | nor
    | xor
    | factor
    ;

nand
    =
    term '/' ~ factor
    ;

nor
    =
    term '|' ~ factor
    ;

factor
    =
    | brackets
    | negation
    | number
    | text
    ;


number
    =
    /\d+/
    ;

text =
	/[a-zA-Z0-9_]+/ ;
'''

class CalcSemantics(object):
    def brackets(self,ast):
        return ast

    def negation(self,ast):
        ast=list(ast)
        ast[0]="( not "
        ast[1]=list(ast[1])+[')']
        return ast

    def dis(self,ast):
        ast=list(ast)
        ast[1]="|"
        return ast

    def nand(self,ast):
        ast=list(ast)
        if type(ast[0])==str:
            ast[0]="not ("+ast[0]
            ast[-1]=ast[-1]+")"
        else:
            ast[0]=list(ast[0])
            ast[0]=["not ("]+ast[0]

            if type(ast[2])==str:
                ast[2]=ast[2]+")"
            else:
                ast[2]=ast[2]+[")"]

        ast[1]="or"
        return ast

    def nor(self,ast):
        ast=list(ast)
        if type(ast[0])==str:
            ast[0]="not ("+ast[0]
            ast[-1]=ast[-1]+")"
        else:
            ast[0]=list(ast[0])
            ast[0]=["not ("]+ast[0]

            if type(ast[2])==str:
                ast[2]=ast[2]+")"
            else:
                ast[2]=ast[2]+[")"]

        ast[1]="&"
        return ast

    def xor(self,ast):
        ast=list(ast)
        ast[1]="^"
        return ast

    def equiv(self,ast):
        ast[1]="=="
        return ast

    def implication(self,ast):
        ast=list(ast)
        if type(ast[0])==str:
            ast[0]="( not "+ast[0]+")"
        else:
            ast[0]=list(ast[0])
            ast[0]=["( not "]+ast[0]+[")"]

        ast[1]="|"
        return ast

def make_pass(l,tmp):
    for i,elem in enumerate(l):
        if not isinstance(elem,str):
            l[i]=list(l[i])
            elem=list(elem)
            l[i]=make_pass(elem,tmp)
        else:
            tmp.append(elem)

    return l

def additional_conversion(mystr):
    b=['|','+','&','>','/','|','!']

    a=re.split("([|+&()>/|!])",mystr.replace(" ",""))
    for k in range(len(a)-1,-1,-1):
        if a[k]=="":
            del a[k]

    for i in range(len(a)):
        if i>0 and a[i]=="!":
            if i<len(a)-1 and a[i-1] in b:
                if a[i+1]!="(":
                    a[i]="("+a[i]
                    a[i+1]=a[i+1]+")"
                else:
                    count=1
                    a[i]="("+a[i]
                    for k in range(i+2,len(a)):
                        if a[k]=="(":
                            count=count+1
                        if a[k]==")":
                            count=count-1
                        if count==0:
                            a[k]=a[k]+")"
                            break

    s="".join(a)
    return s


def main_converter(str1):
    a=additional_conversion(str1)
    parser = tatsu.compile(grammar)
    parser = tatsu.compile(grammar,asmodel=True)
    a=parser.parse(str1,semantics=CalcSemantics())
    tmp=[]
    make_pass(list(a),tmp)
    r=" ".join(tmp)

    return r

