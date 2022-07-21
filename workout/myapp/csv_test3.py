import pandas as pd


pd.options.display.max_rows = 7000
var1 = pd.read_csv("E:/csv_ file_ folder/100 Records.csv")
var1.loc[var1["Region"] == "West", "First Name"] = "Ben"
var1.to_csv("E:/csv_ file_ folder/changed_data.csv")



