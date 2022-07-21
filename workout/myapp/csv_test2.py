import pandas as pd


pd.options.display.max_rows = 7000
var1 = pd.read_csv("E:/csv_ file_ folder/100 Records.csv")

filtered_data = var1.loc[var1["Region"] == "West"]
value = pd.DataFrame(filtered_data)
print("fgeeen",value)
value.to_csv("E:/csv_ file_ folder/filtered_data.csv",index=False)
