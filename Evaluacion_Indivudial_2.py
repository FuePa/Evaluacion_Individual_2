import pandas as pd 
import datetime

archivo = pd.read_csv("ojito.csv")


    
def menu():
    x = input("""
    Que desea realizar hoy?
    1. Agregar Evento
    2. Quitar Evento
    3. Editar Evento
    4. Ver reportes
    5. Salir
    
    """)
    if x == "1":
        agg()
    if x == "2":
        rmv()
    if x == "3":
        edit()
    if x == "4":
        reports()
    if x == "5":
        print("Que tenga un buen dia!! \n")
        exit()
def agg():    
    # r = archivo.iat[0,1]
    # print(r)
    # fechasT = archivo("FECHA")
    r = archivo["FECHA"]
    fecha1 = input("Ingrese la fecha a agendar en formato MM/DD/AAAA \n")

    if fecha1 not in r:
        numsfecha = fecha1.split(sep="/")

        M = int(numsfecha[0])
        D = int(numsfecha[1])
        A = int(numsfecha[2])

           
        fecha2 = datetime.datetime(A,M,D)
        dia = fecha2.weekday()
        horaI = input("Ingrese a que hora iniciara en formato militar \n")
        horaF = input("Ingrese a que hora terminara en formato militar \n")
        actividad = input("Ingrese el nombre de la actividad \n")
        descripcion = input("Ingrese una breve descripcion de la actividad \n")
        archivo.concat({"FECHA":fecha1, "DIA":dia, "INICIO":horaI, "FIN":horaF, "NOMBRE":actividad, "DESCRIPCION":descripcion}, ignore_index = True)
        print("Felicidades se agrego tu actividad con exito! \n")

    else: 
        print("Estas ocupado ese dia, elige otro! \n")
        agg()
    

    menu()

def rmv():
    print()
def edit():
    print()
def reports():
    print()

menu()

