from Cuenta import*
from Cliente import*
class Cuenta_credito(Cuenta):
    """def __init__(self,valor,sobregiro):
           super().__init__(valor)
           self.__sobregiro=sobregiro
         def __init__(self,valor):
           super().__init__(valor)
           self.__sobregiro=0"""

    
    def __init__(self, *args):
        if len(args) == 2:
            super().__init__(args[0])
            self.__cantidad=args[0]
            self.boleano=False  
            self.__sobregiro=args[1]
        
        if len(args) == 1:
            super().__init__(args[0])
            self.__cantidad=args[0]
            self.__sobregiro=0
            self.boleano=False      
            
    def retirar(self,valor):
      valor=float(valor)
      self.__cantidad=float(self.__cantidad)
      self.__sobregiro=float(self.__sobregiro)
      self.valor_retiro=valor  
      if valor>=0  : #Primero nos aseguramos de que nuestros retiros siempre sean positivos
        saldo_disponible=self.__cantidad+self.__sobregiro
        if valor<=saldo_disponible: #Nuestro valor de retiro no debe de exceder a nuestro balance más nuestra cantidad de sobregiro 
          self.boleano=True
          if valor<=self.__cantidad:
              self.__cantidad=self.__cantidad-valor
          else: #Si nuestro valor de retiro es más grande que nuestro balance dejara nuestro saldo en 0 y el sobrante se sustraerá al nuestra cantidad de sobregiro
              self.__cantidad=0
              self.valor_deposito=0
              self.__sobregiro=saldo_disponible-valor
        else:
          print("La cantidad de retiro sobrepasa a la cantidad disponible en la cuenta por lo que no es posible realizar el retiro")     
      else:
          print("No se puede llevar a cabo el retiro")
          
 
    def __str__(self):
      self.__cantidad=float(self.__cantidad)  
      if self.boleano_deposito==True:  #En el caso de que se efectue un deposito nos aseguramos de que se notifique en la consola
          self.__cantidad=self.__cantidad+self.get_valordeposito()
          self.boleano_deposito=False
      cadena="El cliente contiene una cuenta de credito con saldo actual de $"+str(self.__cantidad)
      cadena+=" y su cantidad de sobregiro es de $"+str(self.__sobregiro)+"\n"    
      return cadena
  
  
  
    
          
          