import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
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
#Agregar etiquetas y valores en cada barra
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
df.Age.mode()[0]

#Reemplazamos los datos nullos por la promedio de la moda
df["Age"] = df["Age"].fillna(df["Age"].mode()[0])
#Corroboramos que ya no tenemos nulos en Age
df.Age.isnull().sum()

#Vemos los datos nulos de Rotten Tomatoes
df["Rotten Tomatoes"].isnull().sum()
"Como son 7 solo lo imprimimos para determinar que hacer con los mismos"
df[df["Rotten Tomatoes"].isnull()]
#Los elimino porque no son relevantes
df.dropna(inplace=True)

#Hasta ahora vizualisamos y limpiamos de los datos nullos!


#Categorizar todos los datos a numericos
df["Age"] = df["Age"].str.replace('+','')
df["Rotten Tomatoes"] = df["Rotten Tomatoes"].str.replace('/','').str.replace('100','')

#Cambiamos el tipo de dato de Rotten Tomatoes
df["Rotten Tomatoes"] = df["Rotten Tomatoes"].astype(np.int64)

#Cambiando nombres de las columnas
df.rename(columns={"Age":"Minimumn Age","Year":"Premiere"}, inplace=True)

#Creacion de df_ml
df_ml = df.copy()

#Unificacion de las 4 columnas: Netflix, Hulu, Disney+, Prime Video
df["Platform"] = df.apply(lambda row:", ".join(df.columns[row == 1]), axis=1)

#Comprobacion de la nueva columna
df["Platform"].unique()
df["Platform"].value_counts()
df["Platform"].describe()

#Eliminacion de las 4 columnas
df.drop(columns = ['Netflix','Disney+','Hulu','Prime Video'], inplace = True)

#Verificamos
df

#Ordenamos por Premiere
df = df.sort_values(by="Premiere")


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