print("Programa para contar números de mayor a menor")
mi_lista = []
elemento = input("Ingresa un número (o 'off' para terminar): ")
while elemento.lower() != 'off':
    mi_lista.append(int(elemento))  
    elemento = input("Ingresa otro número (o 'off' para terminar): ")
mi_lista.sort()
mayor = mi_lista[-1]
menor = mi_lista[0]
print("La lista completa es:", mi_lista)
print("Este es el número mayor en la lista:", mayor)
print("Este es el número menor en la lista:", menor)




