from Cuenta import*
from Cliente import*
from Cuenta_de_ahorro import*
from Cuenta_de_credito import*

class Menu:
    def __init__(self):
        pass
    
    def menu_cliente():
      print("-------------------NUEVO UN CLIENTE-------------------\n","\n")
      nombre=input("Nombre del cliente: ")
      edad=input("Edad: ")
      direccion=input("Dirección: ")
      print("\n-------------------Cuentas del cliente-------------------\n")
      tipo=input("Tipo de cuenta (Elija la opción de acuerdo al numero)"+"\n1.-Ahorro"+"\n2.-Credito"+"\n")
      valor=input("Cantidad de la cuenta: ")
      cuentas=[]
      if int(tipo)==2:
          sobregiro=input("Cantidad de sobregiro: ")
          cuenta=Cuenta_credito(valor,sobregiro)
      else:
          cuenta=Cuenta_ahorro(valor)
      print("\nCLIENTE REGISTRADO\n")
      print("\nDatos del cliente: ")
      cliente=Cliente(nombre,direccion,edad,cuentas)
      cliente.agregar_cuenta(cuenta)
      print(cliente)
      

print("----------Banco Regional----------","\n")
print("Elija la opción correspondite: ","\n")
opcion=input("1.-Crear un cliente"+"\n2.-Elegir un cliente"+"\n3.-Salir"+"\n")
if int(opcion)==1:
   Menu.menu_cliente()
    

    
    
    
    