import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from os import system as sys

sys('cls')
df = pd.read_csv("MoviesOnStreamingPlatforms.csv", index_col="ID", na_values="#N/D")
values_ascending =df.isna().sum().sort_values(ascending=False)
print(values_ascending)
#Creacion de la variable null
null_counts = df.isnull().sum()

#Vizualisar datos nulos
plt.figure(figsize=(10,6))
null_counts.plot(kind="bar")
plt.title("Count of null values per column")
plt.xlabel("Columns")
plt.ylabel("Number of null values")
plt.show()

#Creamos la funcion nullpercentage
def nullpercentage (df):
    null = (df.isnull().sum()/len(df))*100
    print (f"Percentage of null values\n{null}%")

#Usamos la funcion
nullpercentage(df["Age"])
nullpercentage(df["Rotten Tomatoes"])
