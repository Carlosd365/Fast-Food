class InventariFacturas:
    def __init__(self):
        self.nomfactu = []
        self.direcfactu = []
        self.telfactu = []
        self.nitfactu = []
        self.total = []

    def calcular_precio_adicionales(self, opciones_personalizadas):
        total_opciones_adicionales = 0
        for opcion_personalizada in opciones_personalizadas:
            total_opciones_adicionales += opcion_personalizada["costo"]
        return total_opciones_adicionales

    def agregar(self,pedido, metodo_pago, cliente):
        self.nomfactu.append(cliente.nombre)
        self.direcfactu.append(cliente.direccion)
        self.telfactu.append(cliente.telefono)
        self.nitfactu.append(cliente.nit)
        opciones_total = self.calcular_precio_adicionales(pedido.opciones_personalizadas)
        total = sum([menu.precios[menu.platillos.index(alimento)] for alimento in pedido.alimentos] +
                    [menu.precios[len(menu.platillos) + menu.bebidas.index(bebida)] for bebida in pedido.bebidas]) + opciones_total
        self.total.append(total)

    def mostrar(self):
        if len(self.nomfactu) > 0:
            n = len(self.total)
            for i in range(n):
                for j in range(0,n-i-1):
                    if self.total[j]>self.total[j+1]:
                        self.total[j],self.total[j+1]=self.total[j+1],self.total[j]
                        self.nomfactu[j],self.nomfactu[j+1]=self.nomfactu[j+1],self.nomfactu[j]
                        self.telfactu[j],self.telfactu[j+1]=self.telfactu[j+1],self.telfactu[j]
                        self.direcfactu[j],self.direcfactu[j+1]=self.direcfactu[j+1],self.direcfactu[j]
                        self.nitfactu[j],self.nitfactu[j+1]=self.nitfactu[j+1],self.nitfactu[j]
        
            for i in range(0,len(self.nomfactu)):
                print("-"*40)
                print("\n---*** Factura ***---")
                print(f"Cliente: {self.nomfactu[i]}")
                print(f"Dirección: {self.direcfactu[i]}")
                print(f"Teléfono: {self.telfactu[i]}")
                print(f"NIT: {self.nitfactu[i]}")
                print('')
                print('Restaurante Rata feliz')
                print("Teléfono de contacto: 8894-4563")
                print("-" * 30)            
                print(f"Total a pagar: Q{self.total[i]}")
                print("¡Gracias por su compra!")
                print("-" * 30)
                print(f"Pago del pedido procesado con {metodo_pago}")
                print("")
        else :
            print("No hay facturas")
                
class Pedido:
    def __init__(self, alimentos, bebidas, opciones_personalizadas, cliente = None):
        self.alimentos = alimentos
        self.bebidas = bebidas
        self.opciones_personalizadas = opciones_personalizadas
        self.cliente = cliente

    def agregar_opcion_personalizada(self, alimento, opcion, costo):
        self.opciones_personalizadas.append({"alimento": alimento, "opcion": opcion, "costo": costo})

