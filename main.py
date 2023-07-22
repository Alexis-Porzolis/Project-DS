import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from os import system as sys

sys('cls')
df = pd.read_csv("MoviesOnStreamingPlatforms.csv", index_col="ID", na_values="#N/D")
df.head(5)
df.info()

#Mostramos los datos nullos de todo el DF
values_ascending =df.isna().sum().sort_values(ascending=False)
print(values_ascending)

#Eliminamos los datos que no aportan dentro del DF
df.drop(columns = ['Unnamed: 0','Type'], inplace = True)

#Creacion de la variable null
null_counts = df.isnull().sum()

#Vizualisamos los datos nulos
plt.figure(figsize=(12,8))
ax = null_counts.plot(kind="bar", color= "skyblue", edgecolor="black")
# Agregar etiquetas y valores en cada barra
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Creamos la funcion nullpercentage
def nullpercentage (df):
    null = (df.isnull().sum()/len(df))*100
    print (f"Percentage of null values\n{null}%")

#Usamos la funcion nullpercentage()
nullpercentage(df["Age"])
nullpercentage(df["Rotten Tomatoes"])

#Priorizamos la optimizacion de Age
df.Age.unique()
df.Age.describe()
df["Age"].mode()[0]

#Reemplazamos los datos nullos por la promedio de la moda
df["Age"] = df["Age"].fillna(df["Age"].mode()[0])
#Corroboramos que ya no tenemos nulos en Age
df.Age.isnull().sum()



#No usar
""" #Determinamos las variables numericas mediantes estadisticas
def statistics_cont(num):
    statistics = num.describe().T
    #Añadimos la mediana
    statistics["median"] = num.median()
    #Reordenamos 
    statistics = statistics.iloc[:,[0,1,8,2,3,4,5,6,7]]
    #Retornamos
    return(statistics)

#Usamos la funcion statistics_cont()
statistics_cont(df.select_dtypes('number')) """