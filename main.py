#ith open ("weather_data.csv") as weather:
#   forcast=weather.readlines()
#   print(forcast)
#import csv
#with open("weather_data.csv")as data_files:
    #data=csv.reader(data_files)
    #temprature=[]
    #for row in data:
    #    print(row)
    #    if row[1]!="temp":
    #        temprature.append(int(row[1]))
    #print(temprature)
#
#import pandas
#data=pandas.read_csv("weather_data.csv")
#print(data["temp"])
#data_dict=data.to_dict()
#print(data_dict)
#temp_list=data["temp"].to_list()
#print(temp_list)
#print(data["temp"].mean())
#print(data["temp"].max())
import csv

import pandas

#with open ("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as squirrel_data:
     #data=csv.reader(squirrel_data)
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count=len(data[data["Primary Fur Color"]=="Gray"])
Black_squirrels_count=len(data[data["Primary Fur Color"]=="Black"])
Red_squirrels_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
print(grey_squirrels_count)
print(Black_squirrels_count)
print(Red_squirrels_count)
data_dict={"Fur Colors":['Gray','Black','Red'],"Count":[grey_squirrels_count,Black_squirrels_count,Red_squirrels_count]}
print(data_dict)
df=pandas.DataFrame(data_dict)
df. to_csv("squirrel_color_data.csv")