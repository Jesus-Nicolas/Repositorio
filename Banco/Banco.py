from Cuenta import*
from Cliente import*
from Cuenta_de_ahorro import*
from Cuenta_de_credito import*

class Banco:
    def __init__(self,clientes):
        self.__cliente=clientes
        
    def __str__(self): #Este metodo va imprimir una lista de los datos del cliente
       Cadena="----------Banco Regional----------\n"+"\n"
       Cadena+="Dirección: Ubicado en calle ABC Ciudad de México\n" +"\n"
       Cadena+="Registro de los clientes disponibles en el banco:\n"+"\n"
       for i in range(len(self.__cliente)):
         Cadena+=str(self.__cliente[i])+"\n"+"\n"
       return Cadena
   
    """def lista_de_cuentas(self,customer): #Este medoto devolverá unicamente los datos de las cuentas que tienen o tiene el cliente dependiendo del tamaño del parametro que contenga
        cadena_datos=""
        for i in range(len(customer)):
            cadena_datos+="Datos de las cuentas del cliente "+str(customer[i].nombre)+"\n"       
            cadena_datos+=str(customer[i].cuenta)+"\n"+"\n"
            if customer[i].cuenta.boleano==True:
                print("El cliente",customer[i].nombre,"ha realizado un retiro de $",customer[i].cuenta.valor_retiro,"\n")
                customer[i].cuenta.boleano=False
            if customer[i].cuenta.boleano_deposito==True:
                print("El cliente",customer[i].nombre,"ha realizado un deposito de $",customer[i].cuenta.valor_deposito,"\n")
                customer[i].cuenta.boleano_deposito=False
        return cadena_datos """
        
        
        
      
#Creamos las cuentas de cada cliente              
cuenta1=Cuenta_credito(65000,5000)
cuenta2=Cuenta_ahorro(3000)
cuenta3=Cuenta_ahorro(1000)
cuenta4=Cuenta_credito(7000)
cuenta5=Cuenta_ahorro(250000)

#Creamos una lista que contenga las cuentas del cliente
cuentas=[cuenta1,cuenta2,cuenta3]

#Creamos los objetos cliente
cliente1=Cliente("Jesús Nicolás","Dirección 1",19,cuentas)
#La lista tendrá como elementos a los clientes 
Clientes=[cliente1]
banco_resgistro_de_clientes=Banco(Clientes)           
print(banco_resgistro_de_clientes)
print(cliente1.get_cuenta(3))
cliente1.agregar_cuenta(cuenta4)
cliente1.eliminar_cuenta(cuenta1)
print(banco_resgistro_de_clientes)
cliente1.get_cuenta(1).depositar(2000)
"""cliente2=Cliente("Nombre B","Dirección 2",18,cuenta2)
cliente3=Cliente("Nombre C","Dirección 3",22,cuenta3)
cliente4=Cliente("Nombre D","Dirección 4",21,cuenta4)
cliente5=Cliente("Nombre E","Dirección 5",35,cuenta5)

print("DATOS SOBRE LAS CUENTAS DE LOS CLIENTES","\n")
#Este objeto tendrá únicamente en cuenta las listas de los clientes 
lista=[cliente1,cliente2]
print(banco_resgistro_de_clientes.lista_de_cuentas(lista))


#Funcionamiento de los metodos retirar y depositar en una cuenta de credito
print("DATOS SOBRE LAS CUENTAS DE LOS CLIENTES UNA VEZ HECHO ALGUNOS DEPOSITOS Y RETIROS","\n")
cuenta1.retirar(45000)
cuenta2.retirar(2000)
print(banco_resgistro_de_clientes.lista_de_cuentas([cliente1,cliente2]))
cuenta1.depositar(9000)
print(banco_resgistro_de_clientes.lista_de_cuentas([cliente1]))
cuenta2.depositar(500)
print(banco_resgistro_de_clientes.lista_de_cuentas([cliente2]))
cuenta1.retirar(30000)
print(banco_resgistro_de_clientes.lista_de_cuentas([cliente1]))"""
  
        