import re

'''
extraer_binaria
———————–
texto : string
final : string
————————
Verfica si texto coincide con la forma "x+algo" (puede ser +,*,-,/,otros), de ser así, se extrae "x+" y lo 
convierte en una expresion regular, luego verifica si "algo" es un elemento (numero, variable, otros) o una 
operacion binaria. En el primer caso la función retorna la coincidencia como una expresion regular, en el 
segundo caso, vuelve a llamar a la función hasta que se verifique todo. En ambos casos si lo que se está 
revisando no coincide con la forma solicitada retorna None
Final solo almacena lo que ya esta revisado, se usa más en un caso recursivo
'''
def extraer_binaria (texto, final):

    expresion1 = '\s*([1-9][0-9]*|(?:true|false)|#[A-Za-z0-9]*#|[A-Za-z][A-Za-z0-9]*)\s*([+]|[-]|[/]|[*]|[<]|==)\s*(.+)'
    expresion2 = '\s*([1-9][0-9]*|(?:true|false)|#[A-Za-z0-9]*#|[A-Za-z][A-Za-z0-9]*)\s*([+]|[-]|[/]|[*]|[<]|==)'
    elementos = '\s*([1-9][0-9]*|(?:true|false)|#[A-Za-z0-9]+#|[A-Za-z][A-Za-z0-9]*)'

    expresion1 = re.compile(expresion1)
    expresion2 = re.compile(expresion2)
    elementos = re.compile (elementos)

    final_aux = final
    linea_aux = ""

    if texto == None:
        return ""
    
    busqueda = re.search(expresion1, texto)
    if busqueda == None:
        return None
    busqueda = busqueda.span()
    resultante = texto[busqueda[0]:busqueda[1]]

    busqueda2 = re.search(expresion2,resultante)
    if busqueda2 == None:
        return None
    busqueda2 = busqueda2.span()

    final = final+texto[busqueda[0]:busqueda[0]+busqueda2[1]]

    signos = re.search('[+]|[*]|[/]',final)
    if signos != None:
        signos = signos.span()
        if final[signos[0]] == '+':
            signos = final.replace('+','\+')
        elif final[signos[0]] == '*':
            signos = final.replace('*','\*')
        elif final[signos[0]] == '/':
            signos = final.replace('/','\/')
    else:
        signos = final

    resto = texto[busqueda[0]+busqueda2[1]:]
    resto2 = re.match(expresion1,resto)
    if resto2 != None:
        return extraer_binaria(resto,final)
    else:
        busqueda3 = re.match(elementos,resto)
        if busqueda3 != None:
            busqueda3 = busqueda3.span()
            linea_aux = linea_aux + resto[0:busqueda3[1]]
            return signos + linea_aux
        else:
            return ""

'''
extarer_condicion
———————–
linea = string
linea2 = string
————————
Verfica si linea coincide con la forma x==algo (puede ser == o <) de ser así se extrae "x==" lo almacena en 
linea2, luego verfica si "algo" es un elemento o una condicion. En el primer caso retorna la coincidencia y en 
el segundo vuelve a llamar a la función hasta que verifique todo. En ambos casos si lo que se está revisando no 
coincide con la forma solicitada retorna None.
'''
def extraer_condicion(linea, linea2):

    forma = '\s*([1-9][0-9]*|(?:true|false)|[#][A-Za-z0-9]*[#]|[A-Za-z][A-Za-z0-9]*)\s*([<]|==)\s*(.+)'
    forma2 = '([1-9][0-9]*|(?:true|false)|[#][A-Za-z0-9]*[#]|[A-Za-z][A-Za-z0-9]*)\s*([<]|==)'
    elementos = '([1-9][0-9]*|(?:true|false)|[#][A-Za-z0-9]*[#]|[A-Za-z][A-Za-z0-9]*)'

    linea2_aux = linea2
    linea3 = ""

    if linea == None:
        return None 
    busqueda = re.search(forma, linea)
    if busqueda == None:
        return None 
    busqueda = busqueda.span()

    busqueda2 = re.search(forma2, linea[busqueda[0]:busqueda[1]])
    if busqueda2 == None:
        return None 
    busqueda2 = busqueda2.span()

    linea2 = linea2 + linea[busqueda[0]:busqueda[0]+busqueda2[1]]
    new_text = linea[busqueda[0]+busqueda2[1]:]

    resto = re.match(forma, new_text)
    if resto != None:
        return extraer_condicion(new_text, linea2)
    else:
        busqueda3 = re.search(elementos, new_text)
        if busqueda3 != None:
            busqueda3 = busqueda3.span()
            linea3 = linea3 + new_text[0:busqueda3[1]]
            return (linea2 + linea3)
        else:
            return 'd'

