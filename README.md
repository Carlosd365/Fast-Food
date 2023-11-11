# Fast-Food

## Descripción
Fast-Food es nuestro segundo proyecto de programacion avanzada, este proyecto nos daba la oprtunidad de aplicar los conceptos de estructura de datos dinamicos y gestion de datos, simulando un programa de gestion d pedidos de un restaurante en el cual segun el menu el cliente tiene la opcion de selecionar diferentes platillos y bebidad y tambien poder deter un platillo personalizado, junto con la gestion de informacion de los clientes.

## Integrantes del Equipo

- [Abel Alexander de Leon Lima](https://github.com/Abelillo14K)
- [Carlos Daniel Gómez Aguilar](https://github.com/Carlosd365)
- [David Israel Tereta Sosof](https://github.com/David-num)

## Funcionalidades Principales
- **Tomar pedido:** En esta primera parte del menu lo que podemos hacer es: Cuando se seleciona esta opcion nos muestra el menu de los productos que hay en el restaurante, en este caso 2 platillos principales y 2 tipos de bebidas, se pueden selecionar cualquiera de estos productos la cantidad de veces que nos permita el invetario si ya no hay productos disponibles nos mostrara un mensaje de que no hay productos en el inventario, al selecionar cualquiera de estos productos nos mostrara una opcion por si queremos personalizar la orden. Esto seguira hasta que salgamos de tomar pedido, cuando salgamos de esta opcion nos dara la opcion de si queremos ingresar nit o no al pedido si elejimos que si nos pedira que ingresemos el numero de nit y con una busqueda secunacial nos dira si el cleinte esta en la lista de clientes del restaurante si esta los datos como el nombre, el telefono, la direccion y el nit se llenaran automaticamente y se ingresaran en la factura, si el nit del usuario no esta registrado le pedira que rellene los mismos datos, esos datos se guardaran en el sistema para futuras compras y los utilizaremos para llenar la factura, si el cliente no decide dar su nit esto se contara como Consumidor Final y solo se le pedira como dato el metodo de pago.
- **Ver cola de pedido:** Esta opcion lo unico que hace es mostrarnos la cola de pedidos que hay desde el primero que ingrese hasta el ultimo, esto se ira actualizando conforme vallan saliendo e ingresando los pedidos.
- **Gestionar facturas:** En esta parte del programa nos mostrara 2 opciones: La primera opcion sera la de generar factura, esto nos servira cuando el producto este listo para entregar se generara la factura con todos los datos del cliente, los del restaurante y del pedido con su total al generar la factura elimina el pedido de la cola de pedidos para que el pedido 2 se vuelva el pedido 1 y asi sucesivamete, estas facturas generadas se guardaran en un historial con ordenamineto burbuja con forme a la factura que menos a gastado hasta la que mas a gastado y oara esto se sincroniza con la opcion2 la cual nos va a mostrar este historial de facturas.
- **Agregar productos al inventario:** En el caso de que el inventario se quede vacio por la cantidad de ordenes se agrego una opcion para poder agregar mas productos al invetario selecionandolos por numer y colocando la cantidad a almacenar.
- **Mostrar el inventario:** Ya por ultimo esta opcion lo unico que realiza es que muestra el inventario del restaurante solo para ir verificando el gasto de productos.
- **Salir:** Ensta ultima opcion del programa nos permite finalizar la ejecucion del mismo.

## Manuales de uso
Puede encontrar el Manual de Usuario de nuestro proyecto en el siguiente enlace: [Maual de Usuario](https://publuu.com/flip-book/297630/691535).

Puede encontrar el Manual técnico de nuestro proyecto en el siguiente enlace: [Maual técnico](https://publuu.com/flip-book/297630/691643).