from Cliente import*
class Cuenta:    
    """Nuestro constructor tendrá dos atributos que seran tomados en cuenta como variables de tipo booleano de tal modo que estas variables
     notifiquen al estado de la cuenta en el caso de que se haya hecho un retiro o deposito"""
    
    def __init__(self,balance):
        self.__cantidad=balance
        self.boleano=False
        self.boleano_deposito=False
        self.valor_deposito=0
    
    def depositar(self,valor):
        valor=float(valor)
        self.__cantidad=float(self.__cantidad)
        self.valor_deposito=valor  
        if valor>=0:
         self.boleano_deposito=True   
         self.__cantidad=self.__cantidad+valor
        else:
         print("Error al momento de realizar el deposito")
    
    def retirar(self,valor):
        valor=float(valor)
        self.__cantidad=float(self.__cantidad)
        self.valor_retiro=valor  
        if valor>=0 and valor<=self.__cantidad:
            self.__cantidad=self.__cantidad-valor
            self.boleano=True
        else:
            print("Error al momento de efectuar el retiro")

    
    def __str__(self):
        return str(self.__cantidad)
    
    def get_balance(self): #Este metodo nos devuelve la cantidad disponible que tiene el cliente
        return self.__cantidad
    
    def get_valordeposito(self): #Este metodo nos será de uso para agregar el valor de deposito a nuestra cantidad en el monto del cliente
        return self.valor_deposito
         
         
       
        




        
                
        

        