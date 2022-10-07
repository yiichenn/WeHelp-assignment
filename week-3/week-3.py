import urllib.request as request
import json

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用 json 模組處理 json 資料格式
list=data["result"]["results"]
#取得名稱列表出來

with open("data.csv","w",encoding="utf-8") as file:
    for row in list:
        #print(first_jpg)
        if int(row["xpostDate"][0:4])>=2015:
            first_jpg=(row["file"]).lower().split("jpg",1) #lower()字母全部轉小寫
            file.write(row["stitle"]+","+row["address"][5:8]+","+row["longitude"]+","+row["latitude"]+","+first_jpg[0]+"jpg"+"\n")
# import csv
# with open("data.cvs","w",encoding="utf-8",newline="")as csvfile:
#     writer = csv.writer(csvfile)
#     for row in list:
#         # writer = csv.Dictwriter(csvfile)
#         first_jpg=(row["file"]).lower().split("jpg",1) #lower()字母全部轉小寫
#         # writer.writerows(row)
#         # writer.writerows([row["stitle"]+row["address"][5:8]+row["longitude"]+row["latitude"]+first_jpg[0]+"jpg"+"\n"])
#         writer.writerow([row["stitle"]]+[row["address"][5:8]]+[row["longitude"]]+[row["latitude"]]+[first_jpg[0]+"jpg"])