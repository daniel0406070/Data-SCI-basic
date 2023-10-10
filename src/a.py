import pandas as pd

df = pd.DataFrame([
  ['Apple', 7, 5, 'Fruit'],
  ['Banana', 3, 6, 'Fruit'],
  ['Beef', 5, 2, 'Meal'],
  ['Kimchi', 4, 8, 'Meal']],
  columns=["Name", "Frequency", "Importance", "Type"],
  index=["A", "B", "C", "D"])

df["Gap"] = df.groupby("Type")["Frequency"].apply(lambda x: x - x.mean())
print(df)