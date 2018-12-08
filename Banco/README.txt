Nombre: Nicolás Mata Jesús


Aquí se explicará detalladamente el funcionamiento y el uso adecuado del proyecto elaborado.

-El "main" se encuentra en la clase Banco donde se podrá inciar el funcionamiento del codigo implementado.
-Una vez inciado el codigo nos mostrará un listado de opciones que simulan el funcionamiento de un banco donde se podrá elegir:
 1.-Crear un cliente.
 2.-Elegir un cliente.
 3.-Salir del sistema

A continuación describiremos cada una de las opciones.

----AGREGAR CLIENTE----

Al momento de que elijamos esta opción nos aparecé un formulario de datos que nostros debemos llenar, este formulario incluye el nombre, la edad y la dirección correspondiente al usuario.

Una vez llenado estas trés opciones enseguida nos apararecerá un par de opciones para elegir el tipo de cuenta del usuario, dentro de este tipo de cuentas se encuentra "Cuenta de credito" y "Cuenta de ahorro".
Seleccionada la opción de la cuenta, si se trató de una cuenta de Credito entonces debemos de llenar los datos que corresponden a la cantidad de la cuenta y su sobregiro, si se trató de una cuenta de ahorro, se tienen que llenar la cantidad de la cuenta y la tasa de interés.

Posteriormente, aparecerán un par de opciones más que nos preguntará si queremos ver los datos del cliente y si queremos agregar más cuentas al cliente, pasando a estas opciones nos regresará al menú principal que se mostró al inicio del programa.


----ELEGIR CLIENTE----

Si no hay clientes registrados con anterioridad se notificará que no hay ningún cliente disponible y regresará nuevamente al menú principal
Si hay clientes registrados, aparecerá un listado de forma enumerada con respecto a los clientes que fueron registrados, abjo contendrá el nombre del cliente con el número de cuentas que tiene disponible, se puede representar con el siguiente ejemplo:

Cliente 1
Nombre: Antonio
Cuentas: 3

Cliente 2
Nombre: Erika
Cuentas: 5  
.
.
.
.

Para acceder a las cuentas que tiene un cliente en particular, presionamos el número que corresponde a la enumeración establecida del listado del cliente, es decir si queremos seleccionar al cliente con el nombre "Antonio" debemos de presionar el número "1" pues en la enumeración del listado aparece como "Cliente 1", de otro modo si queremos acceder a las cuentas de Erika presionamos el número "2" pues en el listado aparece como "Cliente 2".
También podemos volver al menú principal presionando el boton 0.

Una vez presionado el número que corresponde al cliente en el listado de registros, apareceran todas las cuentas disponibles de ese cliente de forma enumerada con todos los detalles, volviendo al ejemplo anterior, supongamos que queremos ver la cuentas disponibles del cliente Antonio, una vez seleccionado el número aparaceran todos los detalles de sus cuentas en este caso dado que tiene 3 cuentas se podrá ver algo como esto:

Cuenta 1
El cliente contiene una cuenta de ahorro de $x con tasa de interés del $y 

Cuenta 2
El cliente contiene una cuenta de ahorro de $x con tasa de interés del $y

Cuenta 3
El cliente contiene una cuenta de credito de $z con sobregiro de $w


Queremos acceder a la segunda cuenta, el funcionamiento es similar al del cliente,es decir, presionamos el número que corresponde a la enumeración del listado de las cuentas que en este caso es el "2", los mismo sucederia en la tercera cuenta , presionariamos el botos "3" para acceder a sus especificaciones.

También podemos agregar más cuentas al cliente pulsando el botón "0"

Cuando accedemos a una cuenta nos aparecerá una seríe de opciones como sigue:

1.-Ver estado de la cuenta
2.-Depositar
3.-Retirar
4.-Dar de baja la cuenta
5.-Salír del menú

Elegimos el número que contiene al inicio de la opción, si queremos depositar presionamos "2", si queremos dar de baja la cuenta presionamos "4"
Una vez terminado el proceso de la opción elegida (a excepción de la cuarta y quinta opción que te regresa al listado de clientes) nos preguntará si queremos volver al menú de opciones de la cuenta o volver al menú de los clientes.



----SALIR DEL SISTEMA----
En esta opción se termina todo el proceso incluyendo con sigo mismo a todos los datos de los clientes que fueron registrados junto con los datos de cada uno de sus cuentas.
También se imprimen un par de graficas que muestran las edades de los clientes y moda del total de clientes registrados junto con su media aritmetica.
Y la segunda grafica corresponde a las cuentas totales que fueron registradas.

 



 


