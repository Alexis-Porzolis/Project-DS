import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from os import system as sys

sys('cls')
df = pd.read_csv("MoviesOnStreamingPlatforms.csv", index_col=0)

print(df.count())
