import pandas as pd
import matplotlib.pyplot as plt

print("Bienvenido a 'App Analytics Pro', una aplicación que te permite tener una idea de cuánto tiempo pasas en tus aplicaciones favoritas y cuánto tiempo pasa la gente en esas aplicaciones.")

usuario_local = input("¿Cuál es tu nombre?: ")
print("¡Hola, {}, espero que estés bien!".format(usuario_local))

app = input("Por favor, indícame cuáles son tus aplicaciones favoritas, separadas por comas (,): ")
lista = app.split(",")
print("Lista guardada:", ", ".join(lista))

horas = []
promedios = []
for aplicacion in lista:
    horas_aplicacion = input("Cuántas horas utilizas {}? ".format(aplicacion))
    horas.append(int(horas_aplicacion))
promedio_horas = sum(horas) / len(horas)
apps = pd.DataFrame()
apps["aplicaciones"] = lista
apps["horas"] = horas

for i, hora in enumerate(apps["horas"]):
    if hora > promedio_horas:
        print("Tú usas {} más que el promedio".format(apps["aplicaciones"][i]))
    elif hora < promedio_horas:
        print("Tú usas {} menos que el promedio".format(apps["aplicaciones"][i]))
    else:
        print("Tú usas {} igual que el promedio".format(apps["aplicaciones"][i]))

horasmin = apps["horas"].min()
horasmax = apps["horas"].max()

plt.bar(apps["aplicaciones"], apps["horas"])
plt.xlabel("Aplicaciones")
plt.ylabel("Horas")
plt.title("Consumo de aplicaciones")

for i, hora in enumerate(apps["horas"]):
    plt.text(i, hora, str(hora), ha='center', va='bottom')
plt.axhline(y=promedio_horas, color='r', linestyle='--', label='Promedio')
plt.legend()
plt.show()