from Cuenta import*
class Cliente:
    def __init__(self,nom,dir,edad,cuenta):
        self.nombre=nom
        self.direccion=dir
        self.edad=edad
        self.cuenta=cuenta
   
    def __str__(self):
      cuentas=""
      for i in range(len(self.cuenta)):
          cuentas=cuentas+"Cuenta "+str((i+1))+" \n"+" \n"+str(self.cuenta[i])+"\n"
      if int(self.edad)>=18:  
        tmp="Nombre del cliente: "+str(self.nombre)
        tmp+="\nEdad: "+str(self.edad)
        tmp+="\nDirección: "+str(self.direccion)
        tmp+="\nCuentas: \n"+cuentas
        return tmp
      else:
       return "El usuario no dispone de la edad suficiente para utilizar una cuenta"
#Metodos para agregar y eliminar una cuenta al cliente
        
    def agregar_cuenta(self,cuenta):
        self.cuenta.append(cuenta)
        print("El cliente "+self.nombre+" ha agregado una nueva cuenta")
    
    def eliminar_cuenta(self,cuenta):
      if cuenta in self.cuenta:  
        self.cuenta.remove(cuenta)
        print("El cliente "+self.nombre+" ha eliminado una cuenta")
      else:
        print("No se puede encontrar la cuenta")  
#Metodo para devolver una cuenta particular del cliente

    def get_cuenta(self,n):
        m=n-1
        if 0<=m<len(self.cuenta):
          return self.cuenta[m]
        else:
          return "No se encontró la cuenta seleccionada"  
