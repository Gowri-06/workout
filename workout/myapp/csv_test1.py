import pandas as pd

pd.options.display.max_rows = 7000
var1 = pd.read_csv("E:/csv_ file_ folder/100 Records.csv")
var1.drop_duplicates(subset="Region",inplace=True)
# var1.drop_duplicates(inplace=True)
print(var1)
print(var1.duplicated())

# var1.to_csv("E:/csv_ file_ folder/duplicates_removed.csv")

