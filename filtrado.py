#FILTRAR
a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)


a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = [i for i in range (n) if a[i] >= 1000]
print(filtered_array)

#SELECCIONAR TODOS LOS ELEMENTOS MAYOR O IGUAL A MIL
a = [100, 200, 1000, 5000, 10000, 10, 5000]
filtered_array = [i for i in a if i >= 1000]
print(filtered_array)


#ADICTO A REDES
min_usuarios = [120, 50, 600, 30, 90, 10, 200, 0, 500] 
clasif = []
for i in min_usuarios:
    if i < 90:
        clasif.append ("bien")
    else:
        clasif.append ("mal")
print (clasif)


#TRANSFORMANDO SEGUNDOS EN MINUTOS
seconds = [100, 50, 1000, 5000, 1000, 500]
minutos = []
for i in seconds:
    minutos.append (int(i/60))
print (minutos)

#PAISES
pais = ["México", "Chile", "Argentina"]
cant_usuarios = [70,50,55]

#Alternativa 1
diccionario = dict(zip(pais, cant_usuarios))
print (diccionario)

#Alternativa 2
diccionario = {k:v for k,v in zip(pais,cant_usuarios)}
print (diccionario)

pais_menos_usuarios = {k:v for k,v in diccionario.items() if v <60}
print (pais_menos_usuarios)

"""pais_menos_usuarios = diccionario[cant_usuarios]
for v in diccionario.valor:
       pais_menos_usuarios.append  (v < 60)
print(pais_menos_usuarios)"""

#VENTAS
#1.CONVERTIR LA TABLA EN UN DICCIONARIO
mes = ["Octubre", "Noviembre", "Diciembre"]
ventas = [65000, 68000, 72000]
dict_venta = {k:v for k,v in zip(mes,ventas)} 
print (dict_venta)

#2.MODIFICA EL DICCIONARIO PARA INCREMENTAR LAS VENTAS EN UN 10%
dict_venta_10 = {k:round(v*1.1) for k,v in dict_venta.items()} 
print (dict_venta_10)

#3.NUEVO DICCIONARIO CON VENTAS DISMINUIDAS UN 20%
dict_venta_20 = {k:round(v*0.8) for k,v in dict_venta.items()}
print (dict_venta_20)
