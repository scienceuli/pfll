# beispiel_square.py

from square import Square

a = int(input("Kantenlänge: "))

quadrat = Square(a)

print(f'Fläche des Quadrats: {quadrat.get_area()}')
print(f'Durchmesser des Quadrats: {quadrat.get_diameter()}')