'''
ciclo
———————–
texto : string
————————
Verifica que texto cumpla con la forma entregada del EBNF, en caso de ser así se comienza a buscar que es lo que 
está dentro del while y que es lo que queda por revisar, por lo tanto se retrna una lista con estos resultados.
En caso que no cumpla con la forma, retorna none
'''        
def ciclo (texto):
    extraer_cond = extraer_condicion(texto,"").strip()
    expresion = '\s*while\s*\(\s*' + extraer_cond + '\s*\)\s*{\s*([\s\S]*)\s*}'
    expresion = re.compile(expresion)
    expresion_while = '\s*while\s*\(\s*' + extraer_cond + '\s*\)\s*{'
    expresion_while = re.compile (expresion_while)

    busqueda = re.search (expresion, texto)
    if busqueda == None:
        return None
    busqueda2 = re.match(expresion_while,texto)
    if busqueda2 == None:
        return None
    busqueda2 = busqueda2.span()

    resto = texto[busqueda2[1]:]

    balance = 1
    dentro_while = ""

    for i in range(len(resto)):
        if resto[i] == '{':
            balance += 1
        elif resto[i] == '}':
            balance -= 1
        if balance == 0:
            resto = resto[i+1:]
            break
        dentro_while += resto[i]

    return [extraer_cond, dentro_while, resto]

'''
condicionales
———————–
texto = string
————————
Al igual que la función anterior, se verifica que texto coincida con la forma entregada del EBNF, en caso de ser así
primero se busca lo que está dentro del if, luego lo que está dentro del else y lo que está fuera del condicional, 
finalmente se retorna una lista con estos valores.
En caso que no se cumpla la forma se retorna None
'''
def condicionales (texto):
    extraer_cond = extraer_condicion(texto,"").strip()
    expresion = 'if\s*\(\s*' + extraer_cond + '\s*\)\s*{\s*([\s\S]*)\s*}\s*else\s*{\s*([\s\S]*)\s*}'
    expresion_if = 'if\s*\(\s*' + extraer_cond + '\s*\)\s*{'
    expresion_restante = '}\s*else\s*{\s*([\s\S]*)\s*}'
    expresion_else = '}\s*else\s*{'

    expresion = re.compile(expresion)
    expresion_if = re.compile(expresion_if)
    expresion_restante = re.compile(expresion_restante)
    expresion_else = re.compile(expresion_else)

    busqueda = re.search(expresion, texto)
    if busqueda == None:
        return None
    
    busqueda2 = re.search(expresion_if, texto)
    busqueda2 = busqueda2.span()

    resto = texto[busqueda2[1]:]

    balance = 1
    dentro_if = ""

    for i in range(len(resto)):
        if resto[i] == '{':
            balance += 1
        elif resto[i] == '}':
            balance -= 1
        if balance == 0:
            resto = resto[i:]
            break
        dentro_if += resto[i]

    busqueda3 = re.search(expresion_restante,resto)
    if busqueda3 == None:
        return None
    busqueda3 = busqueda3.span()

    busqueda4 = re.search (expresion_else , resto)
    busqueda4 = busqueda4.span()
    resto = resto[busqueda4[1]:]

    balance = 1
    dentro_else = ""
    for i in range(len(resto)):
        if resto[i] == '{':
            balance += 1
        elif resto[i] == '}':
            balance -= 1
        if balance == 0:
            resto = resto[i+1:]
            break
        dentro_else += resto[i]

    return [extraer_cond, dentro_if, dentro_else, resto]

'''
extraer_main
———————–
texto = string
————————
Verifica que el texto entregado cumpla con la estructura de main, de ser así retorna lo que está dentro de esta, 
en caso contrario retorna none
'''
def extraer_main(texto):
    expresion = '\s*int\s*main\(\)\s*{([\s\S]*)return\s*0\s*;\s*}'
    expresion = re.compile(expresion)

    busqueda = re.match(expresion,texto)
    if busqueda == None:
        return None
    
    return busqueda.group(1)

'''
escribir_archivo
———————–
archivo = archivo de texto
texto = string
nivel = entero
————————
Modifica el texto resultante dependiendo de la configuración entregada, no retorna nada
'''
def escribir_archivo(archivo, texto, nivel):
    texto = re.sub("\s+"," "*cant_espacios,texto).strip()
    archivo.write("\t"*cant_tab*nivel + texto + "\n"*cant_saltos)
    return None

