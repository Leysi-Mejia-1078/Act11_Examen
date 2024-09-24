print("Examen Clase Pedido")
print("")

# Zona Clase

class Pedido1078:
    num_pedido=0
    fecha=""
    cliente=0
    cant_prod=0
    estado=""
    cantidadT=0
    entrega=""

    # Clase mostrar datos

    def mostrardatos(sel):
        print(f"Numero de pedido: {ped.num_pedido}, 
        \nFecha: {ped.fecha}, \nId Cliente: {ped.cliente}, 
        \nCantidad productos: {ped.cant_prod} productos, 
        \nEstado: {ped.estado}, \nCantidad Total: ${ped.cantidadT}, 
        \nMetodo de entrega: {ped.entrega}")

    def lista_productos(self):
        lista_prod= ["Cadena", "Pendientes", "Brazalete", "Gargantilla", "Anillos"]
        print(lista_prod)
        for x in lista_prod:
            print(x)

    def tupla_cant_Prod(self):
        tupla_cant_prod= (3, 4, 2, 1, 5)
        print(tupla_cant_prod)
        for x in tupla_cant_prod:
            print(x)

    def diccionario_precioProd(self):
        diccionario_cantP = {
            "Cadena: $": 30000,
            "Pendientes $": 20000,
            "Brazalete: $": 30000,
            "Gargantilla: $": 60000,
            "Anillo: $": 25000
        }
        print(diccionario_cantP)
        for x,y in diccionario_cantP.items():
            print(x,y)

    def alta(self):
        print(" El producto se ha dado de alta de manera correcta")
    def baja(self):
        print(" El producto se ha dado de baja de manera correcta")

ped= Pedido1078()
ped.num_pedido=1234
ped.fecha="24-09-2024"
ped.cliente=123
ped.cant_prod=8
ped.estado="En proceso de entrega"
ped.cantidadT=350000
ped.entrega="A domicilio"

ped.mostrardatos()
print("------------------------------------------")
ped.lista_productos()
print("------------------------------------------")
ped.tupla_cant_Prod()
print("------------------------------------------")
ped.diccionario_precioProd()
print("------------------------------------------")
ped.alta()
print("------------------------------------------")
ped.baja()