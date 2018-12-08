from Cuenta import*
from Cliente import*
from Cuenta_de_ahorro import*
from Cuenta_de_credito import*
import sys
import matplotlib.pyplot as plt

class Banco:
    def __init__(self):
        self.cliente=None
        self.clientes=[]
        self.boolean=False #Este valor de tipo booleano nos servirá para asegurar a la consola de que efectivamente estamos agregando más cuentas al cliente
        self.cuentas_credito=[] 
        self.cuentas_ahorro=[]
    
    def menu_inicio(self):
      print("----------Banco Regional----------","\n")
      print("Elija la opción correspondite: ","\n")
      opcion=input("1.-Crear un cliente"+"\n2.-Elegir un cliente"+"\n3.-Salir"+"\n")
      while opcion!="1" and opcion!="2" and opcion!="3":
          opcion=input("Opción incorrecta, vuelva a ingresar alguna de las opciones mostradas en el menú"+"\n")
      if opcion=="1":
        self.agregar_cliente()
      if opcion=="2":
        self.menu_cliente()
      if opcion=="3":
        print("Gracias por su visita")
        if len(self.clientes)!=0: #En el caso de que haya clientes registrados, se creará un archivo donde aparecerán los datos de los clientes junto con un par de graficas que analizan sus edades y sus cuentas bancarias respectivamente
            self.guardar_registros()
            print("\nSe han guardado/actualizado los registros de los clientes")
            print("\nSe muestra la grafica de edades de los clientes\n")
            self.get_total_cuentas()
            self.grafica_edades()
            self.grafica_cuentas()
        sys.exit()
     
    def agregar_cliente(self):  
        
      print("-------------------NUEVO UN CLIENTE-------------------\n","\n")
      nombre=input("Nombre del cliente: ")
      edad=input("Edad: ")
      direccion=input("Dirección: ")
      print("\n-------------------Cuentas del cliente-------------------\n")
      tipo=input("Tipo de cuenta (Elija la opción de acuerdo al numero)"+"\n1.-Ahorro"+"\n2.-Credito"+"\n")
      cuentas=[]
      if tipo=="1":
          valor=input("Cantidad de la cuenta: ")
          interes=input("Tasa de interés: ")
          cuenta=Cuenta_ahorro(valor,interes)
          self.cuentas_ahorro.append(cuenta)
          self.cliente=Cliente(nombre,direccion,edad,cuentas)
          self.cliente.agregar_cuenta(cuenta)
          self.clientes.append(self.cliente)
      elif tipo=="2":
          valor=input("Cantidad de la cuenta: ")
          sobregiro=input("Cantidad de sobregiro: ")
          cuenta=Cuenta_credito(valor,sobregiro)
          self.cuentas_credito.append(cuenta)
          self.cliente=Cliente(nombre,direccion,edad,cuentas)
          self.cliente.agregar_cuenta(cuenta)
          self.clientes.append(self.cliente)
      else:
          print("Tipo de cuenta no disponible") 
      
      if len(cuentas)>0:  
        print("\nCLIENTE REGISTRADO\n")
        ver_datos=input("¿Mostrar los datos del cliente?\n"+"Si, oprima 's'\n"+"No, oprima 'n'\n")
        while ver_datos.lower()!="s" and ver_datos.lower()!="n":
            print("\nOpción incorrecta\n")
            ver_datos=input("¿Mostrar los datos del cliente?\n"+"Si, oprima 's'\n"+"No, oprima 'n'\n")
        if ver_datos.lower()=="s":
          print("\nDatos del cliente: ")
          print(self.cliente)
        if ver_datos.lower()=="n" or ver_datos.lower()=="s":
          agregar_mas_cuentas=input("¿Se agregaran más cuentas al cliente?\n"+"Si, oprima 's'\n"+"No, oprima 'n'\n")
          self.agregar_cuenta(agregar_mas_cuentas)                
          if agregar_mas_cuentas.lower()=="n":
              self.menu_inicio()     
      else:
          print("El cliente no fué registrado")
          
    def agregar_cuenta(self,add):
        while add.lower()=="s":
              tipo=input("Tipo de cuenta (Elija la opción de acuerdo al numero)"+"\n1.-Ahorro"+"\n2.-Credito"+"\n")
              cuentas=[]
              if tipo=="1":
                valor=input("Cantidad de la cuenta: ")
                interes=input("Tasa de interés: ")
                cuenta=Cuenta_ahorro(valor,interes)
                self.cuentas_ahorro.append(cuenta)
                self.cliente.agregar_cuenta(cuenta)
              elif tipo=="2":
                valor=input("Cantidad de la cuenta: ")
                sobregiro=input("Cantidad de sobregiro: ")
                cuenta=Cuenta_credito(valor,sobregiro)
                self.cuentas_credito.append(cuenta)
                self.cliente.agregar_cuenta(cuenta)
              else:
                print("Tipo de cuenta no disponible") 
              add=input("¿Se agregaran más cuentas al cliente?\n"+"Si, oprima 's'\n"+"No, oprima 'n'\n")
        if self.boolean==False:
          self.menu_inicio()
        else:
          self.boolean=False  
          self.menu_cliente()
            
                     
    def menu_cliente(self):
        #En el caso de que haya clientes en el banco va a aparecer un menú correspondiente para hacer cada una de las modificaciones
        if len(self.clientes)!=0:
            print("------------------------------------MENÚ DE LOS CLIENTES------------------------------------")
            print("\n\nClientes registrados en el banco: ","\n")
            cadena=""
            for i in range(len(self.clientes)):
              cadena="Cliente "+str(i+1)+"\n"+"\n"
              cadena+="Nombre del cliente: "+self.clientes[i].nombre+"\n"
              cadena+="Número de cuentas: "+str(len(self.clientes[i].cuenta))+"\n"
              print(cadena)  
            print("El número de cliente se muestra en la parte superior","\n")
            accede_cliente=input("\nElija alguna de las siguientes opciones: "+"\n\nPresione el número que corresponde al cliente para administrar sus cuentas\n"
            +"Presione '0' para volver al menú principal\n\n")
            for i in range(len(self.clientes)):                
             
