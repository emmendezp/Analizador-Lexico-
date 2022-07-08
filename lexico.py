import re
import sys

row = 1
salida = [0, 0]

reservadas = {'proceso':'proceso',
              'caracter':'caracter',
              'numerico':'numerico',
              'numero':'numero',
              'texto':'texto',
              'cadena':'cadena',
              'verdadero':'verdadero',
              'falso':'falso',
              'hasta':'hasta',
              'dimension':'dimension',
              'inproceso':'inproceso',
              'definir':'definir',
              'como':'como',
              'segun':'segun',
              'no':'token_neg',
              'mod':'token_mod',
              'de':'de',
              'otro':'otro',
              'modo':'modo',
              'subalgoritmo':'subalgoritmo',
              'logico':'logico',
              'entero':'entero',
              'real':'real', 
              'caracter':'caracter',
              'si':'si',
              'entonces':'entonces',
              'sino':'sino',
              'para':'para',
              'con':'con',
              'paso':'paso',
              'hacer':'hacer',
              'mientras':'mientras',
              'funcion':'funcion',
              'finproceso':'finproceso',
              'finsegun':'finsegun',
              'finsubproceso':'finsubproceso',
              'finsubalgoritmo':'finsubalgoritmo',
              'finfuncion':'finfuncion',
              'hasta':'hasta',
              'algoritmo':'algoritmo',
              'que':'que',
              'limpiar':'limpiar',
              'borrar':'borrar',
              'pantalla':'pantalla',
              'esperar':'esperar',
              'tecla':'tecla',
              'segundos':'segundos',
              'milisegundos':'milisegundos',        
              'rc':'raiz',
              'sen':'sen',
              'cos':'cos',
              'tan':'tan',
              'asen':'asen',
              'acos':'acos',
              'atan':'atan',
              'aleatorio':'aleatorio',
              'longitud':'longitud',
              'mayusculas':'mayusculas',
              'minusculas':'minusculas',
              'subcadena':'subcadena',   
              'concatenar':'concatenar',
              'convertiranumero':'convertianumero',
              'convertiratexto':'convertiratexto',
              'finsi':'finsi',
              'finpara':'finpara',
              'finmientras':'finmientras',
              'subproceso':'subproceso',
              'repetir':'repetir',
              'escribir':'escribir',
              'leer':'leer',
              'dimension':'dimension',
              'algoritmo':'algoritmo',
              'finalgoritmo':'finalgoritmo',
              'abs' : 'abs',
              'exp' : 'exp',
              'otro':'otro',
              'o':'token_o',
              'y':'token_y',
              'fin':'fin',
              'ln':'ln'}