class Inventario:
    def __init__(self, productos):
        self.productos = productos

    def actualizar_inventario(self, pedido):
        for alimento in pedido.alimentos:
            if alimento in self.productos and self.productos[alimento] > 0:
                self.productos[alimento] -= 1
            else:
                print(f"No hay suficiente catidad de {alimento} en el inventario. El pedido no se agregará.")
                return False

        for bebida in pedido.bebidas:
            if bebida in self.productos and self.productos[bebida] > 0:
                self.productos[bebida] -= 1
            else:
                print(f"No hay suficiente cantidad de {bebida} en el inventario. El pedido no se agregará.")
                return False

        return True

    def agregar_inventario(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def mostrar_inventario(self):
        print('')
        print("Inventario:")
        for producto, cantidad in self.productos.items():
            print(f"{producto}: {cantidad}")
            print('')

class OpcionesExtra:
    def __init__(self):
        self.opciones = {
            "Hamburguesa🍔": {"Queso extra": 5, "Carne extra": 10, "Agrandado": 8},
            "Pizza🍕": {"Queso extra": 5, "Queso en la orilla": 7},
            "Refresco🧋": {"Refil": 3}
        }

    def mostrar_opciones(self, alimento):
        if alimento in self.opciones:
            print(f"\nOpciones adicionales para {alimento}:")
            opciones_alimento = self.opciones[alimento]
            for opcion, costo in opciones_alimento.items():
                print(f"{opcion}: Q{costo}")
        else:
            print(f"No hay opciones adicionales disponibles para {alimento}.")

class Menu:
    def __init__(self, platillos, bebidas, precios, opciones_extra):
        self.platillos = platillos
        self.bebidas = bebidas
        self.precios = precios
        self.opciones_extra = opciones_extra

    def mostrar_menu(self):
        print('')
        print("Menu:")

        for i in range(len(self.platillos)):
            print(f"{i + 1}. {self.platillos[i]} - Q{self.precios[i]}")

        for i in range(len(self.bebidas)):
            print(f"{i + len(self.platillos) + 1}. {self.bebidas[i]} - Q{self.precios[i + len(self.platillos)]}")

class ColaPedidos:
    def __init__(self, pedidos):
        self.pedidos = pedidos

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_pedidos(self):
        if not self.pedidos:
            print("La cola de pedidos está vacía.")
        else:
            print("Cola de Pedidos:")
            for i, pedido in enumerate(self.pedidos, 1):
                print('')
                print(f"Pedido {i}:")
                print(f"  Alimentos: {', '.join(pedido.alimentos)}")
                print(f"  Bebidas: {', '.join(pedido.bebidas)}")
                print('')
                print("  Opciones Personalizadas:")
                for opcion in pedido.opciones_personalizadas:
                    print(f"    {opcion['opcion']} para {opcion['alimento']}: Q{opcion['costo']}")

class Facturacion:
    def __init__(self, pedidos):
        self.pedidos = pedidos

    def calcular_precio_opciones_adicionales(self, opciones_personalizadas):
        total_opciones_adicionales = 0
        for opcion_personalizada in opciones_personalizadas:
            total_opciones_adicionales += opcion_personalizada["costo"]
        return total_opciones_adicionales

    def generar_factura(self, pedido, metodo_pago, cliente):
        print("-"*40)
        print("\n---*** Factura ***---")
        print(f"Cliente: {cliente.nombre}")
        print(f"Dirección: {cliente.direccion}")
        print(f"Teléfono: {cliente.telefono}")
        print(f"NIT: {cliente.nit}")
        print('')
        print('Restaurante Rata feliz')
        print("Teléfono de contacto: 8894-4563")
        print("-" * 40)
        print("Descripción del pedido:")

        for alimento in pedido.alimentos:
            print(f" {alimento}: Q{menu.precios[menu.platillos.index(alimento)]}")

        for bebida in pedido.bebidas:
            print(f" {bebida}: Q{menu.precios[len(menu.platillos) + menu.bebidas.index(bebida)]}")

        opciones_total = self.calcular_precio_opciones_adicionales(pedido.opciones_personalizadas)
        if opciones_total > 0:
            print("\nOpciones adicionales:")
            for opcion in pedido.opciones_personalizadas:
                print(f" {opcion['opcion']} para {opcion['alimento']}: Q{opcion['costo']}")

        total = sum([menu.precios[menu.platillos.index(alimento)] for alimento in pedido.alimentos] +
                    [menu.precios[len(menu.platillos) + menu.bebidas.index(bebida)] for bebida in pedido.bebidas]) + opciones_total

        print("-" * 30)
        print(f"Total a pagar: Q{total}")
        print("¡Gracias por su compra!")
        print("-" * 30)
        print(f"Pago del pedido procesado con {metodo_pago}")
        print("")

class Cliente:
    def __init__(self, nombre, direccion, telefono, nit, metodo_pago):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.nit = nit
        self.metodo_pago = metodo_pago

class AdministracionClientes:
    def __init__(self, clientes):
        self.clientes = clientes

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente_por_nit(self, nit):
        for i, cliente in enumerate(self.clientes):
            if cliente.nit == nit:
                return i
        return -1

opciones_extra = OpcionesExtra()
menu = Menu(["Hamburguesa🍔", "Pizza🍕"], ["Refresco🧋", "Agua🫗"], [25, 40, 10, 7], opciones_extra)
inventario = Inventario({"Hamburguesa🍔": 10, "Pizza🍕": 5, "Refresco🧋": 20, "Agua🫗": 15})
cola_pedidos = ColaPedidos([])
facturacion = Facturacion([])
admin_clientes = AdministracionClientes([])
factura = InventariFacturas()

while True:
    print("-"*45)
    print("|  Bienvenido al restaurante Rata feliz :3.")
    print("|")
    print("|  Por favor, seleccione una opción:")
    print("|  1. Tomar un pedido")
    print("|  2. Ver la cola de pedidos")
    print("|  3. Gestion de facturas")
    print("|  4. Agregar cantidad de productos al inventario")
    print("|  5. Mostrar inventario")
    print("|  6. Salir")
    print("-"*45)
    opcion = input("Opción: ")

    if opcion == "1":
        alimentos = []
        bebidas = []
        opciones_personalizadas = []

        while True:
            menu.mostrar_menu()
            print('')
            opcion = input("Seleccione lo que desea consumir (presione 0 para terminar): ")

            if opcion == "0":
                break
            elif opcion.isdigit() and int(opcion) in range(1, len(menu.platillos) + len(menu.bebidas) + 1):

                opcion = int(opcion)

                if opcion <= len(menu.platillos):
                    alimentos.append(menu.platillos[opcion - 1])
                    alimento_seleccionado = menu.platillos[opcion - 1]
                else:
                    bebidas.append(menu.bebidas[opcion - len(menu.platillos) - 1])
                    alimento_seleccionado = menu.bebidas[opcion - len(menu.platillos) - 1]

                opciones_extra.mostrar_opciones(alimento_seleccionado)
                confirmacion = input(f"\n¿Desea opciones adicionales para {alimento_seleccionado}? (S/N): ").strip().lower()

                if confirmacion == 's':
                    opciones_alimento = opciones_extra.opciones[alimento_seleccionado]
                    for opcion, costo in opciones_alimento.items():
                        confirmacion_opcion = input(f"¿Desea {opcion} por Q{costo}? (S/N): ").strip().lower()
                        if confirmacion_opcion == 's':
                            opciones_personalizadas.append({"alimento": alimento_seleccionado, "opcion": opcion, "costo": costo})
                            print(f"Se agregó {opcion} por Q{costo} al pedido.")

        while True:

            decea = input('Decea agregar nit (S/N): ').strip().lower()

            if decea == 's':
                nit_buscar = input("Ingrese el NIT del cliente: ")
                metodo_pago = input("Método de pago del cliente: ")

                resultado = admin_clientes.buscar_cliente_por_nit(nit_buscar)

                if resultado != -1:
                    cliente = admin_clientes.clientes[resultado]
                    cliente.metodo_pago = metodo_pago
                    print(f'Cliente encontrado en la posición {resultado}:')
                    print(f'Nombre: {cliente.nombre}')
                    print(f'Dirección: {cliente.direccion}')
                    print(f'Teléfono: {cliente.telefono}')
                    print(f'NIT: {cliente.nit}')
                else:
                    print('')
                    print('Cliente no registrado, tomo los siguientes datos')
                    nombre = input("Nombre del cliente: ")
                    direccion = input("Dirección del cliente: ")
                    telefono = input("Teléfono del cliente: ")
                    nit = nit_buscar
                    
                    cliente = Cliente(nombre, direccion, telefono, nit, metodo_pago)
                    admin_clientes.agregar_cliente(cliente)

                break

            elif decea == 'n':
                print('')
                metodo_pago = input("Método de pago del cliente: ") 
                cliente = Cliente("C/F", "No Aplica", "No Aplica", "No aplica", metodo_pago)
                break

            else:
                print('Opcion no valida')

        pedido = Pedido(alimentos, bebidas, opciones_personalizadas, cliente)
        cola_pedidos.agregar_pedido(pedido)
        inventario.actualizar_inventario(pedido)

    elif opcion == "2":
        cola_pedidos.mostrar_pedidos()

    elif opcion == "3":
        print("1. Generar factura\n2. Ver facturas\n")
        t = input("Selecione una opcion: ")
        if t == "1":
            if cola_pedidos.pedidos:
                facturacion.generar_factura(cola_pedidos.pedidos[0], cola_pedidos.pedidos[0].cliente.metodo_pago, cola_pedidos.pedidos[0].cliente)
                factura.agregar(cola_pedidos.pedidos[0], cola_pedidos.pedidos[0].cliente.metodo_pago, cola_pedidos.pedidos[0].cliente)
                cola_pedidos.pedidos.pop(0)
            else:
                print("No hay pedidos en la cola.")
        elif t == "2":
            factura.mostrar()
        else :
            print("Opción invalida")

    elif opcion == "4":
        print('')
        print("Productos disponibles para agregar al inventario:")
        for i, producto in enumerate(inventario.productos, 1):
            print(f"{i}. {producto}")

        try:
            seleccion = int(input("Seleccione el número del producto que desea agregar al inventario: "))
            productos_disponibles = list(inventario.productos.keys())
            if 1 <= seleccion <= len(productos_disponibles):
                producto = productos_disponibles[seleccion - 1]
                cantidad = int(input(f"Ingrese la cantidad de {producto} a agregar al inventario: "))
                inventario.agregar_inventario(producto, cantidad)
                print(f"Se agregaron {cantidad} {producto}(s) al inventario.")
                print('')
            else:
                print("Número de producto no válido. Intente nuevamente.")
                print('')
        except ValueError:
            print("Por favor, ingrese un número válido.")
            print('')

    elif opcion == "5":
        inventario.mostrar_inventario()

    elif opcion == "6":
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")