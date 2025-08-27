## Importaciomes 
from Data.ItalikaContext import ItalikaContext
from Models.Moto import Moto
from Utils.Inventario import Inventario

# Inicializando clase de Datos
ctx = ItalikaContext()

## Creandi un nuevo modelo de moto
nueva_moto = Moto("TC300", 48000.20, 300, "Negro", 100)
if ctx.insertMoto(nueva_moto):
    print("Insert exitoso.")
else:
    print("Falló el insert.")


##Consultando motos
motos : list[Moto] = ctx.getMotos()


## Variable temporal para usar en vender motos
vender_ultima_moto : Moto

for moto in motos:
    print(moto)
    vender_ultima_moto = moto # usare la ultima moto iterada

## Consultando total de motos  
cantidad : int = Inventario.motosStock(motos)
print(f"Hay {cantidad} motos en la empresa ")

## Vendiendo la ultima moto
Inventario.venderMoto(vender_ultima_moto)


##Consultando motos
motos = ctx.getMotos()
for moto in motos:
    print(moto)

# ## Borrar modelo moto
# Inventario.borrarModelo(vender_ultima_moto)

# ##Consultando motos
# motos = ctx.getMotos()
# for moto in motos:
#     print(moto)