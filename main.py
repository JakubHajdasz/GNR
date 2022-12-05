import time
import plotly
import plotly.graph_objects as go
import pandas as pd

excel_file = 'minuty.xlsx'

print("Odczytywanie pliku")
df = pd.read_excel(excel_file)

print("Obliczanie średniej intensywności ruchu")
srednia = df['intensywnosc'].mean()


a = df['minuta']
b = df['ruch']

for i in range(len(b)):
    b[i] = b[i] * srednia


print("Obliczanie godziny największego ruchu")
highest = 0
highest_index = 0

for i in range(0, len(b) - 59):
    current = 0
    for j in range(0, 59):
        current = current + b[i+j]
    if current > highest:
        highest = current
        highest_index = i


c=[]
d=[]


for i in range(int(highest_index), int(highest_index) + 60, 1):
    c.append(a[i])
    d.append(b[i])

print("GNR:")
print(int(c[0]/60))
