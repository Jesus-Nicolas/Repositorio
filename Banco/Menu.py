from Cuenta import*
from Cliente import*
from Cuenta_de_ahorro import*
from Cuenta_de_credito import*

class Menu:
    def __init__(self):
        self.cliente=None
        self.clientes=[]
   
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
          self.cliente=Cliente(nombre,direccion,edad,cuentas)
          self.cliente.agregar_cuenta(cuenta)
          self.clientes.append(self.cliente)
      elif tipo=="2":
          valor=input("Cantidad de la cuenta: ")
          sobregiro=input("Cantidad de sobregiro: ")
          cuenta=Cuenta_credito(valor,sobregiro)
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
                self.cliente.agregar_cuenta(cuenta)
              elif tipo=="2":
                valor=input("Cantidad de la cuenta: ")
                sobregiro=input("Cantidad de sobregiro: ")
                cuenta=Cuenta_credito(valor,sobregiro)
                self.cliente.agregar_cuenta(cuenta)
              else:
                print("Tipo de cuenta no disponible") 
              add=input("¿Se agregaran más cuentas al cliente?\n"+"Si, oprima 's'\n"+"No, oprima 'n'\n")
        self.menu_inicio()           
    
    def menu_cliente(self):
        if len(self.clientes)!=0:
            print("Clientes registrados en el banco: ","\n")
            cadena=""
            for i in range(len(self.clientes)):
              cadena="Cliente "+str(i+1)+"\n"+"\n"
              cadena+="Nombre del cliente: "+self.clientes[i].nombre+"\n"
              cadena+="Número de cuentas: "+str(len(self.clientes[i].cuenta))+"\n"
              print(cadena)  
            print("El número de cliente se muestra en la parte superior","\n")
            accede_cliente=input("Presione el número que corresponde al cliente para administrar sus cuentas"+" o presione 'v' para volver al menú\n")
            for i in range(len(self.clientes)):                
              if int(accede_cliente)==i+1:
                  c=""
                  print("\nAccediendo a las cuentas del cliente disponibles"+"\n")
                  for j in range(len(self.clientes[i].cuenta)):
                      c="Cuenta "+str(j+1)+"\n"+str(self.clientes[i].cuenta[j])
                      print(c)
            if accede_cliente.lower()=="v":
                self.menu_inicio()
                  
        else:
            print("No hay clientes registrados en el banco")
            self.menu_inicio()
            
            

Menu=Menu()
Menu.menu_inicio()
    
    
    
    