#Mediante este par de bucles anidados se obtendrán totas las cuentas que tiene cada uno de los clientes, esto será a partr de seleccionar un elemento de la lista de clientes y 
#una vez seleccionado el elemento de la lista de clientes , este elemento seleccionará una cuenta especifica de la lista de cuentas que tiene el cliente
                       
              if int(accede_cliente)==i+1:
                  c=""
                  print("\nAccediendo a las cuentas del cliente disponibles"+"\n")
                  for j in range(len(self.clientes[i].cuenta)):
                      c="Cuenta "+str(j+1)+"\n"+str(self.clientes[i].cuenta[j])
                      print(c)
                  num_cuenta=input("\n\nElija la opción que se muestra a continuación\n: "+
                  "Presione '0' para agregar más cuentas al cliente"+"\nPresione el número de cuenta que aparece arriba para acceder a ella\n")
                  if num_cuenta=="0":
                    self.boolean=True
                    self.agregar_cuenta("s")
                  for k in range(len(self.clientes[i].cuenta)):    
                      if int(num_cuenta)==k+1:
                          print ("Accediendo a la cuenta",k+1,"\n")
                          self.menu_cuenta(self.clientes[i].cuenta[k])
                  sys.exit()
            if accede_cliente.lower()=="0":
                self.menu_inicio()
                  
        else:
            print("No hay clientes registrados en el banco")
            self.menu_inicio()
            
    
    
    def menu_cuenta(self,cuenta):
        print("------------------------------------MENÚ DE LA CUENTA------------------------------------")
        opcion_cuenta=input("\n\nA continuación se muestran las opciones de la cuenta, elija la opción deacuerdo al número que aparece\n\n"+
        "1.-Ver estado de la cuenta\n"+
        "2.-Depositar\n"+
        "3.-Retirar\n"+
        "4.-Dar de baja la cuenta\n"+
        "5.-Salír del menú\n")
        
        #Una vez terminado el proceso de cada una de las opciones que aparecen en el menú de la cuenta la consola regresará al menú de la cuenta o de otro modo podrá regresar al menú de los clientes
        
        if opcion_cuenta=="1":
            print(cuenta)
            regresar=input("¿Volver al menú de la cuenta? \nSi oprima 'S' No oprima 'N'\n")  
            while regresar.lower()!="s" and regresar.lower()!="n":
                regresar=input("Opción equivocada vuelva a ingresar la opción nuevamente\n")                
            if regresar.lower()=="s":
                self.menu_cuenta(cuenta)
            if regresar.lower()=="n":
                print("Regresando al resgistro de clientes\n")
                self.menu_cliente()
                
        if opcion_cuenta=="2":
            deposito=input("Valor de deposito\n")
            cuenta.depositar(deposito)
            r=input("Se depositaron a la cuenta $"+deposito+"\n\n"+"¿Volver al menú de la cuenta? \nSi oprima 'S' No oprima 'N'\n")              
            
            while r.lower()!="s" and r.lower()!="n":
                r=input("Opción equivocada vuelva a ingresar la opción nuevamente\n")                
            if r.lower()=="s":
                self.menu_cuenta(cuenta)
            if r.lower()=="n":                
                print("Regresando al resgistro de clientes\n")
                self.menu_cliente() 
        
        if opcion_cuenta=="3":
          retiro=input("Valor de retiro\n")
          cuenta.retirar(float(retiro))
          s=input("Se retiraron a la cuenta $"+retiro+"\n\n"+"¿Volver al menú de la cuenta? \nSi oprima 'S' No oprima 'N'\n")  
          while s.lower()!="s" and s.lower()!="n":
             s=input("Opción equivocada vuelva a ingresar la opción nuevamente\n")                
          if s.lower()=="s":
             self.menu_cuenta(cuenta)
          if s.lower()=="n":
             print("Regresando al resgistro de clientes\n")
             self.menu_cliente()
             
             
        if opcion_cuenta=="5":
            self.menu_cliente()
        
        if opcion_cuenta=="4":
            for i in range(len(self.clientes)):
                if cuenta in self.clientes[i].cuenta:
                    self.clientes[i].eliminar_cuenta(cuenta)
                    print("\n\nLa cuenta ha sido eliminada\n"+"\n\nRegresando a los registros de los clientes en el banco\n\n\n")
            
            #El siguiente bucle consiste en determinar si hay algún cliente en el banco que no contenga ninguna cuenta en el caso de que este suceso ocurra, el sistema borrará automaticamente al cliente
            
            for i in range(len(self.clientes)):         
              if len(self.clientes[i].cuenta)==0:
                print("No quedan más cuentas del cliente por lo que el cliente queda fuera del sistema")
                self.clientes.remove(self.clientes[i])
                self.menu_inicio()
                
            self.menu_cliente()  
    
    
    def guardar_registros(self):
        file=open("Registro de clientes en el banco.txt","w")
        file.write("--------------------------------------------REGISTRO DE CLIENTES DEL BANCO--------------------------------------------\n")
        for i in self.clientes:
            file.write(i.__str__())
            file.write("\n\n")
        file.close()    
            
    
    #En la grafica de de edades se analizan las edades de cada uno de los clientes
    
    def grafica_edades(self):
        ax=plt.subplot()
        edades=[int(self.clientes[i].edad) for i in range(len(self.clientes))]
        Clientes=["Cliente"+str(i+1) for i in range(len(self.clientes))]
        
        Nombres=[i for i in range(len(edades))]
        colores=[]
        for i in range(len(edades)):
          colores.append("yellow")
        
        ax.set_xticks(Nombres)
        ax.set_xticklabels(Clientes)
        
        #Recopilamos dos datos que son de suma utilidad al momento de analizar las edades como es el caso de la media y la moda.
        #Para la obtención de la media se sumaron todas las edaes de los clientes disponibles que fué divido entre la longitud de la lista de los clientes.
        #Para la obtención de la moda usamos el metodo 'count()' de la lita para que verifique la edad que se está repitiendo mas en la lista de clientes. 
        
        suma=0
        muestra=len(edades)
        for i in range(len(edades)):
         suma+=edades[i]
        media_aritmetica=suma/muestra
        datos=[]
        for i in edades:
            datos.append(edades.count(i))
        moda=0
        for j in range(len(edades)):
            if max(datos)==edades.count(edades[j]):        
              moda1=edades[j]
              colores[j]="blue"
              moda="Moda="+str(moda1)   
        plt.title("Edades de los clientes\n"+"Media aritmética= "+str(media_aritmetica),fontsize=25)
        plt.xlabel("Clientes",fontsize=20)
        plt.ylabel("Edad",fontsize=25)      
        plt.bar(Nombres,edades,color=colores,align="center")
        plt.legend([moda])
        plt.savefig("Grafica de edades")
        plt.show()

        
   #Se créo una grafica que indica la cantidad de los tipos de cuentas que hay en el banco , para ello se hizo el uso de 2 sub-listas donde cada una contiene únicamente a 1 tipo de cuenta (Ya sea de credito o ahorro).
    
    
    def get_total_cuentas(self):
        credito=len(self.cuentas_credito)
        ahorro=len(self.cuentas_ahorro)
        total=credito+ahorro
        mensaje="Se dispone en total de " + str(total)+" cuentas bancarias de las cuales "+str(credito)+" son de credito y "+str(ahorro)+" son de ahorro"+" los datos se representan en la grafica que aparece en pantalla"
        print(mensaje)
        return mensaje                             
    
    def grafica_cuentas(self):
        plt.rcParams["figure.figsize"]=[25,10]
        plt.figure()
        plt.pie([len(self.cuentas_credito),len(self.cuentas_ahorro)],autopct="%1.1f%%")
        plt.legend(["Cuentas de credito","Cuentas de ahorro"],fontsize=20)
        plt.title("Total de cuentas bancarias",fontsize=24)
        #Para hacer redonda la figura
        plt.axis("equal")
        plt.savefig("Grafica de cuentas")
        plt.show()
                                        
Banco=Banco()
Banco.menu_inicio()


