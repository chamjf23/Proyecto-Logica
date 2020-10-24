class letrasss(object):
    def __init__(self, letra,numero, fila, columna):
        self.l=letra
        self.n=numero
        self.f=fila
        self.c=columna
    def __str__(self):
        return "{0},{1},{2}".format(self.n,self.f,self.c)

    def mismolugar2 (self,l): #Regla 3 no puede haber mas de un numero en la misma casilla
        o=""
        e=0
        for p in l:
            if self.f==p.f and self.c==p.c:
               if self.n==p.n:
                    t=str(self.l)
               else:
                    if e==19:
                        o += str(p.l)
                    else:                     
                        o += str(p.l)+"O"
                        e+=1
        d=t+"=-"+o
        return d
   
    def columnayfila(self,l): # Regla2 No puede haber el mismo numero en la misma columna o fila
        o=""
        t=""
        e=0
        for i in l:
            if self.f==i.f and self.c==i.c:
                t=str(self.l)
            elif self.f==i.f or self.c==i.c:
                if e==0:    
                    o+=(str(i.l)+"-")
                    e+=1
                else:
                    o+=str(i.l)+"-"+"Y"
            else:
                if e==0:    
                    o+=str(i.l)
                    e+=1
                else:
                    o+=str(i.l)+"O"
        d=t+"="+o
        return d
    
    def columnayfila2(self,l): #regla 3
        o=""
        t=""
        e=0
        for i in l:
            if self.f==i.f and self.c==i.c:
                t="("+str(self.l)+")"
            elif self.f==i.f or self.c==i.c:
                if e==0:    
                    o+="-("+str(i.l)+")"
                    e+=1
                else:
                    o+="Y-("+str(i.l)+")"
            else:
                if e==0:    
                    o+="("+str(i.l)+")"
                    e+=1
                else:
                    o+="O("+str(i.l)+")"
        d=t+"=("+o+")"
        return d
    
def sumas(n): #Regla 1 las sumas de las filas y columnas nos dan como resultado el numero n dado por el usuario
    lista = []
    for i in range (n+1):
        for j in range (n+1):
            if n-i-j>=0:
                lista.append((i,j,n-i-j))
    regla1=""
    regla2=""
    for tupla in lista:
        inicial= True
        Nfilas = 3
        Ncolumnas = 3
        Nnumeros = 57
        for i in range (3):
            inicial= True
            formula1 = ""
            for j in range (3):
                if inicial:
                    formula1 = P(i,j,tupla[j],Nfilas,Ncolumnas,Nnumeros)
                    inicial= False
                else:
                    formula1+= P(i,j,tupla[j],Nfilas,Ncolumnas,Nnumeros) + "Y"
            if inicial:
                regla1=formula1
                inicial2 = False
            else:
                regla1+=formula1+"Y"
    for tupla in lista:
        inicial= True
        Nfilas = 3
        Ncolumnas = 3
        Nnumeros = 57
        for i in range (3):
            inicial= True
            formula1 = ""
            for j in range (3):
                if inicial:
                    formula1 = P(j,i,tupla[j],Nfilas,Ncolumnas,Nnumeros)
                    inicial= False
                else:
                    formula1+= P(j,i,tupla[j],Nfilas,Ncolumnas,Nnumeros) + "Y"
            if inicial:
                regla1=formula1
                inicial2 = False
            else:
                regla1+=formula1+"Y"
        
    regla_final=regla1+regla2
    return regla_final

def suma_c_f(n):
    return polacainversa(suma_filas(n)+suma_columna(n))


def polaca_arbol(f):
    F = String2Tree(f)
    letrasProposicionales=[chr(x) for x in range(256, 600)]
    conectivosBinarios=["O", "Y", ">", "="]
    negacion = ["-"]
    if F.l in letrasProposicionales:
         return F.l
    elif F.l in negacion:
        return "-"+polaca_arbol(f.right)
    elif F.l in conectivosBinarios:
        return F.l+polaca_arbol(F.left)+polaca_arbol(F.right)
    
def polacainversa(f):
    return polaca_arbol(f)[::-1]

class Tree(object):
    def __init__(self, label, left, right):
        self.left = left
        self.right = right
        self.label = label
        
def String2Tree(A):
    letrasProposicionales=[chr(x) for x in range(256, 600)]
    Conectivos = ['O','Y','>','=']
    Pila = []
    for c in A:
        if c in letrasProposicionales:
            Pila.append(Tree(c,None,None))
        elif c=='-':
            FormulaAux = Tree(c,None,Pila[-1])
            del Pila[-1]
            Pila.append(FormulaAux)
        elif c in Conectivos:
            FormulaAux = Tree(c,Pila[-1],Pila[-2])
            del Pila[-1]
            del Pila[-1]
            Pila.append(FormulaAux)
        else:
            print(u"Hay un problema: el símbolo " + str(c)+ " no se reconoce")
    return Pila[-1]

def Inorderp(f):
    if f.right == None:
        return str(Pinv(f.label, Nfilas, Ncolumnas, Nnumeros))
    elif f.label == '-':
        return f.label + Inorderp(f.right)
    else:
        return "(" + Inorderp(f.left) + f.label + Inorderp(f.right) + ")"
    
def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)
    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla
    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)
    f = int(n / Nc)
    c = n % Nc
    return f, c
def P(f, c, o, Nf, Nc, No):
    # Funcion que codifica tres argumentos
    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf - 1) + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1) + "\nSe recibio " + str(c)
    assert((o >= 0) and (o <= No - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    v1 = codifica(f, c, Nf, Nc)
    v2 = codifica(v1, o, Nf * Nc, No)
    codigo = chr(256 + v2)
    return codigo
def Pinv(codigo, Nf, Nc, No):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    x = ord(codigo) - 256
    v1, o = decodifica(x, Nf * Nc, No)
    f, c = decodifica(v1, Nf, Nc)
    return f, c, o
Nfilas = 3
Ncolumnas = 3
print(u"Números correspondientes a la codificación:")
print("\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        print(v1, end = " ")
    print("")
for v1 in range(9):
    f, c = decodifica(v1, Nfilas, Ncolumnas)
    print('Código: '+str(v1)+', Fila: '+str(f)+', Columna: '+str(c))
letras = []
print("\n\nfilas x columnas")
for i in range(Nfilas):
    for j in range(Ncolumnas):
        v1 = codifica(i, j, Nfilas, Ncolumnas)
        cod = chr(v1 + 256)
        print(cod, end = " ")
        letras.append(cod)
    print("")
for cod in letras:
    print('Letra = '+cod, end=', ')
    f, c = decodifica(ord(cod)-256, Nfilas, Ncolumnas)
    print('Fila = '+str(f), end=', ')
    print('Columna = '+str(c))

letras = []
Nnumeros = 21
for k in range(Nnumeros):
    print("Numero: "+str(k))
    print("filas x columnas")
    for i in range(Nfilas):
        for j in range(Ncolumnas):
            cod = P(i, j, k, Nfilas, Ncolumnas, Nnumeros)
            print(cod, end = " ")
            letras.append(cod)
        print("")
    print('\n')
a=[]
for cod in letras:
    f, c, o = Pinv(cod, Nfilas, Ncolumnas, Nnumeros)
    cod=letrasss(cod,o,f,c)
    a.append(cod)
    

# for i in a:
#     q=i
#     b=i.mismolugar2(a)
#     c=i.columnayfila2(a)
#     p=i.sumas(3)
    #f=i.sumas3(A,B,C,D,E,F,G,H,J,10)
    #print (f)
    #print (b)
    #print (p)
X=suma_c_f(3) 
print(X)

    



