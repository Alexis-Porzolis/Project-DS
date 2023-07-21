import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from os import system as sys

sys('cls')
df = pd.read_csv("MoviesOnStreamingPlatforms.csv", index_col=0)

#Creacion de la variable null
null_count = df.isnull().sum()

#Vizualisar datos nulos
plt.figure(figsize=(10,6))
null_count.plot(kind="bar")
plt.title("Count of null values per column")
plt.xlabel("Columns")
plt.ylabel("Number of null values")
plt.show()
