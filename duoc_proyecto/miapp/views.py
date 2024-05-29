from django.shortcuts import render
from miapp.models import Producto
# Create your views here.
def mostrarFormRegistrar(request):
    return render(request,'form_registrar.html')

def mostrarListado(request):
    pro = Producto.objects.all().values()
    datos = {'pro':pro}
    return render(request,'listado.html',datos)

def insertarProducto(request):
    if request.method == 'POST':
        nom = request.POST ['txtnom']
        mar = request.POST ['cbomar']
        pre = request.POST ['txtpre']        
        pro = Producto(nombre=nom, marca=mar, precio=pre)
        pro.save()
        datos = {'r' : 'Registro Actualizado'}
        return render(request, 'form_registrar.html',datos)
    else:
        datos = {'r2' : 'Registro con error'}
        return render(request,'listado.html',datos)

def eliminarProducto(request, id):
    try: 
        pro = Producto.objects.get(id==id)
        pro.delete()
        pro = Producto.objects.all().values()
        datos = {
            'pro':pro,
            'r':'Registro eliminado'
        }

        return render(request, 'listado.html', datos)
    except:
        pro = Producto.objects.get(id==id)
        pro.delete()
        pro = Producto.objects.all().values()
        datos = {
            'pro':pro,
            'r2':'El Registro no existe, no se puede eliminar'
        }

        return render(request, 'listado.html', datos)