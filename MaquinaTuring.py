import csv
def ejemplo(a,b,c):
    return [c,b,a]

def buscarTabla(tabla,caracter,estadoActual):
    a=0
    b=0
    for i in range(len(tabla[0])):
        if(caracter==tabla[0][i]):
            a=i
    for i in range(len(tabla)):
        if(estadoActual==tabla[i][0]):
            b=i
    return tabla[b][a].split(",")

def EjecucionAutomata(cadena,tabla,estadoInicial,estadosFinales):
    estadoActual=estadoInicial
    cabezal=0
    while((not estadoActual in estadosFinales) and (not estadoActual=="e")):
        [estadoActual,escribir,movimiento]=buscarTabla(tabla,cadena[cabezal],estadoActual)
        ##Acciones de mi cinta
        cadena=cadena[:cabezal]+escribir+cadena[cabezal+1:]
        if movimiento=="R":
            cabezal+=1
        else: 
            if (movimiento=="L"):
                cabezal-=1
        if(cabezal<0):
            cadena="#"+cadena
            cabezal+=1
        if(cabezal>len(cadena)-1):
            cadena+="#"
        
    if (estadoActual in estadosFinales):
        print("Cadena Aceptada") 
        print("Resultado "+cadena.replace("#",""))
        
    else:
        print("Cadena Inválida")
        
def cargarMaquina(direccion):
    estadoInicial=None
    estadosFinales=[]
    tabla=[]
    with open(direccion, newline='') as File:  
        reader = csv.reader(File)
        i = 0
        for row in reader:
            if (i==0):
                estadoInicial=row[0]
            elif (i==1):
                for elemento in row:
                    if(not elemento == ''):
                        estadosFinales.append(elemento)
            else:
                filaTabla=[]
                for elemento in row:
                    if(not elemento == ''):
                        elemento=elemento.replace(";", ",")
                        filaTabla.append(elemento)
                tabla.append(filaTabla)
                        
            i+=1
    return tabla,estadoInicial,estadosFinales

tabla=[["e", "0", "1", "#"],
       ["q1","q1,1,R","q1,0,R","q2,#,L"],
       ["q2","e,#,#","e,#,L"]]
                
