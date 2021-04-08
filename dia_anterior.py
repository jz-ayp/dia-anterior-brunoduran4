"""
Codifica tu solución en este archivo.
"""
print("Tarea: Tarea extra 3: Día anterior")
print("Autor: Bruno Mauricio Duran Dominguez")
print("Fecha de entrega: 08/04/2021")
print("Grupo: <Tu grupo ESI-4522-17>")
print("Profesor: Jorge Adalberto Zaldivar Carrillo")
print()
print("Descripción:")
print("El programa calculará, a continuación, la fecha correspondiente al día anterior a la fecha introducida.")
print()
# Entradas
print("Fecha inicial:")
h=int(input("    Dia: "))
m=int(input("    Mes: "))
s=int(input("    Año: "))

# Proceso

if h == 1:
    h=28
    m -= 1
else:
    h -= 1
if m  == 28 :
    m = 0
if s == 28:
    s -=1
if s  < 59:   
    s -= 1

# Salidas
print("Un día antes:")
print("    Dia", h)
print("    Mes", m)
print("    Año", s)
