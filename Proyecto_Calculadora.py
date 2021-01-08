from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image 
import re 
import csv

ventana=Tk() 
ventana.title("Proyecto Calculadora") 
ventana.geometry("936x551") 
ventana.configure(background="Steelblue4") 
color_boton=("White") 
label=Label(text="Calculadora Lógica Proposicional", fg="black") 
label.place(x=80,y=50) 
listb=Listbox(ventana, width=46, height=18, font=('arial',17,'bold')) 
listb.place(x=330,y=40) 


def btnClik(num): 
    global operador
    operador=operador+str(num)
    input_text.set(operador) #VISUALIZAR LA OPERACION EN LA PANTALLA

def clear(): #limpiar el cuadro de texto
    global operador
    operador=("")
    input_text.set("")

def izquierda(): #Linea para movilizarnos un indice a la izquierda del cuadro de texto
    Salida.configure(state='normal')
    Salida.focus()
    Salida.icursor(0)

def derecha():
    Salida.configure(state="disabled")  

def e_logica():

    m=False
    cuadro=str(input_text.get()).strip()
    
    if cuadro==("p v q") or  cuadro==("(p v q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p v q.jpg')
        img.show()
        m=True
    elif cuadro==("p v r") or  cuadro==("(p v r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p v r.jpg')
        img.show()
        m=True
    elif cuadro==("p v s") or  cuadro==("(p v s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p v s.jpg')
        img.show()
        m=True
    elif cuadro==("q v p") or  cuadro==("(q v p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q v p.jpg')
        img.show()
        m=True
    elif cuadro==("q v r") or  cuadro==("(q v r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q v r.jpg')
        img.show()
        m=True
    elif cuadro==("q v s") or  cuadro==("(q v s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q v s.jpg')
        img.show()
        m=True
    elif cuadro==("r v p") or  cuadro==("(r v p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r v p.jpg')
        img.show()
        m=True
    elif cuadro==("r v q") or  cuadro==("(r v q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r v q.jpg')
        img.show()
        m=True
    elif cuadro==("r v s") or  cuadro==("(r v s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r v s.jpg')
        img.show()
        m=True
    elif cuadro==("s v p") or  cuadro==("(s v p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s v p.jpg')
        img.show()
        m=True
    elif cuadro==("s v q") or  cuadro==("(s v q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s v q.jpg')
        img.show()
        m=True
    elif cuadro==("s v r") or  cuadro==("(s v r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s v r.jpg')
        img.show()
        m=True
    elif cuadro==("p ^ q") or  cuadro==("(p ^ q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p ^ q.jpg')
        img.show()
        m=True
    elif cuadro==("p ^ r") or  cuadro==("(p ^ r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p ^ r.jpg')
        img.show()
        m=True
    elif cuadro==("p ^ s") or  cuadro==("(p ^ s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p ^ s.jpg')
        img.show()
        m=True
    elif cuadro==("q ^ p") or  cuadro==("(q ^ p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q ^ p.jpg')
        img.show()
        m=True
    elif cuadro==("q ^ r") or  cuadro==("(q ^ r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q ^ r.jpg')
        img.show()
        m=True
    elif cuadro==("q ^ s") or  cuadro==("(q ^ s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q ^ s.jpg')
        img.show()
        m=True
    elif cuadro==("r ^ p") or  cuadro==("(r ^ p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r ^ p.jpg')
        img.show()
        m=True
    elif cuadro==("r ^ q") or  cuadro==("(r ^ q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r ^ q.jpg')
        img.show()
        m=True
    elif cuadro==("r ^ s") or  cuadro==("(r ^ s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r ^ s.jpg')
        img.show()
        m=True
    elif cuadro==("s ^ p") or  cuadro==("(s ^ p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s ^ p.jpg')
        img.show()
        m=True
    elif cuadro==("s ^ q") or  cuadro==("(s ^ q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s ^ q.jpg')
        img.show()
        m=True
    elif cuadro==("s ^ r") or  cuadro==("(s ^ r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s ^ r.jpg')
        img.show()
        m=True
    elif cuadro==("p ! ^ q") or cuadro==("(p ! ^ q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n ^ q.jpg')
        img.show()
        m=True
    elif cuadro==("p ! ^ r") or cuadro==("(p ! ^ r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n ^ r.jpg')
        img.show()
        m=True
    elif cuadro==("p ! ^ s") or cuadro==("(p ! ^ s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n ^ s.jpg')
        img.show()
        m=True
    elif cuadro==("q ! ^ p") or cuadro==("(q ! ^ p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q n ^ p.jpg')
        img.show()
        m=True
    elif cuadro==("q ! ^ r") or cuadro==("(q ! ^ r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q n ^ r.jpg')
        img.show()
        m=True
    elif cuadro==("q ! ^ s") or cuadro==("(q ! ^ s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n ^ s.jpg')
        img.show()
        m=True
    elif cuadro==("r ! ^ p") or cuadro==("(r ! ^ p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r n ^ p.jpg')
        img.show()
        m=True
    elif cuadro==("r ! ^ q") or cuadro==("(r ! ^ q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r n ^ q.jpg')
        img.show()
        m=True
    elif cuadro==("r ! ^ s") or cuadro==("(r ! ^ s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r n ^ s.jpg')
        img.show()
        m=True
    elif cuadro==("s ! ^ p") or cuadro==("(s ! ^ p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s n ^ p.jpg')
        img.show()
        m=True
    elif cuadro==("s ! ^ q") or cuadro==("(s ! ^ q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s n ^ q.jpg')
        img.show()
        m=True
    elif cuadro==("s ! ^ r") or cuadro==("(s ! ^ r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s n ^ r.jpg')
        img.show()
        m=True
    elif cuadro==("p ! v q") or cuadro==("(p ! v q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n v q.jpg')
        img.show()
        m=True
    elif cuadro==("p ! v r") or cuadro==("(p ! v r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n v r.jpg')
        img.show()
        m=True
    elif cuadro==("p ! v s") or cuadro==("(p ! v s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\p n v s.jpg')
        img.show()
        m=True
    elif cuadro==("q ! v p") or cuadro==("(q ! v p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q n v p.jpg')
        img.show()
        m=True
    elif cuadro==("q ! v r") or cuadro==("(q ! v r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q n v r.jpg')
        img.show()
        m=True
    elif cuadro==("q ! v s") or cuadro==("(q ! v s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\q n v s.jpg')
        img.show()
        m=True
    elif cuadro==("r ! v p") or cuadro==("(r ! v p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r n v p.jpg')
        img.show()
        m=True
    elif cuadro==("r ! v q") or cuadro==("(r ! v q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r n v q.jpg')
        img.show()
        m=True
    elif cuadro==("r ! v s") or cuadro==("(r ! v s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\_r n v s.jpg')
        img.show()
        m=True
    elif cuadro==("s ! v p") or cuadro==("(s ! v p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s n v p.jpg')
        img.show()
        m=True
    elif cuadro==("s ! v q") or cuadro==("(s ! v q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s n v q.jpg')
        img.show()
        m=True
    elif cuadro==("s ! v r") or cuadro==("(s ! v r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\s n v r.jpg')
        img.show()
        m=True
    elif cuadro==("p") or cuadro==("(p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P.jpg')
        img.show()
        m=True
    elif cuadro==("! p") or cuadro==("(! p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\! P.jpg')
        img.show()
        m=True
    elif cuadro==("p ! + q") or cuadro==("(p ! + q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P--NXOR--Q.jpg')
        img.show()
        m=True
    elif cuadro==("p ! + r") or cuadro==("(p ! + r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P--NXOR--R.jpg')
        img.show()
        m=True
    elif cuadro==("p ! + s") or cuadro==("(p ! + s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P--NXOR--S.jpg')
        img.show()
        m=True
    elif cuadro==("p + q") or cuadro==("(p + q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P--XOR--Q.jpg')
        img.show()
        m=True
    elif cuadro==("p + r") or cuadro==("(p + r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P--XOR--R.jpg')
        img.show()
        m=True
    elif cuadro==("p + s") or cuadro==("(p + s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\P--XOR--S.jpg')
        img.show()
        m=True
    elif cuadro==("q") or cuadro==("(q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--BUFFER--Q.jpg')
        img.show()
        m=True
    elif cuadro==("! q") or cuadro==("(! q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--NOT--~Q.jpg')
        img.show()
        m=True
    elif cuadro==("q ! + p") or cuadro==("(q ! + p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--NXOR--P.jpg')
        img.show()
        m=True
    elif cuadro==("q ! + r") or cuadro==("(q ! + r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--NXOR--R.jpg')
        img.show()
        m=True
    elif cuadro==("q ! + s") or cuadro==("(q ! + s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--NXOR--S.jpg')
        img.show()
        m=True
    elif cuadro==("q + p") or cuadro==("(q + p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--XOR--P.jpg')
        img.show()
        m=True
    elif cuadro==("q + r") or cuadro==("(q + r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--XOR--R.jpg')
        img.show()
        m=True
    elif cuadro==("q + s") or cuadro==("(q + s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\Q--XOR--S.jpg')
        img.show()
        m=True
    elif cuadro==("r") or cuadro==("(r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--BUFFER--R.jpg')
        img.show()
        m=True
    elif cuadro==("! r") or cuadro==("(! r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--NOT--~R.jpg')
        img.show()
        m=True
    elif cuadro==("r ! + p") or cuadro==("(r ! + p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--NXOR--P.jpg')
        img.show()
        m=True
    elif cuadro==("r ! + q") or cuadro==("(r ! + q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--NXOR--Q.jpg')
        img.show()
        m=True
    elif cuadro==("r ! + s") or cuadro==("(r ! + s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--NXOR--S.jpg')
        img.show()
        m=True
    elif cuadro==("r + p") or cuadro==("(r + p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--XOR--P.jpg')
        img.show()
        m=True
    elif cuadro==("r + q") or cuadro==("(r + q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--XOR--Q.jpg')
        img.show()
        m=True
    elif cuadro==("r + s") or cuadro==("(r + s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\R--XOR--S.jpg')
        img.show()
        m=True
    elif cuadro==("s") or cuadro==("(s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--BUFFER--S.jpg')
        img.show()
        m=True
    elif cuadro==("! s") or cuadro==("(! s )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--NOT--~S.jpg')
        img.show()
        m=True
    elif cuadro==("s ! + p") or cuadro==("(s ! + p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--NXOR--P.jpg')
        img.show()
        m=True
    elif cuadro==("s ! + q") or cuadro==("(s ! + q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--NXOR--Q.jpg')
        img.show()
        m=True
    elif cuadro==("s ! + r") or cuadro==("(s ! + r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--NXOR--R.jpg')
        img.show()
        m=True
    elif cuadro==("s + p") or cuadro==("(s + p )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--XOR--P.jpg')
        img.show()
        m=True
    elif cuadro==("s + q") or cuadro==("(s + q )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--XOR--Q.jpg')
        img.show()
        m=True
    elif cuadro==("s + r") or cuadro==("(s + r )"):
        img = Image.open('C:\Proyecto Grupo 9\img\S--XOR--R.jpg')
        img.show()
        m=True

    if m!=True:
        showinfo(title="Lo sentimos", message="Lamentablemente no podemos mostrar los circuitos lógicos de expresiones complejas o expresiones inválidas. Para más información lea el manual de usuario.")
        

def operacion(): #Linea para resolver la operación que se encuentra en el cuadro de texto
    try:
        listb.delete(0,'end')
    
        class myStack:
            def __init__(self):
                self.stack = []
            def push(self, x):
                self.stack.append(x)
            def size(self):
                return len(self.stack)
            def empty(self):
                return self.size() == 0
            def top(self):
                return self.stack[-1]
            def pop(self):
                res = self.top()
                self.stack.pop()
                return res

        def Priority(c : str): 
            """return priority order of operator"""    """regresa la prioridad del orden de los operadores"""
            if (c == '('):
                return 0
            elif (c == '>' or c == '~'):
                return 1
            elif (c == 'v' or c == '^' or c=='+'):
                return 2
            else:
                assert(c == '!')
                return 3
        def Oper(x : int, y : int , oper : str): 
            """Calculate expression (x oper y), which 'oper' is in [v,^,<->, ->, +]"""
            """Calcula la expresión (x por y), cual 'oper' esta en [v,^,<->, ->, +]"""
            if (oper == 'v'):
                return (x | y) #x v y
            elif (oper == '^'):
                return (x & y) #x ^ y
            elif (oper == '>'):
                return ((1 ^ y) | x) #x -> y
            elif (oper == '+'):                         
                return (0 if (x==y)else 1) #x + y 
            else:
                assert(oper == '~')
                return (1 if (x == y) else 0) #x <-> y

        def preprocess(expression : str):  
            expression = re.sub(' ','', expression) #delete all the space
            #for easier programming, I convered all multi-char operators to one-char
            expression = re.sub('<->', '~', expression) 
            expression = re.sub('->', '>', expression)
            #- and ! both are represent for NOT operator
            expression = re.sub('-', '!', expression)  
            #+ and v both are represent for OR operator
            expression = re.sub('\-','v', expression)
            #. and ^ both are represent for AND operator
            expression = re.sub('\.', '^', expression)  
            #delete all !! operator
            while (re.search('!!',expression) != None):
                expression = re.sub('!!', '', expression)
            return expression

        def GetVariable(expression : str): 
            """Get all variables appeared in 'expression'"""
            """Obtiene todas las variables aparecidas en el parametro 'expression'"""
            SetVar = set()
            ListVar = []
            for c in expression:
                if ('a' <= c) and (c <= 'z') and (c != 'v'): #v is an operator
                    if (c in SetVar):
                        continue
                    SetVar.add(c)
                    ListVar.append(c)
            return ListVar

        def GetRPN(expression : str): 
            """Use shunting-yard algorithm to get Reverse Polish notation of 'expression' from Infix notation"""
            """Se usa el algoritmo de desviación para obtener la notación polaca inversa de 'expresión' de la notación Infix"""
            stack = myStack()
            RPN = myStack()
            for c in expression:
                if c == '(':
                    stack.push(c)
                elif c == ')':
                    while True:
                        x = stack.pop()
                        if (x != '('):
                            RPN.push(x)
                        else:
                            break
                elif c in ['v','^','>','~','!','+']:
                    while (not stack.empty()) and Priority(c) <= Priority(stack.top()):
                        RPN.push(stack.pop())
                    stack.push(c)
                elif (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))):
                    RPN.push(c)
            while (not stack.empty()): 
                RPN.push(stack.pop())
            return RPN

        def Calculate(RPN : myStack, VariableValue: dict):  
            """Calculate value of expression from RPN, with value of variable is stored in 'VariableValue'"""
            """Calcula el valor de la expresion des RPN, con el valor de la variable almacenada en 'VariableValue'"""
            res = myStack()
            for c in RPN.stack:
                if (c == '0' or c == '1' or (('a' <= c) and (c <= 'z') and (c != 'v'))): #'v' is an operator
                    res.push(VariableValue[c])
                elif (c == '!'):
                    res.push(1 ^ res.pop()) # not X, !X, -X
                else:
                    assert(c == '^' or c == 'v' or c == '>' or c == '~' or c=='+')
                    x = res.pop()
                    y = res.pop()
                    res.push(Oper(x, y, c))
            assert(res.size() == 1)
            return res.pop()

        """Funcion para imprimir el resultado en el Listbox"""
        """Function to print the result in the Listbox"""
        def WriteToListBox(result : list):
            renglones=iter(result)
            encabezado=next(renglones)
            tam=tuple(map(len,encabezado))
            listb.insert(0,' | '.join(encabezado))
        
            for renglon in renglones:
                listb.insert(1,' | '.join(str(b).center(tam[i])for i, b in enumerate(renglon)))

        def Solve(expression : str):
            result = []

            ListVariable = GetVariable(expression)
            ListVariable.append(expression)
            result.append(ListVariable.copy())
            ListVariable.pop()

            expression = preprocess(expression)
            RPN = GetRPN(expression)
            n = len(ListVariable)

            #brute force all value of all variables
            #Fuerza bruta de todos los valores de todas las variables
            for mask in range(2 ** n):
                VariableValue = {'0' : 0, '1' : 1}
                cur = []
                for i in range(n):
                    VariableValue[ListVariable[i]] = (mask >> (n - i - 1) & 1)
                    cur.append(mask >> (n - i - 1) & 1)
                cur.append(Calculate(RPN, VariableValue))
                result.append(cur)
            WriteToListBox(result)

        def main():
            expression = str(input_text.get())
            Solve(expression)

        if __name__ == '__main__': #Condicional para ejecutar el cógido #Conditional to execute the Code
            main()
    except:   #Si hay algún error, se mostrará en el ListBox 'Expresion no válida'.   If there is an error, it will show in the Listbox 'Invalid expression'
        listb.insert(0,'Expresión no válida')

ancho_boton=9 
alto_boton=2
input_text=StringVar()
text2=StringVar()
operador=""
clear()
            #Lineas para crear los botones de la interfaz gráfica
Button(ventana,text="AC",fg="red",bg=color_boton,width=20,height=alto_boton,command=lambda:clear()).place(x=17,y=180)
#Button(ventana,text="DEL",fg="red",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:delE()).place(x=94,y=180)
Button(ventana,text="=",fg="green",bg=color_boton,width=20,height=alto_boton,command=lambda:operacion()).place(x=170,y=180)
Button(ventana,text="p",fg="blue",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("p ")).place(x=17,y=225)
Button(ventana,text="q",fg="blue",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("q ")).place(x=94,y=225)
Button(ventana,text="r",fg="blue",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("r ")).place(x=170,y=225)
Button(ventana,text="s",fg="blue",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("s ")).place(x=247,y=225)
Button(ventana,text="!",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("! ")).place(x=17,y=270)
Button(ventana,text="^",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("^ ")).place(x=94,y=270)
Button(ventana,text="v",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("v ")).place(x=170,y=270)
Button(ventana,text="->",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("-> ")).place(x=247,y=270)
Button(ventana,text="<->",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("<-> ")).place(x=17,y=315)
Button(ventana,text="+",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("+ ")).place(x=94,y=315)
Button(ventana,text="(",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik("(")).place(x=170,y=315)
Button(ventana,text=")",fg="purple",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(")")).place(x=247,y=315)
Button(ventana,text="Habilitar Cuadro",fg="black",bg=color_boton,width=20,height=alto_boton,command=lambda:izquierda()).place(x=17,y=360)
Button(ventana,text="Desabilitar Cuadro",fg="black",bg=color_boton,width=20,height=alto_boton,command=lambda:derecha()).place(x=170,y=360)

Button(ventana,text="Tabla De Verdad",fg="red",bg=color_boton,width=20,height=alto_boton,command=lambda:btnClik("")).place(x=470,y=0)
Button(ventana,text="Expresión Lógica",fg="red",bg=color_boton,width=20,height=alto_boton,command=lambda:e_logica()).place(x=621,y=0)

#Linea para crear el cuadro de texto y colocarlo en el idice X y Y
Salida=Entry(ventana,font=('arial',20,'bold'),state="disabled",width=20,textvariable=input_text,justify="right")
Salida.place(x=17,y=120)
ventana.mainloop()