'''
check
———————–
texto : string
archivo : archivo de texto
tab : int
————————
Revisa que texto coincida con alguna expresion del EBNF, si coincide escribe en el texto lo que está correcto (con formato) 
y retorna la funcion con lo que queda por revisar para que se vuelva a ejecutar. En los casos como ciclos y condicionales, 
primero se vuelve a llamar la función para verificar lo que está dentro de los bloques y luego se retorna la función con lo 
que queda fuera del bloque. En caso que alguna expresión no coincida, el programa se termina de ejecutar.
'''
def check (texto,archivo,tab):
    if texto == None:
        return ""
    
    if extraer_binaria(texto,"") != None:
        expresion_igual = '\s*[A-Za-z][A-Za-z0-9]*\s*=\s*' + extraer_binaria(texto,"") + '\s*;'
        expresion_igual = re.compile(expresion_igual)
        match_igual = re.match(expresion_igual, texto)
    else:
        expresion_igual = '\s*[A-Za-z][A-Za-z0-9]*\s*=\s*@\s*;'
        expresion_igual = re.compile(expresion_igual)
        match_igual = re.match(expresion_igual, texto)

    if extraer_condicion(texto,"") != None:
        expresion_ciclo = '\s*while\s*\(\s*'+extraer_condicion(texto,"") +'\s*\)\s*{\s*([\s\S]*)\s*}'
        expresion_ciclo = re.compile(expresion_ciclo)
        match_ciclo = re.match(expresion_ciclo, texto)
    else:
        expresion_ciclo = '\s*while\s*\(\s*@\s*\)\s*{\s*([\s\S]*)\s*}'
        expresion_ciclo = re.compile(expresion_ciclo)
        match_ciclo = re.match(expresion_ciclo, texto)

    if extraer_condicion(texto,"") != None:
        expresion_condicion = '\s*if\s*\(\s*'+ extraer_condicion(texto,"") + '\s*\)\s*{\s*([\s\S]*)\s*}\s*else\s*{\s*([\s\S]*)\s*}'
        expresion_condicion = re.compile(expresion_condicion)
        match_condicion = re.match(expresion_condicion, texto)
    else:
        expresion_condicion = '\s*if\s*\(\s*@\s*\)\s*{\s*([\s\S]*)\s*}\s*else\s*{\s*([\s\S]*)\s*}'
        expresion_condicion = re.compile(expresion_condicion)
        match_condicion = re.match(expresion_condicion, texto)

    expresion_declaracion = '\s*(?:int|bool|str)\s*(?:[A-Za-z][A-Za-z0-9]*)\s*;'
    expresion_declaracion = re.compile(expresion_declaracion)
    match_declaracion = re.match(expresion_declaracion, texto)

    expresion_main = '\s*int\s*main\(\)\s*{([\s\S]*)return\s*0\s*;\s*}'
    expresion_main = re.compile(expresion_main)
    match_main = re.match(expresion_main, texto)

    if re.fullmatch('\s*', texto):
        return True

    elif match_igual != None:
        pos1 = match_igual.span()
        text1 = texto[pos1[0]:pos1[1]].strip()
        escribir_archivo (archivo,text1,tab)
        return check(texto[pos1[1]:],archivo,tab)
        
    elif match_declaracion != None:
        pos2 = match_declaracion.span()
        text2 = texto[pos2[0]:pos2[1]].strip()
        escribir_archivo(archivo, text2, tab)
        return check(texto[pos2[1]:],archivo,tab)

    elif match_ciclo != None:
        x1 = ciclo(texto)
        if x1 == None:
            return None
        
        condicion, dentro_while, resto = x1
        escribir_archivo(archivo, "while (" + condicion + ") {" ,tab)
        y = check (dentro_while,archivo,tab+1)
        if y == None:
            return None
        escribir_archivo(archivo,"}",tab)
        return check(resto, archivo, tab)
    
    elif match_condicion != None:
        x2 = condicionales(texto)
        if x2 == None: 
            return None
        
        condicion, dentro_if, dentro_else, resto = x2
        escribir_archivo(archivo, "if ("+ condicion + ") {" , tab)

        y = check(dentro_if,archivo,tab+1)
        if y == None:
            return None
        escribir_archivo(archivo, "} else {", tab)

        z = check(dentro_else,archivo,tab+1)
        if z == None:
            return None
        escribir_archivo(archivo, "}" , tab)

        return check(resto,archivo,tab)
    
    elif match_main != None:
        x3 = extraer_main(texto)
        if x3 == None:
            return None
        escribir_archivo(archivo, "int main () {",tab)

        y= check(x3,archivo,tab+1)
        if y == None:
            return None
        escribir_archivo (archivo, "return 0;" , tab+1)
        escribir_archivo (archivo, "}", tab)
        return True
    
    else: 
        return None


archivo_configuracion = open("config.txt","r")
archivo_codigo = open("codigo.txt","r")
archivo_formateado = open("formateado.txt","w")

datos = archivo_configuracion.readline()
datos = datos.split(" ")
cant_espacios = int(datos[0])
cant_saltos = int(datos[1])
cant_tab = int(datos[2])
archivo_configuracion.close()

info = ""
for line in archivo_codigo:
    x = line.split('\n')
    info = info + x[0]

# se agrega un espacio a los lados del caracter 
info = re.sub(r'([(){};+-/<*]|==)', r' \1 ', info)
info = re.sub(r'\s+', ' ', info)
info = re.sub(r"\s*int\s*main\s*\(\s*\)\s*{", "int main() {", info)

check(info,archivo_formateado,0)
archivo_formateado.close()
archivo_codigo.close()