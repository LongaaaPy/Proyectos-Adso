''''print("Lista de Estudiantes!")
mis_estudiantes=[]
nombres = input("Ingresa el nombre de un estudiante (o 'off' para terminar): ")
while nombres.lower() != 'off':
    mis_estudiantes.append(str(nombres))  
    nombres = input("Ingresa el nombre de un estudiante (o 'off' para terminar): ")
for nombres in mis_estudiantes:
    print(nombres)


usuarios = {
    "Longa1234":"Moneda1234",
    "Dalay1234":"Moneda1234",
    "Jenifer1234":"Moneda1234",
}
usuario=input("Ingrese su username: ")
password=input("Ingrese su password: ")
if usuario in usuarios and usuarios[usuario] == password:
    print("Welcome :) " + usuario)
else:
    print("Hubo un error intentalo de nuevo :(")'''''
    
    
print("Suma de numero!")

numero_1= int(input("Ingrese un numero: "))

numero_2= int(input("Ingrese un numero: "))

sum_num= (numero_1 + numero_2)
print("El resultado de la suma es: ",sum_num)