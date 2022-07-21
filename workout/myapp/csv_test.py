from audioop import maxpp
import pandas as pd
import csv
import os

# pd.options.display.max_rows = 7000
# var1 = pd.read_csv("E:\csv_ file_ folder\employees.csv")
# var1.drop_duplicates(subset="Team",keep="last",inplace=True)
# var1.dropna(inplace=True)
# print(var1.drop(columns=["Gender","Team"]))
# var2 = "developerrr"
# var1["Gender"].fillna(var2, inplace=True)
# var1.loc[0, "Team"] = "Sunlight"
# res = var1["Total"] = var1.iloc[:, 4:6].sum(axis=1)
# res = var1.loc[(var1["Senior Management"] == True) & (var1["Team"] == "Marketing") & (var1["Gender"] == "Male")]
# res = var1.loc[var1["Team"].str.contains("es", na=False)]
# res = var1.loc[var1["Team"] == "Sales", "Team"] = "Salesforce"
# res = var1.loc[var1["Team"] == "Sales", "Gender"] = "human"
# var1.loc[var1["Salary"] > 10000, ["Bonus %", "First Name"]] = ["testvalue11","testvalue22"] 
# print(var1)
# res.to_csv("filtered.csv")
# res.to_csv("E:/csv_ file_ folder/filo.csv")
# print(var1.iloc[0, 1])
# for index, row in var1.iterrows():
    # print(row["Team"])
# ans = var1.loc[var1["Team"] == "Sales"]
# print(ans)
# print(var1.describe())
# res = var1.sort_values(["Team", "Salary"], ascending=False)
# print(var1.sort_values(["Team", "Salary"], ascending=[1,0]))
# coloumn value ocurring multiple no of times:
# var1["Team"] = var1["Team"].replace({"Finance":"Muthoot Finance"}) 
# print(var1)

# open_file = open("E:\csv_ file_ folder\data.csv", "r")
# reader = csv.DictReader(open_file)
# print("readererrererr",reader)
# list = []
# for data in reader:
#     print(data)
#     row = {
#            "Duration":data["Duration"],
#            "Pulse":data["Pulse"],
#            "Maxpulse":data["Maxpulse"],
#            "Calories":data["Calories"]
#           }
#     print(row)
#     list.append(row)
# print(list)
# open_file.close()
# yeah_open = open("E:\csv_ file_ folder\simpledata.csv", "w", newline="")
# headers = ["Duration","Pulse","Maxpulse","Calories"]
# wmode = csv.DictWriter(yeah_open,delimiter=",", fieldnames=headers)
# wmode.writeheader()
# wmode.writerow(dict((heads,heads) for heads in headers))
# wmode.writerows(list)
# yeah_open.close()



# read contents of csv file
# file = pd.read_csv("E:\csv_ file_ folder\data.csv")
# print("\nOriginal file:")
# print(file)

# adding header
# headerList = ['Dura', 'Puls rate', 'Maxpulse high','caloriesone']

# converting data frame to csv
# file.to_csv("E:\csv_ file_ folder\simpledata2.csv", header=headerList, index=False)

# display modified csv file
# file2 = pd.read_csv("E:\csv_ file_ folder\simpledata2.csv")
# print('\nModified file:')
# print(file2)

# list = ["E:/csv_ file_ folder/employees.csv","E:/csv_ file_ folder/data.csv"]
# nice = pd.read_csv("E:/csv_ file_ folder/username.csv",sep=";")
# for csv_file in list:
#     print(csv_file)
#     df = pd.read_csv(csv_file)
#     print(df)
#     df.to_csv("E:/csv_ file_ folder/master.csv",header=True,mode="a",index=False)
# nice.to_csv("E:/csv_ file_ folder/master.csv",header=True,mode="a",index=False)
# var1 = pd.read_csv("E:/csv_ file_ folder/username.csv",)
# print(var1)

# lst = [["one","two"],["three","four"],["five","six"]] 
# lst2 = ["7","8"]
# lst3 = ["seven","eight"]
# df = pd.DataFrame(lst,columns=["Number","Number"],dtype=float)
# df.iloc[2] = lst3
# df.columns = ["columns_1","columns_2"]
# # df.transpose()
# df.loc[len(df)] = lst2
# print(df.transpose())

#Assignment Csv:

pd.options.display.max_rows = 7000
var1 = pd.read_csv("E:/csv_ file_ folder/100 Records.csv")
# print(var1)
# print(var1.duplicated())

# var1.drop_duplicates(inplace=True)
# var1.to_csv("E:/csv_ file_ folder/duplicates_removed.csv")
red = var1.loc[var1["Region"] == "West"]
green = pd.DataFrame(red)
print("fgeeen",green)
green.to_csv("E:/csv_ file_ folder/filtered_data.csv",index=False)
# print(result2)
# res = var1.loc[var1["Team"] == "Sales", "Gender"] = "human"
# var1.loc[var1["Region"] == "West", "First Name"] = "Ben"
# var1.to_csv("E:/csv_ file_ folder/changed_data.csv")
# print(result)
# print(result3)
































