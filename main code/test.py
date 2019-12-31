import csv
import random

csvFile = open("shanghaiData.csv")

reader = csv.reader(csvFile)

poiData = []

for item in reader:
    if reader.line_num == 1:
        continue
    newItem = [round(float(item[0]) * 100, 2), round(float(item[1]) * 100, 2)]
    if 12197 > newItem[0] > 12100 and 3141 > newItem[1] > 3100:
        poiData.append(newItem)

csvFile.close()

data = random.sample(poiData, 4000)
csvFile = open("shData4000.csv", "w")
writer = csv.writer(csvFile)

fileHeader = ["x", "y"]

writer.writerow(fileHeader)

for item in data:
    writer.writerow(item)
csvFile.close()

