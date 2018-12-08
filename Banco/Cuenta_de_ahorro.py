from Cuenta import*

class Cuenta_ahorro(Cuenta):
    def __init__(self,valor,interes):
        super().__init__(valor)
        self.__interes=interes
        
    
    
    """Aún no se hace uso del balance de la cuenta con respecto a los meses transcurridos
    paran ello se debería de agregar un parametro al constructor que indique el tiempo que lleva el cliente con la cuenta"""
    def __str__(self):
        cadena="El cliente contiene una cuenta de ahorro con saldo actual de $"+Cuenta.__str__(self)
        cadena+=" con una tasa de interes del "+str(self.__interes)+"%" 
        return cadena
        
        
      