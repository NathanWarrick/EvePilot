import pandas as pd

df = pd.read_csv(r"src/assets/temp/inv.csv", index_col=0)

moon_ores = [
    "Bitumens",
    "Brimful Bitumens",
    "Coesite",
    "Brimful Coesite",
    "Sylvite",
    "Brimful Sylvite",
]

hold_ore = []

# for ore in moon_ores:
#     if df["Name"].eq(ore).any():
#         hold_ore.append(ore)
