
#Construir un programa que permita ingresar 10 números enteros y cuente cuantos múltiplos de 3 fueron ingresados

cont = 0
numero = 0

for i in range(10):
    numero = int(input("Ingrese un número: "))
    if numero % 3 == 0:
        cont = cont +1
        
print(f"En su lista hay {cont} múltiplos de 3.")
    


