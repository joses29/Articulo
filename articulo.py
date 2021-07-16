
articulo
cliente
venta
ventadet

class Articulo:
    def __init__(self,cod,des,pre,sto):
        self.codigo=cod
        self.descripcion=des
        self.precio=pre
        self.stock=sto

class Cliente:
    def __init__(self,ced,nom,num,dir,tel):
        self.cedula=ced
        self.nombre=nom
        self.direcion=dir
        self.telefono=tel
class Venta:
    def __init__(self,fac,fec,cliente,tot,detalle):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=tot
        self.detalle = detalle
class VentaDet:
    def __init__(self,venta,producto,precio,cantidad):
        self.producto=producto
        self.precio=pre
        self.antidad=cantidad


class Venta:
    def __init__(self,fac,fec,cliente,tot,detalleven):
        self.factura=fac
        self.fecha=fec
        self.cliente=cliente
        self.total=tot
        self.detalleven = detalleven
        
