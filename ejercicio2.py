'''
Juan tiene N cantidad de pesos, Camila tiene la mitad de lo que posee
Juan y Ricardo tiene la mitad de lo que poseen Camila y Juan Juntos.
¿Puede PYTHON ayudarme a calcular la cantidad de dinero de los 3+(1)
'''

juan = int(input("¿Cuánto dinero tiene Juan? $"))

camila = juan/2

ricardo = (camila + juan)/2

print(f"Juan tine ${juan}")
print(f"Camila tiene ${camila}")
print(f"Ricardo tiene ${ricardo}")