def delta(column, char, state):
    global lex
    global line
    if state == 0:
        #cadenas no especificas => string
        if re.match(r'["\']',char) :
            lex = ""
            return [5, 0]
        # operadores especiales
        #parentesis
        
        elif char == ')':
            print("<token_par_der," + str(row) + "," + str(column) + ">")
            return [0, 0]
        
        #corchetes 
        elif char == '[':
            print("<token_cor_izq," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == ']':
            print("<token_cor_der," + str(row) + "," + str(column) + ">")
            return [0, 0]
        #operacion
        elif char == '+':
            print("<token_mas," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '-':
            print("<token_menos," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '*':
            print("<token_mul," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '%':
            print("<token_mod," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == ';':
            print("<token_pyc," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == ':':
            print("<token_dosp," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == ',':
            print("<token_coma," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '^':
            print("<token_pot," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '~':
            print("<token_neg," + str(row) + "," + str(column) + ">")
            return [0, 0]
        elif char == '$':         
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
            exit(0)
        elif char == '!':         
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
            exit(0)
        elif char == '&':
            print("<token_y," + str(row) + "," + str(column) + ">")
            return [0, 0] 
        elif char == '=':
            print("<token_igual," + str(row) + "," + str(column) + ">")
            return [0, 0] 
        elif char == '|':
            print("<token_o," + str(row) + "," + str(column) + ">")
            return [0, 0] 
        elif char == '.':
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
            exit(0) 
        elif char == 'á' or char == 'é' or char == 'í' or char == 'ó' or char == 'ú'or char == 'ñ' or  char == 'Á' or char == 'É' or char == 'Í' or char == 'Ó' or char == 'Ú' or char == 'Ñ'or char == '@'or char == '¡':
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
        
            exit(0)
        elif char == '?' or char == '¿':
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
            exit(0) 
        elif char == '>':
            return [1, 0]
        elif char == '<':
            return [2, 0]
        elif char == '/':
            return [3, 0]
        elif char == '(':
            return [4, 0]
       
        #palabras reservadas
        elif re.match(r'[a-z,_]', char) or re.match(r'[A-Z,_]', char):
            lex=char.lower()
            return [6, 0]
        #cadenas no especificas => int, float
        elif re.match(r'[0-9]', char):
            lex = char
            return [7, 0]
        else:
            return [0, 0]

    if state == 1:
        if char == '=':
            print("<token_mayor_igual," + str(row) + "," + str(column-1) + ">")
            return [0, 0]
        else:
            print("<token_mayor," + str(row) + "," + str(column-1) + ">")
            state = 0
            return [0, 1]

    if state == 2:
        if char == '=':
            print("<token_menor_igual," + str(row) + "," + str(column - 1) + ">")
            return [0,0]
        elif char == '-':
            print("<token_asig,"+ str(row) + "," + str(column - 1) + ">")
            return [0,0]
        elif char == '>':
            print("<token_dif,"+ str(row) + "," + str(column - 1) + ">")
            return [0,0]

        else:
            print("<token_menor," + str(row) + "," + str(column - 1) + ">")
            return [0,1]
    if state == 3:
        if char == '/':
            line = ""
            return [0, 0]
        else:
            print("<token_div," + str(row) + "," + str(column-1) + ">")
            state = 0
            return [0, 1]
    if state == 4:
        if char == '"' or char == '\'':
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
            exit(0)
        else:
            print("<token_par_izq," + str(row) + "," + str(column-1) + ">")
            state = 0
            return [0, 1]
    if state == 5:
        if char=='"':
            print("<token_cadena," + lex + "," + str(row) + "," + str(column-len(lex)-1) + ">")
            return[0, 0]
        elif char == "'":
            print("<token_cadena," + lex + "," + str(row) + "," + str(column-len(lex)-1) + ">")
            return[0, 0]
        else:
            lex = lex + char
            return [5, 0]

    if state == 6:
        if re.match(r'[a-z_]', char) or re.match(r'[A-Z_]', char) or re.match(r'[0-9]', char):
            lex = lex + str.lower(char)
            return[6, 0]
        else:
            if lex in reservadas:
                print("<"+reservadas[lex]+ "," + str(row) + "," + str(column - len(lex)) + ">")     
                
            else:
                print("<id," + lex + "," + str(row) + "," + str(column - len(lex)) + ">")
            return [0, 1]

    if state == 7:
        if re.match(r'[0-9]', char):
            lex = lex + char
            return [7, 0]
        elif char == '.':
            lex = lex + char
            return [8, 0]
        elif re.match(r'[a-z_@]', char) or re.match(r'[A-Z_@]', char):
            print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(column) + ")")
            exit(0)
        else:
            print("<token_entero," + lex + "," + str(row) + "," + str(column - len(lex)) + ">")
            return [0, 1]

    if state == 8:
        if re.match(r'[0-9]', char):
            lex = lex + char
            return[9, 0]
        else:
            print("<token_entero," + lex[0:len(lex)-1] + "," + str(row) + "," + str(column - len(lex)) + ">")
            return[0, 2]

    if state == 9:
        if re.match(r'[0-9]', char):
            lex = lex + char
            return[9, 0]
        else:
            print("<token_real," + lex + "," + str(row) + "," + str(column - len(lex)) + ">")
            return [0, 1]


lines = sys.stdin.readlines() 
print

for line in lines:
    i = 0
    line = line+" "

    while i < len(line):
        salida = delta(i+1, line[i], salida[0])
        i = i + 1 - salida[1]
    if salida[0] == 5:
        print(">>> Error lexico (linea: " + str(row) + ", posicion: " + str(i -len(lex)) + ")")
        exit(0)
        
    row += 1