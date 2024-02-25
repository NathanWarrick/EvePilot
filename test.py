import pandas as pd

df = pd.read_csv(r"src/assets/temp/inv.csv", index_col=0)

print(df["Price"].sum())
