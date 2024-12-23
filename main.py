import pandas as pd
df = pd.read_csv("./stat.csv")
print(df[df["Country"] == "Uzbekistan"])